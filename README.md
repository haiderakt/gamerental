# gamerental
A simple and intuitive game rental system for shops that uses mysql as the database

Go to your mysql and paste this:

CREATE DATABASE IF NOT EXISTS gamrentaldb;
USE gamrentaldb;

CREATE TABLE customers (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(20)
);

CREATE TABLE games (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(100) NOT NULL,
    genre VARCHAR(50),
    price_per_day DECIMAL(10,2) NOT NULL,
    available_copies INT NOT NULL
);

CREATE TABLE staff (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    position VARCHAR(50) NOT NULL
);

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
