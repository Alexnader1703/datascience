import os
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from connect_db import WorkPDB

mydb=WorkPDB(port=5432,user="postgres",host="localhost",password="3021")

print(mydb.PrintInfoDB())