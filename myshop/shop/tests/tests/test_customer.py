import unittest
from shop import app, db
from shop.customers.models import Register
from shop.customers.forms import CustomerRegisterForm


import unittest
from flask import Flask
from flask_testing import TestCase
from flask_login import login_manager

class TestCustomerRegister(TestCase):

    # Set up the test environment
    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'  # Use a test database
        app.config['TESTING'] = True
        app.config['SECRET_KEY'] = 'secretkey'  # Set a secret key for CSRF protection
        return app

    def setUp(self):
        # Create all tables in the test database
        with app.app_context():
            db.create_all()

    def tearDown(self):
        # Drop all tables after each test to ensure a clean state
        with app.app_context():
            db.drop_all()

    def test_customer_register(self):
        # Simulate form data
        form_data = {
            'name': 'Test User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'confirm': 'password123',
            'country': 'Test Country',
            'city': 'Test City',
            'contact': '1234567890',
            'address': 'Test Address',
            'zipcode': '12345',
            'profile': None  # Optional file field, can be skipped
        }
        
        # Create a CustomerRegisterForm instance with the form data
        form = CustomerRegisterForm(data=form_data)
        
        # Ensure the form is valid (this tests the validators)
        self.assertTrue(form.validate())
        
        # Simulate posting the form data
        with self.client:
            response = self.client.post('/customer/register', data=form_data, follow_redirects=True)
            
            # Check if the user is redirected to the login page after successful registration
            self.assertRedirects(response, '/customer/login')
            
            # Verify user is added to database
            user = Register.query.filter_by(username='testuser').first()
            self.assertEqual(user.name, 'Test User')
            self.assertEqual(user.email, 'testuser@example.com')
            self.assertEqual(user.username, 'testuser')

if __name__ == '__main__':
    unittest.main()

