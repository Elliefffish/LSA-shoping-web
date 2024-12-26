import sqlite3
import subprocess
from package_table import create_db

def insert_status():
  conn = sqlite3.connect('shopping.db')
  c = conn.cursor()
  package_data = [
    ("Delivered", "Classroom 228", "2023-05-14 10:15"),
    ("Out for Delivery", "Local Courier, Puli", "2023-05-14 08:30"),
    ("In Transit", "Distribution Center, Puli", "2023-05-13 20:00"),
    ("Processing", "LSA Shop", " ")
  ]
  c.execute("DELETE from Status")
  for status, place, time in package_data:
    c.execute("INSERT INTO Status (status, place) VALUES (?, ?)", (status, place))
  subprocess.run(['sqlite3','shopping.db',
               '-cmd','.mode csv','.import goods.csv Goods'],capture_output=True)
  conn.commit()
  conn.close()

create_db()
insert_status()
