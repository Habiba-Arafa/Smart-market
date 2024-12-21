from flask import render_template, session, request, redirect, url_for, flash
from shop import app, db
from .forms import RegistrationForm, LoginForm
from .models import User
from shop.products.models import Addproduct,Brand,Category
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app) 

@app.route('/admin')
def admin():
    if "email" not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    
    products = Addproduct.query.all()  
    return render_template('admin/index.html', title='Admin Page', products=products)


@app.route('/brands')
def brands():
    if "email" not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    brands = Brand.query.order_by(Brand.id.desc()).all()
    return render_template('admin/brand.html', title='brands',brands=brands)


@app.route('/category')
def category():
    if "email" not in session:
        flash('Please log in first.', 'danger')
        return redirect(url_for('login'))
    categories = Category.query.all()
    return render_template('admin/brand.html', title='Categories', categories=categories)





@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == "POST" and form.validate():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data, username=form.username.data, email=form.email.data, password=hash_password)
        
        db.session.add(user)
        db.session.commit()

        flash(f'Welcome {form.name.data}, thanks for registering!', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', title='Registration Page', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == "POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()

        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email'] = form.email.data 
            flash(f'Welcome back, {form.email.data}! You are now logged in.', 'success')
            
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Incorrect email or password.', 'danger')

    return render_template('admin/login.html', title='Login Page', form=form)
