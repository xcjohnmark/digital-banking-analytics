import psycopg2

DATABASE = "digital_banking_analytics"
USER = "postgres"
PASSWORD = "os.getenv('DB_PASSWORD')"
HOST = "127.0.0.1"
PORT = 5432

try:
    connection = psycopg2.connect(
        dbname = DATABASE,
        user = USER,
        password = PASSWORD,
        host = HOST,
        port = PORT
    )
    print("Database connection Successful!")

    cursor = connection.cursor()
    sql_file_createtables = "sql/create_tables.sql"
    with open(sql_file_createtables, "r") as file:
        sql_script = file.read()

    cursor.execute(sql_script)

    connection.commit()
    print("SQL Script executed and committed successfully!")

    list_of_mappings = [
        ("data/users.csv", "users"),
        ("data/accounts.csv", "accounts"),
        ("data/transactions.csv", "transactions"),
        ("data/events.csv", "events"),
        ("data/sessions.csv", "sessions")
    ]

    for csv_path, table_name in list_of_mappings:
        with open(csv_path, "r") as file:
            copy_query = f"COPY {table_name} FROM STDIN WITH CSV HEADER"
            cursor.copy_expert(copy_query, file)
            print(f"Data successfully loaded into {table_name}!")
    connection.commit()
    


    cursor.close()
    connection.close()
    print("Connection closed cleanly")

except Exception as error:
    print(f"Error: Unable to connect to the database. Reason: {error}")