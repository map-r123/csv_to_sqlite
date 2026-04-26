import csv
import sqlite3
from pathlib import Path

def read_file(file_name):
    output = []
    count = 0
    try:
        with open(file_name, newline="", encoding="UTF-8-sig") as file:
            reader = csv.DictReader(file, delimiter=";")

            for row in reader:
                output += [row]
                count += 1

        return output, reader.fieldnames

    except FileNotFoundError:
        print(file_name, "was not found")


def create_db(fieldnames):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    table = get_column_names(fieldnames)

    try:
        cursor.execute(f"CREATE TABLE IF NOT EXISTS Data ({table});")
        print("Database created")
    except sqlite3.Error as error:
        print("create_db error:", error)
        pass

    cursor.close()
    conn.close()


def get_column_names(fieldnames):
    table = ""
    for column in fieldnames:
        table += f'{column.replace(" ","_")} TEXT,'
    return table.removesuffix(",")


# Function to write the data from the csv to the a sqlite database
def write(data, fieldnames):

    with sqlite3.connect("data.db") as conn:
        cursor = conn.cursor()
        columns = ""

        # creates the string for columns and cleans it up
        for column in fieldnames:
            columns += f'"{column.replace(" ","_")}",'
        columns = columns.removesuffix(",")

        placeholders = ",".join(["?"] * len(fieldnames))
        placeholders = placeholders.removesuffix(",")

        for row in data:
            # list with all the data that should be insert into the database
            values = []
            for col in fieldnames:
                values.append(row[col])

            try:
                cursor.execute(
                    f"INSERT INTO data ({columns})" f"VALUES ({placeholders}) ",
                    (values),
                )
            except sqlite3.IntegrityError:
                pass
        print("Table created")
        conn.commit()
        cursor.close()


def main():
    file_name = input("Enter CSV Name: ")

    while Path(file_name).suffix.lower() != ".csv":
        print("File not Found")
        file_name = input("Enter CSV Name: ")

    data, fieldnames = read_file(file_name)
    create_db(fieldnames)
    write(data, fieldnames)


if __name__ == "__main__":
    main()
