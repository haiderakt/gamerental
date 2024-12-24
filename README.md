GameRental System
A simple and intuitive game rental system designed for shops, leveraging MySQL as the database. This system allows users to manage customer information, game inventory, staff details, and rental transactions efficiently.

Features
Customer Management: Store and manage customer details like name, email, and phone.
Game Inventory: Track games, their genres, prices, and available copies.
Staff Management: Manage staff details, including their roles and contact information.
Rental System: Record rental transactions, including rental dates, return dates, and associated costs.
Database Setup
Follow these steps to set up the database and tables for the GameRental system.

Create the Database:

First, create the gamrentaldb database (if it doesn’t already exist) and use it:

CREATE DATABASE IF NOT EXISTS gamrentaldb;
USE gamrentaldb;
Create Tables:

After creating and using the database, execute the following SQL statements to create the required tables:

Customers Table:
Stores customer information, including their name, email, and phone number.

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20)
);
Games Table:
Stores details about the games available for rent, including their title, genre, price per day, and available copies.

CREATE TABLE games (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    price_per_day DECIMAL(10,2) NOT NULL,
    available_copies INT NOT NULL
);
Staff Table:
Stores information about staff members, including their name, email, and position in the shop.

CREATE TABLE staff (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    position VARCHAR(50) NOT NULL
);
Rentals Table:
Tracks rental transactions, linking customers, games, and staff. It also stores rental and return dates, as well as the total cost.

CREATE TABLE rentals (
    id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    game_id INT,
    staff_id INT,
    rental_date DATE NOT NULL,
    return_date DATE,
    total_cost DECIMAL(10,2),
    FOREIGN KEY (customer_id) REFERENCES customers(id),
    FOREIGN KEY (game_id) REFERENCES games(id),
    FOREIGN KEY (staff_id) REFERENCES staff(id)
);


Requirements
MySQL 5.7 or higher
Basic knowledge of SQL and MySQL database management
A MySQL client or database management tool (e.g., phpMyAdmin, MySQL Workbench)
Usage
Once the database and tables are set up, you can start using the system to:

Add customers and games
Record rental transactions and track returns
Manage staff and their roles
