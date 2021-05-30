
import sqlite3
import Tools
Name = Tools.readSettings()["Database_Name"]

# Execute
def db_exec(query):
    con = sqlite3.connect(Name)
    cur = con.cursor()

    cur.execute(query)
    con.commit()
    con.close()

# Fetch
def db_fetch(query):
    con = sqlite3.connect(Name)
    cur = con.cursor()

    cur.execute(query)
    tmp = cur.fetchall()

    con.commit()
    con.close()
    return tmp

# Build the Database
def db_build():
    db_exec("""Create Table IF NOT EXISTS Passwords(
                ID integer not null PRIMARY KEY,
                Name text,
                Email text,
                Username text,
                Password text)""")

# Drop the Database
def db_drop():
    db_exec("""Drop Table Passwords""")

# Get All
def db_getAll():
    return db_fetch("""select * from Passwords""")

# Get by ID
def db_getByID(id):
    return db_fetch("select * from Passwords where ID = '{}'".format(id))

# Get by
def db_getBy(key,value):
    return db_fetch("select * from Passwords where {} like '%{}%'".format(key,value))

# Inserting
def db_insert(name,email,username,password):
    db_exec("insert into Passwords(Name,Email,Username,Password) values ('{}','{}','{}','{}')".format(name,email,username,password))

# Updating
def db_update(id,key,value):
    db_exec("update Passwords set {} = '{}' where id = {}".format(key,value,id))

# Removing
def db_remove(id):
    db_exec("Delete from Passwords where id = {}".format(id))

