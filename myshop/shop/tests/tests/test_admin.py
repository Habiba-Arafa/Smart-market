import unittest
from shop import app, db
from flask import session
from werkzeug.security import generate_password_hash
from shop.admin.models import User


class AdminAppTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the test client and initialize the database."""
        self.app = app.test_client()
        self.app.testing = True

        # Create the test database and tables
        with app.app_context():
            db.create_all()

            # Create a test user
            hashed_password = generate_password_hash('password')
            test_user = User(name='Test User', username='testuser', email='test@example.com', password=hashed_password)
            db.session.add(test_user)
            db.session.commit()

    def tearDown(self):
        """Clean up after each test."""
        with app.app_context():
            db.drop_all()

    def test_register_page(self):
        """Test if the register page renders correctly."""
        response = self.app.get('/register')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Register', response.data)

    def test_register_user(self):
        """Test user registration functionality."""
        response = self.app.post('/register', data={
            'name': 'New User',
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password',
            'confirm': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome New User, thanks for registering!', response.data)

    def test_login_page(self):
        """Test if the login page renders correctly."""
        response = self.app.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Login', response.data)

    def test_login_user(self):
        """Test user login functionality."""
        response = self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'password'
        }, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome back, test@example.com! You are now logged in.', response.data)
        self.assertIn('email', session)

    def test_admin_page_access(self):
        """Test admin page access when logged in."""
        # Log in the test user first
        self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'password'
        })
        response = self.app.get('/admin')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Admin Page', response.data)

    def test_admin_page_access_without_login(self):
        """Test admin page access without login (should redirect to login)."""
        response = self.app.get('/admin', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Please log in first.', response.data)

    def test_brands_page_access(self):
        """Test brands page access."""
        # Log in the test user first
        self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'password'
        })
        response = self.app.get('/brands')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Brands', response.data)

    def test_category_page_access(self):
        """Test category page access."""
        # Log in the test user first
        self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'password'
        })
        response = self.app.get('/category')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Categories', response.data)

    def test_logout(self):
        """Test logout functionality."""
        # Log in the test user first
        self.app.post('/login', data={
            'email': 'test@example.com',
            'password': 'password'
        })

        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('email', session)
        self.assertIn(b'Please log in first.', response.data)


if __name__ == '__main__':
    unittest.main()
