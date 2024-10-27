# Nombre: brute.py
# Asignatura: Seguridad en Redes - Curso 2024/2025.
# Descripcion: Script de fuerza bruta sobre un fichero PDF protegido con PGP
#              en el que varios hilos usan el diccionario (literalmente) para
#              generar las posibles contraseñas.
# Tiempo estimado para la solucion: 4 horas aprox.

#PAQUETES
import threading
import gnupg
import itertools
import signal

#VARIABLES
password_combination_length= 5  #Acotamos el largo de la contraseña por si no se encontrara la clave. Combinaciones de 5 letras máximo. Se puede modificar
gpg = gnupg.GPG()               #Objeto creado para interactuar con el fichero cifrado.


num_threads=50                  #Numero de hilos empleados para realizar pruebas. Se puede modificar. Por defecto, 50.
match = False                   #Variable creada para detener todos los hilos una vez se encuentre la solucion



pool = ['a', 'b', 'c', 'd', 'e', 'f', 'g', #Diccionario usado para generar las claves
        'h', 'i', 'j', 'k', 'l', 'm', 'n', 
        'o', 'p', 'q', 'r', 's', 't', 'u', 
        'v', 'w', 'x', 'y', 'z']

test_password = (                                                                   #Iterador para generar todas las posibles combinaciones
    ''.join(i) 
    for password_combination_length in range(1, password_combination_length + 1)    #Para contraseñas que van desde longitud 1 a 5.
    for i in itertools.product(pool, repeat=password_combination_length)            #Genero todas las combinaciones posibles de los caracteres.
)


#Funcion Generator: Lógica principal del programa. Toma una contraseña generada (Primera parte), intenta desencriptar el fichero mostrando por pantalla
#                   la contraseña empleada y si ha funcionado (Bloque intermedio). Cuando encuentra la contraseña, pone match a true para que todos los hilos paren.
def password_generator():
    global match
    for password in test_password:
        if match:                                   #Compruebo la variable match para ver si ya está encontrada o parado el programa, para no abrir el fichero.
            break
        with open('archive.pdf.gpg', 'rb') as file: #Si puedo desencriptar el fichero, pongo match a true.
            if match:
                break

            result = gpg.decrypt(file.read(), passphrase=password)  #Intenta desencriptar el fichero con la contraseña proporcionada.
            print(f'Test case: {password} | Status: [{result.ok}]') #Log de la prueba

            
            if result.ok:                                           #Al encontrarla, pone match a true, para todos los hilos y muestra la contraseña.
                match = True
                print('MATCH! The password is:', password)


def end_program(sig, frame):                 #Funcion para acabar el programa por linea de comando. No borrar frame, pues da error
    global match
    match = True                             #Simplemente ponemos la variable match a true y anunciamos que es debido a una interrupción.
    print("\n Interrumpiendo ejecución...")
signal.signal(signal.SIGINT, end_program)    #Asociamos el apretar Ctrl+C con acabar el programa.

print("Iniciando programa...")

thread_list = []                             #Creamos la lista vacía de hilos.
for _ in range(num_threads):
    thread = threading.Thread(target=password_generator)  #Creamos el hilo, lo lanzamos y lo metemos en la lista creada anteriormente.
    thread.start()                          
    thread_list.append(thread)                  

for thread in thread_list:                   #Esperamos a que terminen los hilos
    thread.join() 
	
print("Fin del programa.")