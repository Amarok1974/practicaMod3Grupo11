import psycopg2
#1.- Hacer la conexión a la base de datos
conexion = psycopg2.connect(
    host = "localhost",
    port = "5432",
    database = "credenciales",
    user = "Admin",
    password = "p4ssw0rdDB"
)

#2.- Crear el cursor
cursor = conexion.cursor()

#3.- Ejecutar la cnsulta
cursor.execute("SELECT * FROM usuarios")
registros = cursor.fetchall()



#4.-Mostrar los resultados
for fila in registros:
    print(fila) 

#5 cerrar las conexiones
cursor.close()
conexion.close()

