import mysql.connector
import models


def create_conection(host_name, user_name, user_password, db_name):
    conection = None
    try:
        conection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = user_password,
            database = db_name
        )
        print("Conection to MySQL DB successful")
    except mysql.connector.Error as err:
        print(f"The error '{err}' ocurred")
    return conection


def create_database(conection, query):
    cursor = conection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except mysql.connector.Error as err:
        print(f"The error '{err}' ocurred")

# create_database_query = "CREATE DATABASE animals_app"
# create_database(conection, create_database_query)

def execute_query(conection, query):
    cursor = conection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except mysql.connector.Error as err:
        print(f"The error '{err}' ocurred")

create_animals_table = """
CREATE TABLE IF NOT EXISTS animals (
    id INT AUTO_INCREMENT,
    name TEXT NOT NULL,
    age INT,
    kind TEXT,
    commands TEXT,
    PRIMARY KEY (id)
) ENGINE = InnoDB
"""
# execute_query(conection, create_animals_table)

# dog = models.DomesticAnimals("Rex", 3, "Dog")
# dog.add_command("Sit")
# dog.add_command("Bring")
# dog.add_command("Jump")

def add_animal(conection, animal):
    sql = """
    INSERT INTO
    animals (name, age, kind, commands)
    VALUES
    (%s, %s, %s, %s)
    """
    values = (animal.name, animal.age, animal.kind, ", ".join(animal.command))
    cursor = conection.cursor()
    cursor.execute(sql, values)
    conection.commit()
    print("Животное успешно добавлено в базу данных питомника.")

def read_query(conection, query):
    cursor = conection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except mysql.connector.Error as err:
        print(f"The error '{err}' ocurred")
