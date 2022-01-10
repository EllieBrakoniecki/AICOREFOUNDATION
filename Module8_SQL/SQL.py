#%%
import psycopg2
from psycopg2 import OperationalError   

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection to PostgreSQL DB successful")
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection(
    "Pagila", "postgres", "halopancake6", "127.0.0.1", "5432"
)
# %%
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        
# %%
select_actors = "SELECT * from actor"
actors = execute_read_query(connection, select_actors)

for actor in actors:
    print(actor)
    
#%%
select_names = "SELECT first_name,last_name FROM actor"
names = execute_read_query(connection, select_names)
for name in names:
    print(name)
#%%
actors_in_film_2 = "SELECT first_name, last_name FROM actor JOIN( SELECT * FROM film_actor WHERE film_id = 2) sub ON actor.actor_id = sub.actor_id"
actors = execute_read_query(connection, actors_in_film_2)
for actor in actors:
    print(actor)
#%%
import sqlalchemy
import pandas as pd
DATABASE_TYPE = 'postgresql'
DBAPI = 'psycopg2'
HOST = 'localhost'
USER = 'postgres'
PASSWORD = 'halopancake6'
DATABASE = 'Pagila'
PORT = 5432
engine = sqlalchemy.create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")


#%%
engine.execute('''SELECT * FROM actor''').fetchall()
actors = pd.read_sql_table('actor', engine)
actors.head(10)
actors = pd.read_sql_query('''SELECT * FROM actor LIMIT 10''', engine).set_index('actor_id')
actors
#%%
from sklearn.datasets import load_iris
data = load_iris()
iris = pd.DataFrame(data['data'], columns=data['feature_names'])
iris.head()
iris.to_sql('iris_dataset', engine, if_exists='replace')
iris.to_sql()






# %%
# 1. SELECT : Specifies which columns we want.
# 2. FROM: Specifies from which tables
# 3. WHERE: Filters the rows out of our result set based on some condition.
# 4. GROUP BY: Collecting information using aggregates(Summary stats) on categorical data.
# 5. HAVING: Like WHERE but used to filter the data after the grouping stage.
# 6. ORDER BY: Specifies the order in which we want our result set.
# 7. LIMIT: Limits the number of data we have.





#%%

# CREATE SCHEMA sales;
# SET search_path TO sales, public
# CREATE TABLE staff(
#     staff_id SERIAL PRIMARY KEY,
#     first_name VARCHAR(45) NOT NULL,
#     last_name VARCHAR(45) NOT NULL,
#     email VARCHAR(100) NOT NULL UNIQUE
# );
# Ovidiu Popa to Everyone (20:48)
# -- Create a table named employee_details with the following values

# -- CREATE TABLE lesson3schema.employee_details (
# -- employee_id INT PRIMARY KEY,
# -- employee_name VARCHAR(20) NOT NULL
# -- )

# -- INSERT INTO lesson3schema.employee_details (employee_id, employee_name)
# -- VALUES (1, 'Mr. Pink'), (2, 'Mr. Blonde'), (3, 'Mr. Orange'), (4, 'Mr. White'), (5, 'Mr. Brown'), (6, 'Eddie'), (7, 'Joe')

# -- CREATE TABLE lesson3schema.employee_salary AS (
# -- 	SELECT * FROM lesson3schema.employee_details
# -- )

# -- ALTER TABLE lesson3schema.employee_salary
# -- 	ADD COLUMN salary INT
# -- some tedious lines



# -- SELECT * FROM lesson3schema.employee_salary



# SELECT address
# FROM address
# JOIN store
# ON address.address_id = store.address_id;
# SELECT first_name, last_name, address, district, postal_code
# FROM staff
# JOIN address
# ON staff.address_id = address.address_id;
# SELECT first_name, last_name, address, district, city
# FROM customer
# JOIN address
# ON customer.address_id = address.address_id
# JOIN city
# ON city.city_id = address.city_id
# JOIN rental
# ON customer.customer_id = rental.customer_id;
# SELECT first_name, last_name, address, district, city, rental_date
# FROM customer
# JOIN address
# ON customer.address_id = address.address_id
# JOIN city
# ON city.city_id = address.city_id
# JOIN rental
# ON customer.customer_id = rental.customer_id
# WHERE rental.rental_date BETWEEN '2005-05-26 00:00:00' AND '2005-05-30 00:00:00'
# ORDER BY last_name LIMIT 25;
# 21:22
# -- CREATE TABLE lesson4schema.customer (
# -- 	customerID INT PRIMARY KEY,
# -- 	customerNAME TEXT NOT NULL);
# -- INSERT INTO lesson4schema.customer
# -- VALUES (1, 'Homer'),  (2, 'Marge'), (3, 'Bart'), (4, 'Lisa'), (5, 'Maggie'), (6, 'Moe');
# -- CREATE TABLE lesson4schema.order (
# -- 	orderID INT PRIMARY KEY,
# -- 	customerID INT NOT NULL,
# -- 	item TEXT NOT NULL);
	
# -- INSERT INTO lesson4schema.order
# -- VALUES (1, 1, 'Beer'), (2, 2, 'Hair Product'), (3, 2, 'Dress'), (4, 3, 'Juice'), (5, 3, 'Magazine'), (6, 6, 'Peanuts');
# SELECT c.customerID, c.customerName, o.item
# FROM lesson4schema.customer AS c
# INNER JOIN lesson4schema.order AS o
# ON c.customerID = o.customerID;
# SELECT c.customerID, c.customerName, o.item
# FROM lesson4schema.customer AS c
# LEFT JOIN lesson4schema.order AS o
# ON c.customerID = o.customerID;

















