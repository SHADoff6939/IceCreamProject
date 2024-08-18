# ICE CREAM PROJECT
#### Video Demo:  https://youtu.be/I-Ea-p-HnnU
#### Description: Ice Cream Sales Tracker is a console application designed to manage ice cream sales. It allows users to add items to a cart, purchase them, and track the total sales. The application uses an SQLite database to store information about items and the number of units sold.

#### Key Features
#### Adding Items to the Cart:

#### Users can add various types of ice cream to the cart by selecting options from the menu.
#### Viewing Cart Contents:

#### Displays all items currently in the cart, with options to remove specific items or clear the entire cart.
#### Making a Purchase:

#### After confirming the purchase, sales information is updated in the database.
#### Viewing Total Cash Amount:

#### Users can check the total amount of money earned from sales.
#### Resetting the Number of Items Sold:

#### An administrator can reset the number of sold items to zero.
#### Safe Exit from the Application:

#### The application supports safe exit with user confirmation.
#### Project Files
#### main.py:

#### The main project file containing all the code for the console application. It implements all the database interactions, user interface, error handling, and core logic.
#### data.db:

#### SQLite database used to store information about items and the number of units sold. This database consists of a single table, sales, which contains three fields: item (item name), price (item price), and saled (number of units sold).
#### data.db-shm, data.db-wal:

#### Accompanying database files that support the Write-Ahead Logging (WAL) journal mode for enhanced performance and database resilience.
#### Logic and Design
#### Data Structure
#### The sales table in the database stores information about each item, including its name, price, and the number of units sold. This allows for tracking sales volume and easily updating item information.
#### Core Logic
#### Database Initialization:

#### Upon launching the application, it checks for the existence of the sales table and creates it if it doesn't exist. The application also verifies whether items have already been added to the table, and if not, it inserts them.
#### User Command Handling:

#### Users can select options from the menu to add items to the cart, view the cash amount, purchase items, or reset sales numbers. All commands are handled within a while loop, allowing the application to run continuously until the user decides to exit.
#### Database Interaction:

#### The application uses SQLite to store and update information about items and sales. All changes are committed to the database, ensuring data persistence even after the application is closed.
#### Error Handling
#### The application handles various types of errors, including database errors (e.g., when the database is locked), invalid user input, and unexpected interruptions (e.g., via KeyboardInterrupt).
#### Design Decisions
#### WAL Mode:
#### WAL (Write-Ahead Logging) is enabled to improve performance and provide greater reliability during concurrent database operations.
#### Simple Console Interface:
#### The interface is designed for easy user interaction with the application, requiring no complex menus or settings. This ensures quick and convenient usage.
#### Conclusion
#### Ice Cream Sales Tracker is an efficient tool for tracking ice cream sales. With its ease of use and reliable SQLite database, this application is an ideal solution for small shops or kiosks looking to manage their sales and monitor their profits. This project demonstrates how even a simple console application can be a powerful tool for business.
