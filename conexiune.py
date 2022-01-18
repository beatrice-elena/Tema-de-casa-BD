import cx_Oracle

conn = cx_Oracle.connect('bd154/Beatrice_12@//bd-dc.cs.tuiasi.ro:1539/orcl')
print(conn.version)
c = conn.cursor()