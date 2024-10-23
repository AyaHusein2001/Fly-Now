# Flight Booking System

A responsive web-based application for booking flights, built with HTML, CSS, JavaScript (frontend), and Flask (backend). The system provides different features for visitors, customers, and admins, leveraging SQLAlchemy and SQLite for database management.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features

### Visitor:
- **Sign Up**: Create a new account.
- **Login**: Access the customer dashboard.
- **View Flights**: Browse available flights and search by arrival airport.
- **Search Flights**: Search by his destination .
- **Sort Flights**: Sort flights by date .


### Customer:
- **Book Flights**: Secure a reservation for a flight.
- **Sort Flights**: Sort flights by date .
- **View Reservations**: See all booked flights.
- **Cancel Reservations**: Remove a booking if necessary.
- **Search Reservations**: Find specific reservations by reservation number.

### Admin:
- **Manage Flights**: 
  - Sort flights by number .
  - Sort flights by date .
  - Add new flights.
  - Edit existing flight details.
  - Delete flights.
  - Add new Admins.

## Installation

### Prerequisites:
- [Python 3.x](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/)
- [SQLAlchemy](https://www.sqlalchemy.org/)

### Setup:

1. Clone this repository:
    ```bash
    git clone https://github.com/AyaHusein2001/epfl-final-project
    cd epfl-final-project
    ```

2. Install required Python packages:
    ```bash
    pip install flask sqlalchemy
    ```

3. Run the Flask application:
    ```bash
    flask run
    ```

4. Access the app by navigating to `http://127.0.0.1:5000` in your browser.

## Usage

1. **Visitors** can sign up or log in to book available flights.
2. **Customers** can book flights, view their reservations, cancel reservations, and search by reservation number.
3. **Admins** can manage the flight schedule by adding, editing, or deleting flights, adding new Admins.

## Screenshots
- **Sign Up**
![Sign Up](screenshots/image.png)
- **Login**
![login](screenshots/image-2.png)
- **Customer Home Page**
![Customer Home Page](screenshots/image-9.png)
- **Customer Reservations Page**
![Customer Reservations Page](screenshots/image-89.png)
- **Sign Up as Admin**
![Sign Up as Admin](screenshots/image-1.png)
- **Admin Home Page**
![Admin Home Page](screenshots/image-80.png)
- **Admin add flight**
![add flight](screenshots/image-3.png)
- **Admin edit flight**
![edit flight](screenshots/image-10.png)
- **Admin Add new Admin**
![add admin](screenshots/image-4.png)
- **Admin View Flight Reservations**
![Admin View Flight Reservations](screenshots/image-11.png)

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask (Python)
- **Database**: SQLite with SQLAlchemy ORM

## Contributing

Feel free to fork the repository, create a new branch, and submit a pull request for any improvements.