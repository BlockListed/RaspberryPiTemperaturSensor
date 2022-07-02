from decouple import config
import mariadb
import random
import idgen

debug = config("DEBUG", default=False, cast=bool)

if debug == False:
    from getdata import getData

db = mariadb.connect(
    host = config("MARIADB_HOST"),
    port = config("MARIADB_PORT", cast=int),
    user = config("MARIADB_USER"),
    password = config("MARIADB_PASSWORD"),
    db = config("MARIADB_DATABASE")
)

if __name__ == "__main__":
    # 0 is temp and 1 is humidity
    data = (0, 0)
    if debug:
        data = (random.randint(-10, 45), random.randint(0, 100))
    else:
        data = getData()
    
    c = db.cursor()
    stmt = '''INSERT INTO raspberrytemperature(id, pi, timestamp, temp, humidity)
    VALUES (%s, %s, %s, %s, %s);'''
    c.execute(stmt % (idgen.getId(), idgen.node, idgen.getTime(), data[0], data[1]))
    db.commit()

db.close()