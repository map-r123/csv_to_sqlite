# CSV to SQLite Importer

A simple Python script that reads data from a `.csv` file and stores it into a SQLite database (`data.db`).

## 📌 Features

* Reads CSV files with `;` (semicolon) delimiter
* Automatically creates a SQLite table based on CSV headers
* Inserts all rows into the database
* Handles UTF-8 encoded files (including BOM)

---

## 📂 Project Structure

```
.
├── script.py        # Main Python script
├── data.db          # SQLite database (created automatically)
└── README.md        # Project documentation
```

---

## ⚙️ Requirements

* Python 3.9+
* No external libraries required (uses built-in modules only):

  * `csv`
  * `sqlite3`
  * `pathlib`

---

## 🚀 How to Use

1. Place your `.csv` file in the same directory as the script.

2. Run the script:

```
python script.py
```

3. Enter the CSV file name when prompted:

```
Enter CSV Name: example.csv
```

4. The script will:

   * Read the file
   * Create a SQLite database (`data.db`)
   * Create a table named `Data`
   * Insert all CSV rows into the table

---

## 🧾 CSV Format Requirements

* Must use **semicolon (`;`)** as a delimiter
* First row must contain column headers

Example:

```
Name;Age;City
Alice;25;London
Bob;30;Paris
```

---

## 🗄️ Database Details

* Database file: `data.db`
* Table name: `Data`
* All columns are stored as `TEXT`
* Column names are derived from CSV headers:

  * Spaces are replaced with underscores (`_`)

---

## ⚠️ Notes

* If the file is not found, the script will prompt again
* Duplicate or conflicting inserts may be ignored
* Large CSV files may take longer due to row-by-row insertion

---

## 🔧 Possible Improvements

* Automatic data type detection (INTEGER, REAL, etc.)
* Support for different delimiters
* Bulk insert optimization (`executemany`)
* Command-line arguments instead of input prompt
* Better error handling and logging

---

## 📄 License

This project is open-source and free to use.
