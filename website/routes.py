import os
import secrets
from flask import render_template, url_for, flash, redirect, request
from unwrap import app, db, bcrypt
from unwrap.models import User, Products, Cart
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy import func, update

def getLoginDetails():
    if current_user.is_authenticated:
        noOfItems = Cart.query.filter_by(buyer=current_user).count()
    else:
        noOfItems = 0
    return noOfItems

# Home page endpoint
@app.route("/")
@app.route("/home")
def home():
    noOfItems = getLoginDetails()
    return render_template('home.html', noOfItems=noOfItems)

# Signup endpoint
@app.route("/signup", methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirmPassword')
        role = request.form.get('role')
        
        # Basic validation and registration logic
        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('signup'))
        
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user = User(email=email, password=hashed_password, role=role)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    
    noOfItems = getLoginDetails()
    return render_template('signup.html', noOfItems=noOfItems)

# Login page endpoint
@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=True)
            next_page = request.args.get("next")
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    noOfItems = getLoginDetails()
    return render_template('login.html', noOfItems=noOfItems)

# Logout endpoint
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

# Profile page endpoint (common for both vendor and customer)
@app.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        
        # Update user details in database
        current_user.firstname = firstname
        current_user.lastname = lastname
        current_user.email = email
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('profile'))
    
    noOfItems = getLoginDetails()
    return render_template('profile.html', noOfItems=noOfItems)

# Vendor Profile page endpoint
@app.route("/profile/vendor", methods=['GET', 'POST'])
@login_required
def vendor_profile():
    if current_user.role != 'vendor':
        flash('Access Denied', 'danger')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        # Handle vendor-specific logic (like updating products or business details)
        pass
    
    noOfItems = getLoginDetails()
    return render_template('vendor_profile.html', noOfItems=noOfItems)

# Customer Profile page endpoint
@app.route("/profile/customer", methods=['GET', 'POST'])
@login_required
def customer_profile():
    if current_user.role != 'customer':
        flash('Access Denied', 'danger')
        return redirect(url_for('home'))
    
    noOfItems = getLoginDetails()
    return render_template('customer_profile.html', noOfItems=noOfItems)

# Cart page endpoint
@app.route("/cart", methods=["GET", "POST"])
@login_required
def cart():
    noOfItems = getLoginDetails()
    cart_items = Cart.query.filter_by(buyer=current_user).all()
    subtotal = sum([item.product.price * item.quantity for item in cart_items])
    
    if request.method == "POST":
        qty = request.form.get("qty")
        product_id = request.form.get("idpd")
        cart_item = Cart.query.filter_by(product_id=product_id, buyer=current_user).first()
        cart_item.quantity = qty
        db.session.commit()
        flash('Cart updated successfully!', 'success')
    
    return render_template('cart.html', cart=cart_items, noOfItems=noOfItems, subtotal=subtotal)

# Add product to cart endpoint
@app.route("/addToCart/<int:product_id>")
@login_required
def add_to_cart(product_id):
    product = Products.query.get_or_404(product_id)
    cart_item = Cart.query.filter_by(product_id=product_id, buyer=current_user).first()
    
    if cart_item:
        cart_item.quantity += 1
        flash('This item is already in your cart, quantity updated!', 'success')
    else:
        new_cart_item = Cart(buyer=current_user, product_id=product_id, quantity=1)
        db.session.add(new_cart_item)
        flash('Item added to your cart!', 'success')
    
    db.session.commit()
    return redirect(url_for('select_products'))

# Remove product from cart endpoint
@app.route("/removeFromCart/<int:product_id>")
@login_required
def remove_from_cart(product_id):
    cart_item = Cart.query.filter_by(product_id=product_id, buyer=current_user).first()
    db.session.delete(cart_item)
    db.session.commit()
    flash('Item removed from cart', 'success')
    return redirect(url_for('cart'))

# Products selection page endpoint
@app.route("/select_products", methods=['GET', 'POST'])
def select_products():
    noOfItems = getLoginDetails()
    products = Products.query.all()
    return render_template('select_products.html', products=products, noOfItems=noOfItems)

# Contact for issue page endpoint
@app.route("/contact", methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Handle sending email or storing the message for later
        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))
    
    noOfItems = getLoginDetails()
    return render_template('contact.html', noOfItems=noOfItems)

# Manage products page (for vendors)
@app.route("/manage_products", methods=['GET', 'POST'])
@login_required
def manage_products():
    if current_user.role != 'vendor':
        flash('Access Denied', 'danger')
        return redirect(url_for('home'))
    
    if request.method == 'POST':
        # Handle product creation or updating
        product_name = request.form.get('name')
        product_price = request.form.get('price')
        product_description = request.form.get('description')
        
        new_product = Products(name=product_name, price=product_price, description=product_description, seller=current_user)
        db.session.add(new_product)
        db.session.commit()
        flash('Product added successfully!', 'success')
    
    noOfItems = getLoginDetails()
    products = Products.query.filter_by(seller=current_user).all()
    return render_template('manage_products.html', products=products, noOfItems=noOfItems)

# Product details page
@app.route("/product/<int:product_id>")
def product_details(product_id):
    noOfItems = getLoginDetails()
    product = Products.query.get_or_404(product_id)
    return render_template('product_details.html', product=product, noOfItems=noOfItems)