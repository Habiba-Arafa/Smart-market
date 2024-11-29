# from flask import Flask, render_template, request, redirect, url_for
# from db_classes import CustomerDatabase

# app = Flask(__name__)

# # Database instance
# customer_db = CustomerDatabase()

# @app.route('/profile/4', methods=['GET', 'POST'])
# def profile():
#     customer_info = customer_db.get_customer_info(4)
    
#     if not customer_info:
#         return "User not found", 404
    
#     if request.method == 'POST':
#         new_username = request.form.get('name')
#         new_email = request.form.get('email')
        
#         customer_db.update_customer_info(4, username=new_username, email=new_email)
        
#         return redirect(url_for('profile', user_id=4)) 

#     return render_template('profile_customer.html', customer_info=customer_info)

# if __name__ == '__main__':
#     app.run(debug=True)
