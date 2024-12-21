from shop import app, db
from shop.products.models import Addproduct, Category, Brand
from datetime import datetime
import sys

if __name__ == "__main__":
    with app.app_context():
        try:
            db.create_all()
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

    # Bind to 0.0.0.0 for external access
    app.run(debug=True, host="0.0.0.0", port=5000)
