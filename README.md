## Project Overview
The Online Smart Market project is designed to provide users with a seamless shopping experience. It includes features like browsing products, smart recommendations, adding items to a cart, and secure checkout. Targeted at online shoppers, this project aims to streamline the online purchasing process and enhance user experience through  a user-friendly design.

## Team Information
- **Abdelrahman Elsayed ** (abdulrahman.hassan@zewailcity.edu.eg-202202049)
- **Abdelaziz ElHelaly ** (s-abdelaziz.eleisawy@zewailcity.edu.eg-202202132) 
- **Ezz Eldeen Ahmed Mohamed** (s-ezz.abdelmotalb@zewailcity.edu.eg-202202132)
- **Nourhan Deif  ** (s-nourhan.sayed@zewailcity.edu.eg-202201959)
- **Habiba Arafa  ** (s-habiba.arafa@zewailcity.edu.eg-202201684) 

# Smart Market

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)

## Table of Contents

1. [Description](#description)
2. [Features](#features)
3. [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
4. [Usage](#usage)
5. [License](#license)

---

## Description

**Smart Market** is a web application designed to streamline the operations of an online tech store. It offers users an intuitive interface to browse, select, and purchase tech products, while providing administrators with efficient tools to manage inventory and orders.

## Features

- **User Authentication:** Secure registration and login for users and admins.
- **Product Browsing:** View detailed descriptions and images of tech products.
- **Shopping Cart:** Add, update, and remove products before purchase.
- **Order Management:** Track and manage user orders.
- **Inventory Management:** Admins can add, edit, or delete products.
- **Responsive Design:** Optimized for desktops, tablets, and mobile devices.

## Getting Started

Follow these instructions to set up and run **Smart Market** on your local machine.

### Prerequisites

Ensure you have the following installed:

- **[Python](https://www.python.org/)** v3.8 or higher
- **[Flask](https://flask.palletsprojects.com/)**
- **[SQLite](https://www.sqlite.org/index.html)**
- **[Git](https://git-scm.com/)**
- **[Virtualenv](https://virtualenv.pypa.io/en/latest/)** (optional but recommended)

### Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/nour-awad/smart-market.git
    ```

2. **Navigate to the project directory**

    ```bash
    cd smart-market
    ```

3. **Create a virtual environment (optional but recommended)**

    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**

    - **On macOS and Linux:**

        ```bash
        source venv/bin/activate
        ```

    - **On Windows:**

        ```bash
        venv\Scripts\activate
        ```

5. **Install the required dependencies**

    ```bash
    pip install -r requirements.txt
    ```

6. **Set up the SQLite database**

    - **Initialize the database:**

        ```bash
        flask db init
        flask db migrate -m "Initial migration."
        flask db upgrade
        ```

    - **Alternatively, use the provided SQL script:**

        ```bash
        sqlite3 smart_market.db < schema.sql
        ```

7. **Configure environment variables**

    - Create a `.env` file in the root directory and add:

        ```env
        FLASK_APP=app.py
        FLASK_ENV=development
        SECRET_KEY=your_secret_key
        SQLALCHEMY_DATABASE_URI=sqlite:///smart_market.db
        ```

8. **Run the application**

    ```bash
    flask run
    ```

9. **Access the application**

    Open your browser and navigate to `http://localhost:5000`

## Usage

After installation, use **Smart Market** to manage and purchase tech products.

### Running the Application

1. **Start the Flask server**

    ```bash
    flask run
    ```

2. **Access the application**

    Open your browser and go to `http://localhost:5000`


License
This project is licensed under the MIT License.
