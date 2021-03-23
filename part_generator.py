import random
import psycopg2
import os

from RandomWordGenerator import RandomWord

# Creating a random word object
rw = RandomWord(max_word_size = 5,
                constant_word_size=True,
                include_digits=False,
                special_chars=r"",
                include_special_chars=False)


##try:
con = psycopg2.connect(
host = "localhost",
dbname = "detectorover_db",
user = "rhyshorner",
password = os.environ['DB_PASSWORD'])
print("connected to detectorover_db.")

cursor = con.cursor()

for x in range(30):

    name = rw.generate()
    print("name done.")
    description = rw.generate()
    print("description done.")
    manufacturer = rw.generate()
    print("manufacturer done.")
    manufacturer_part_number = rw.generate()
    print("manufacturer_part_number done.")
    supplier = rw.generate()
    print("supplier done.")
    supplier_part_number = rw.generate()
    print("supplier_part_number done.")
    cost = round((random.random()*100),2)
    print("cost done.")

    cursor.execute("INSERT INTO public.detectorovers_parts_part(name, description, manufacturer, manufacturer_part_number, supplier, supplier_part_number, cost) VALUES (%s, %s, %s, %s, %s, %s, %s)", (name, description, manufacturer, manufacturer_part_number, supplier, supplier_part_number, cost))
    print("inserted data into table.")

    con.commit()
    print("connection commited.")

cursor.close()
con.close()

#except:
#    print("exception error")
#    cursor.close()
#    con.close()