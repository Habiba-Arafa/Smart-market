from datetime import datetime
from shop import db

class Addproduct(db.Model):
    __tablename__ = 'addproduct'
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    discount = db.Column(db.Integer, default=0)
    stock = db.Column(db.Integer, nullable=False)
    colors = db.Column(db.Text, nullable=False)
    desc = db.Column(db.Text, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('categories', lazy=True))
    brand_id = db.Column(db.Integer, db.ForeignKey('brand.id'), nullable=False)
    brand = db.relationship('Brand', backref=db.backref('brands', lazy=True))
    image_1 = db.Column(db.String(150), nullable=True)
    image_2 = db.Column(db.String(150), nullable=True)
    image_3 = db.Column(db.String(150), nullable=True)

    def __repr__(self):
        return f'<Addproduct {self.name}>'



class Brand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)

    def __repr__(self):
        return f'<Brand {self.name}>'

class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    products = db.relationship('Addproduct', backref='product_category', cascade='all, delete-orphan')

    
    def __repr__(self):
        return f'<Category {self.name}>'

