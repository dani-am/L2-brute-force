# Lab2 - Script de Fuerza Bruta
Curso: Seguridad en Redes - 2024/2025
Daniel Aguado

## Descripción breve
Script en Python que desencripta mediante fuerza bruta un PDF protegido con PGP, empleando un diccionario simple de letras del abecedario.

## Consideraciones previas

 - El archivo pdf a desencriptar debe estar en la misma carpeta que el
   fichero brute.py con el nombre *archive.pdf.gpg* 
  - Se ha incluido un *makefile* para preparar el entorno de ejecución.
	- **make install:** Instala los paquetes necesarios dentro del entorno virtual.
	- **make run:** Ejecuta el script dentro del entorno virtual
	- **make clean:** Elimina el entorno virtual.

## Partes importantes del programa

1. **Iterador**: Genera todas las posibles combinaciones para una contraseña, cuya longitud va de 1 hasta 5. Este límite de 5 se puede aumentar o disminuir según sea necesario **en el propio código**.

2. **Función generator**: Se encarga de proporcionar una contraseña a un hilo, el cual probará en el archivo PDF.

3. **Lista de hilos**: Controlada por el hilo principal, el cual lanza todos a la vez. Por defecto, se utilizan 50 hilos, pero este número puede ser modificado **en el propio código**.

---
En el fichero brute.py se encuentra una descripción del funcionamiento más detallada del programa.

