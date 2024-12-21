from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField, DecimalField, FileField
from wtforms.validators import DataRequired, NumberRange
from .models import Category, Brand

class AddProductForm(FlaskForm):
    name = StringField('Product Name', validators=[DataRequired()])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)], places=2)
    discount = IntegerField('Discount', default=0, validators=[NumberRange(min=0, max=100)])
    stock = IntegerField('Stock Quantity', validators=[DataRequired(), NumberRange(min=0)])
    colors = TextAreaField('Colors', validators=[DataRequired()])
    desc = TextAreaField('Description', validators=[DataRequired()])
    category_id = SelectField('Category', coerce=int, choices=[], validators=[DataRequired()])
    brand_id = SelectField('Brand', coerce=int, choices=[], validators=[DataRequired()])
    image_1 = FileField('Image 1')
    image_2 = FileField('Image 2')
    image_3 = FileField('Image 3')

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.category_id.choices = [(category.id, category.name) for category in Category.query.all()]
        self.brand_id.choices = [(brand.id, brand.name) for brand in Brand.query.all()]
