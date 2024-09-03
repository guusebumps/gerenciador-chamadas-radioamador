# Amateur Radio Call Manager

I did this project at the request of my college professor Virgilio Cesar Leandro, who is an amateur radio operator. He asked me for this software to store his calls in a database and to be able to print them in Excel. The program has a graphical interface and connects to the SQLite database, where it creates a table with the columns necessary to store the data. In this program, it is possible to insert, edit and delete rows from the table through the interface, in addition to being able to generate an Excel file of the table.

This Python project is a desktop application for registering, modifying, and managing call data using PyQt5 for the user interface and SQLite for the database. The application also allows exporting data to an Excel file.

## Features

- **Add Call Data:** Users can input various details related to a call, such as date, time, frequency, and additional notes.
- **Edit Call Data:** Modify existing call entries.
- **Delete Call Data:** Remove unwanted call entries from the database.
- **Export to Excel:** Export all call data to an Excel file for external use or backup.
- **Real-Time Data Update:** The application displays data in a table format and updates in real-time as data is modified.

## Dependencies

The application relies on the following Python libraries:

- **PyQt5:** Used for creating the graphical user interface.
- **SQLite3:** A lightweight database for storing call data.
- **Pandas:** Utilized for handling data and exporting it to Excel.
- **OpenPyXL:** Used for reading and writing Excel files.
- **XLWT:** Used for generating Excel files.

## Installation

To run this application, ensure you have Python installed and then install the necessary libraries using pip:

```bash
pip install PyQt5 pandas openpyxl xlwt mysql-connector-python
```

# Call Registration System

This Python project is a desktop application for registering, modifying, and managing call data using PyQt5 for the user interface and SQLite for the database. The application also allows exporting data to an Excel file.

## Features

- **Add Call Data:** Users can input various details related to a call, such as date, time, frequency, and additional notes.
- **Edit Call Data:** Modify existing call entries.
- **Delete Call Data:** Remove unwanted call entries from the database.
- **Export to Excel:** Export all call data to an Excel file for external use or backup.
- **Real-Time Data Update:** The application displays data in a table format and updates in real-time as data is modified.

## Dependencies

The application relies on the following Python libraries:

- **PyQt5:** Used for creating the graphical user interface.
- **SQLite3:** A lightweight database for storing call data.
- **Pandas:** Utilized for handling data and exporting it to Excel.
- **OpenPyXL:** Used for reading and writing Excel files.
- **XLWT:** Used for generating Excel files.

## Installation

To run this application, ensure you have Python installed and then install the necessary libraries using pip:

```bash
pip install PyQt5 pandas openpyxl xlwt mysql-connector-python
```

# Database Setup
The application uses SQLite to store call data. On the first run, it will automatically create a database file named banco_cadastro.db and a table cadastro_chamadas if they do not exist.

# User Interface
The application consists of multiple windows created with PyQt5:

* Main Window: Allows navigation between adding, modifying, deleting, and exporting data.
* Add Data Window: Form to input new call data.
* Edit Data Window: Interface for modifying existing data.
* Delete Data Window: Interface for deleting data entries.
  
# Usage
1. Starting the Application: Run the script, and the main window will appear.
2. Adding Data: Click on the "Insert" button to open the Add Data Window. Fill in the fields and click "Submit" to add the data to the database.
3. Modifying Data: Click on the "Edit" button to open the Edit Data Window. Select the data to edit, make changes, and save.
4. Deleting Data: Click on the "Delete" button to open the Delete Data Window. Enter the ID of the entry to delete and confirm the deletion.
5. Exporting Data: Click on the "Export to Excel" button to export all entries to an Excel file named chamadas_cadastradas.xls.

# Code Overview

* Database Connection and Table Creation: The database is connected to using sqlite3, and the table cadastro_chamadas is created if it does not exist.
* Data Operations
  * Inserting Data: Data is collected from user input fields and inserted into the database.
  * Deleting Data: The specified entry is removed based on its ID.
  * Updating Data: Updates the table view with the latest data from the database.
  * Exporting to Excel: Retrieves all data from the database and exports it to an Excel file using pandas.
* UI Functions: Functions are provided to show/hide different windows and handle button clicks for inserting, editing, and deleting data.

# Error Handling

The code contains basic error handling for database operations and file generation. Future improvements could include more robust exception handling and user feedback.

# Future Improvements

* User Authentication: Add user login functionality to protect data.
* Enhanced Validation: Implement more comprehensive input validation and error handling.
* Graphical Enhancements: Improve the UI with better design and user feedback.
* Data Analysis: Incorporate data analysis tools to provide insights based on the call data.

  # Screenshots

![image](https://user-images.githubusercontent.com/113928099/228587507-17bb354d-e412-49f4-812c-dd4de65f9b79.png)
![image](https://user-images.githubusercontent.com/113928099/228587599-5790fa37-e634-43b4-9731-7a41c96b9417.png)
![image](https://user-images.githubusercontent.com/113928099/228587941-b570c1ff-aeab-4593-846f-9f12041605b1.png)
