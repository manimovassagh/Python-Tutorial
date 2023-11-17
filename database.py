import mysql.connector


# Establish a connection to the MySQL server
with mysql.connector.connect(
    host='localhost',
    user='myuser',
    password='mypassword',
    database='mydatabase'
) as connection:
    
    # Create a cursor object to interact with the database
    with connection.cursor() as cursor:
        # Create the students table
        cursor.execute("DROP TABLE IF EXISTS students")

        cursor.execute("""
           
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(50),
                age INT
            )
        """)

        # Insert some random data into the students table
        cursor.execute("INSERT INTO students (name, age) VALUES ('Alice', 20)")
        cursor.execute("INSERT INTO students (name, age) VALUES ('Bob', 22)")
        cursor.execute("INSERT INTO students (name, age) VALUES ('Charlie', 21)")

        # Commit the changes
        connection.commit()

        # Example: Execute a query to retrieve student data
        cursor.execute("SELECT * FROM students")

        # Fetch the results
        results = cursor.fetchall()
     
        # Display the results
        print("Student Data:")
        for row in results:
            print(row)
