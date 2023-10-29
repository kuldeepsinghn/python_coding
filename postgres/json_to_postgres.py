import psycopg2
import json


hostname = 'localhost'
database = 'workdb'
username = 'postgres'
password = 'new_password'
port = 5432


json_file_path = 'D:\git_hub\python_\python_coding\making_request_to_github_api/2023-10-27,21-46-03.json'


conn = psycopg2.connect(
    host=hostname,
    database=database,
    user=username,
    password=password,
    port=port
)


cursor = conn.cursor()


with open(json_file_path, 'r') as file:
    data = json.load(file)


table_name = 'practice_tab'
columns = list(data[0].keys())


table_name = table_name[:63]
table_name = ''.join(c for c in table_name if c.isalnum())


create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join([f'{col} TEXT' for col in columns])})"
cursor.execute(create_table_sql)
conn.commit()


for record in data:
    insert_data_sql = f"INSERT INTO {table_name} ({', '.join(columns)}) VALUES ({', '.join(['%s' for _ in columns])})"
    values = [(record[col]) for col in columns]
    cursor.execute(insert_data_sql, values)
    conn.commit()

print(f"Table '{table_name}' has been created and populated with data from the JSON file.")


if 'cursor' in locals():
    cursor.close()
if 'conn' in locals():
    conn.close()
