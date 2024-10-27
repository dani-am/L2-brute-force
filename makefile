VENV := env

# Objetivo principal que crea el entorno, instala dependencias y ejecuta el script
all: $(VENV)/bin/activate run

# Crea el entorno virtual si no existe
$(VENV)/bin/activate: 
	python3 -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt
	touch $(VENV)/bin/activate

# Instala los paquetes necesarios dentro del entorno virtual
install: $(VENV)/bin/activate

# Ejecuta el script dentro del entorno virtual
run:
	$(VENV)/bin/python3 brute.py

# Elimina el entorno virtual
clean:
	rm -rf $(VENV)

# No borrar por si acaso
.PHONY: all install run clean

