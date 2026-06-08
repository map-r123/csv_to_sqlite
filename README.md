# CSV to SQLite Importer

A simple Python script that reads data from a `.csv` file and stores it into a SQLite database (`data.db`).

## 📌 Features

* Reads CSV files
* Autonatically detects the delimiter used
* Automatically creates a SQLite table based on CSV headers
* Automatically detects is data is INTERGER, REAL or TEXT
* Inserts all rows into the database
* Handles UTF-8 encoded files

---

## 📂 Project Structure

```
.
├── etl.py        # Main Python script
├── data.db          # SQLite database (created automatically)
└── README.md        # Project documentation
```

---

## ⚙️ Requirements

* Python 3.9+
* External libraries required:
  * `detect_delimiter`
* Built-in modules used:
  * `sqlite3`
  * `pathlib`
  * `csv`

---

## 🚀 How to Use

1. Place your `.csv` file in the same directory as the script or have the path to the `.csv` file

2. Run the script:

```
python etl.py
```

3. Enter the CSV file name or path when prompted:

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
* Column names are based from CSV headers:

  * Spaces are replaced with underscores (`_`)

---

## ⚠️ Notes

* If the file is not found, the script will raise a file not found error
* If file does not end in `.csv`, the script will keep asking for the file name
* Duplicate or conflicting inserts may be ignored
* If delimiter is not found an error will be rasised

---

## 🔧 Possible Improvements

* Command-line arguments instead of input prompt
* Better error handling and logging

---

## 📄 License

This project is open-source and free to use.
