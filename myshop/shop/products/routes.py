import os
from flask import request, render_template, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from shop import app, db
from .models import Addproduct, Brand, Category
from .forms import AddProductForm

@app.route('/')
def home():
    products = Addproduct.query.paginate(page=request.args.get('page', 1, type=int), per_page=8)
    brands = Brand.query.all()
    categories = Category.query.all()
    return render_template('products/index.html', products=products, brands=brands, categories=categories)

@app.route('/product/<int:id>')
def single_page(id):
    product = Addproduct.query.get_or_404(id)
    brands = Brand.query.all()
    categories = Category.query.all()
    return render_template('products/single_page.html', product=product, brands=brands, categories=categories)

@app.route('/brand/<int:id>')
def get_brand(id):
    brand_products = Addproduct.query.filter_by(brand_id=id).paginate(
        page=request.args.get('page', 1, type=int), per_page=3)
    brands = Brand.query.all()
    categories = Category.query.all()
    return render_template('products/index.html', products=brand_products, brands=brands, categories=categories)

@app.route('/categories/<int:id>')
def get_category(id):
    category_products = Addproduct.query.filter_by(category_id=id).paginate(
        page=request.args.get('page', 1, type=int), per_page=3)
    brands = Brand.query.all()
    categories = Category.query.all()
    return render_template('products/index.html', products=category_products, brands=brands, categories=categories)

# ================= CART ====================
@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(float(item['price']) for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    product = Addproduct.query.get_or_404(product_id)
    cart_item = {
        'id': product.id,
        'name': product.name,
        'price': float(product.price),
        'image': product.image_1
    }
    cart = session.get('cart', [])
    cart.append(cart_item)
    session['cart'] = cart
    session.modified = True
    flash(f"{product.name} has been added to your cart.", 'success')
    return redirect(url_for('cart'))

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    cart = [item for item in cart if item['id'] != product_id]
    session['cart'] = cart
    session.modified = True
    flash("Item removed from your cart.", 'info')
    return redirect(url_for('cart'))

# ================= BRANDS ====================
@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if "email" not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    
    if request.method == "POST":
        item_name = request.form.get('name')

        if item_name:
            existing_brand = Brand.query.filter_by(name=item_name).first()
            if existing_brand:
                flash(f'The brand "{item_name}" already exists.', 'warning')
            else:
                brand = Brand(name=item_name)
                db.session.add(brand)
                db.session.commit()
                flash(f'The brand "{item_name}" was added successfully!', 'success')
        else:
            flash('Please provide a valid brand name.', 'danger')

        return redirect(url_for('addbrand'))

    return render_template('products/addbrand.html', title='Add Brand', item_type='brand')


@app.route('/addcat', methods=['GET', 'POST'])
def addcat():
    if "email" not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    
    if request.method == "POST":
        item_name = request.form.get('name')

        if item_name:
            existing_category = Category.query.filter_by(name=item_name).first()
            if existing_category:
                flash(f'The category "{item_name}" already exists.', 'warning')
            else:
                category = Category(name=item_name)
                db.session.add(category)
                db.session.commit()
                flash(f'The category "{item_name}" was added successfully!', 'success')
        else:
            flash('Please provide a valid category name.', 'danger')

        return redirect(url_for('addcat'))

    return render_template('products/addbrand.html', title='Add Category', item_type='category')





@app.route('/updatebrand/<int:id>',methods=['GET','POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}','success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/updatebrand.html', title='Udate brand',brands='brands',updatebrand=updatebrand)




@app.route('/deletebrand/<int:id>', methods=['GET','POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database","success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))



@app.route('/updatecat/<int:id>',methods=['GET','POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please','danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method =="POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('category'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update Category Page',updatecat=updatecat)


@app.route('/deletecat/<int:id>', methods=['GET','POST'])
def deletecat(id):
    category = Category.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(category)
        db.session.commit()
        flash(f"The brand {category.name} was deleted from your database","success")
        return redirect(url_for('admin'))
    flash(f"The brand {category.name} can't be  deleted from your database","warning")
    return redirect(url_for('admin'))



@app.route('/addproduct', methods=['GET', 'POST'])
def add_product():
    if "email" not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    form = AddProductForm()

    if form.validate_on_submit():
        # Create a new product instance
        new_product = Addproduct(
            name=form.name.data,
            price=form.price.data,
            discount=form.discount.data,
            stock=form.stock.data,
            colors=form.colors.data,
            desc=form.desc.data,
            category_id=form.category_id.data,
            brand_id=form.brand_id.data
        )

        # Use app.root_path to get the project directory and then static/uploads folder
        image_folder = os.path.join(app.root_path, 'static', 'uploads')

        # Check if the uploads folder exists, if not, create it
        if not os.path.exists(image_folder):
            os.makedirs(image_folder)
            print(f"Created uploads folder at {image_folder}")

        # Debug: Check if the folder was created
        print(f"Uploads folder path: {image_folder}")

        # Handle Image 1 upload
        if form.image_1.data:
            image_1_filename = secure_filename(form.image_1.data.filename)
            image_1_path = os.path.join(image_folder, image_1_filename)  # Saving in uploads folder
            try:
                form.image_1.data.save(image_1_path)
                new_product.image_1 = image_1_filename  # Save image name to the database
                print(f"Image 1 saved at {image_1_path}")
            except Exception as e:
                print(f"Error saving Image 1: {e}")
                flash('Error saving Image 1. Please try again.', 'error')

        # Handle Image 2 upload
        if form.image_2.data:
            image_2_filename = secure_filename(form.image_2.data.filename)
            image_2_path = os.path.join(image_folder, image_2_filename)  # Saving in uploads folder
            try:
                form.image_2.data.save(image_2_path)
                new_product.image_2 = image_2_filename
                print(f"Image 2 saved at {image_2_path}")
            except Exception as e:
                print(f"Error saving Image 2: {e}")
                flash('Error saving Image 2. Please try again.', 'error')

        # Handle Image 3 upload
        if form.image_3.data:
            image_3_filename = secure_filename(form.image_3.data.filename)
            image_3_path = os.path.join(image_folder, image_3_filename)  # Saving in uploads folder
            try:
                form.image_3.data.save(image_3_path)
                new_product.image_3 = image_3_filename
                print(f"Image 3 saved at {image_3_path}")
            except Exception as e:
                print(f"Error saving Image 3: {e}")
                flash('Error saving Image 3. Please try again.', 'error')

        # Add the new product to the database and commit
        try:
            db.session.add(new_product)
            db.session.commit()
            flash('Product added successfully!', 'success')
            print(f"Product {new_product.name} added to the database.")
        except Exception as e:
            print(f"Error adding product to the database: {e}")
            flash('Error adding product. Please try again.', 'error')

    return render_template('products/addproduct.html', form=form)




@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    brands = Brand.query.all()
    categories = Category.query.all()
    product = Addproduct.query.get_or_404(id)
    brand = request.form.get('brand')
    category = request.form.get('category')
    form = AddProductForm(request.form)
  
    if request.method =="POST":
         product.name = form.name.data 
         product.price = form.price.data
         product.discount = form.discount.data
         product.stock = form.stock.data 
         product.colors = form.colors.data
         product.desc = form.desc.data
         product.category_id = category
         product.brand_id = brand

         db.session.commit()

  

         flash('The product was updated','success')
         return redirect(url_for('admin'))
    form.name.data = product.name
    form.price.data = product.price
    form.discount.data = product.discount
    form.stock.data = product.stock
    form.colors.data = product.colors
    form.desc.data = product.desc
    # brand = product.brand.name
    # category = product.category.name
    return render_template('products/updateproduct.html', form=form, title='Update Product',product=product, brands=brands,categories=categories)



@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    product = Addproduct.query.get_or_404(id)
    if request.method =="POST":
        db.session.delete(product)
        db.session.commit()
        flash(f'The product {product.name} was delete from your record','success')
        return redirect(url_for('admin'))
    flash(f'Can not delete the product','success')
    return redirect(url_for('admin'))

