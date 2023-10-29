import json
import psycopg2

# Database connection parameters
db_params = {
    "host": "your_database_host",
    "database": "your_database_name",
    "user": "your_database_user",
    "password": "your_password",
}

# Path to your JSON file
json_file_path = "your_json_file.json"

try:
    # Connect to the database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Open and parse the JSON file
    with open(json_file_path, "r") as file:
        data = json.load(file)

    # Define your SQL table creation and insertion statements
    table_name = "your_table_name"
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS {} (
        column1_type data_type,
        column2_type data_type,
        -- Add more columns here
    );
    """.format(table_name)

    insert_data_sql = """
    INSERT INTO {} (column1, column2, ...)
    VALUES (%s, %s, ...);
    """.format(table_name)

    # Create the table
    cursor.execute(create_table_sql)
    conn.commit()

    # Insert data into the table
    for record in data:
        values = (
            record['column1'],
            record['column2'],
            # Add more columns' values here
        )
        cursor.execute(insert_data_sql, values)
        conn.commit()

    print("Data has been successfully inserted into the PostgreSQL table.")
except Exception as e:
    print("Error:", e)
finally:
    cursor.close()
    conn.close()
