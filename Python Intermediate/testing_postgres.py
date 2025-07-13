import psycopg

# Connect to the database
with psycopg.connect("dbname=defaultdb " \
"user=<user>  " \
"password=<password> " \
"host=<hostname> " \
"port=25060") as conn:
    # Create a server-side cursor
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM <table_name>;")
        results = cursor.fetchall()
        for row in results:
            print(row)

            