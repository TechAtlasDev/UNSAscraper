# -- Inicializador del Scrapper UNSA --
# Módulos básicos
import sys, time, os

# Funcion para limpiar la pantalla de la terminal (compatible para Windows y Linux)
def clear_terminal():
  os.system('cls' if os.name == 'nt' else 'clear')

#Colores del sistema
GL = "\033[96;1m" # Azul agua
BB = "\033[34;1m" # Azul claro
YY = "\033[33;1m" # Amarillo claro
GG = "\033[32;1m" # Verde claro
WW = "\033[0;1m"  # Blanco claro
RR = "\033[31;1m" # Rojo claro
CC = "\033[36;1m" # Cyan claro
B = "\033[34m"    # Azul
Y = "\033[33;1m"  # Amarillo
G = "\033[32m"    # Verde
W = "\033[0;1m"   # Blanco
R = "\033[31m"    # Rojo
C = "\033[36;1m"  # Cyan
M = "\033[35;1m"  # Morado

# Banner del sistema
banner = f"""           Bienvenido, este es el scrapper de datos a la UNSA

{WW}------------------------------------------------------------------------------------------------------
"""

# Funciones de animación
def sutil(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(9. / 150)

def fast(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 150)

def retry_after():
    fast(f"{RR} - SE PRODUJO UN ERROR EN EL PROCESO, VUELVE A INTENTARLO MÁS TARDE O TRATA DE RESOLVERLO.")
    sys.exit()

# Mensajes para el usuario del sistema
info = BB+"["+WW+"INFO"+BB+"]"+WW+" {}"
error = RR+"["+WW+"ERROR"+RR+"]"+WW+" {}"
done = GG+"["+WW+"DONE"+GG+"]"+WW+" {}"

# -- Comenzando bienvenida --
clear_terminal() # Limpiando la pantalla
print (banner) # Mostrando el banner
sutil(Y+"-- Bienvenido al sistema, el bot se prenderá a continuación. --") # Animación para el usuario

fast(info.format("Importando los módulos. -> main.py"))
# Importando módulos
try:
    from pyrogram import Client
    import json
    import os
except Exception as Error:
    fast(error.format(f"Se produjo un error al importar los módulos.\nError: {Error}\nArchivo: main.py"))
    retry_after()

fast(done.format("Se logró importar los módulos. -> main.py"))

# Obteniendo los datos del documento json de configuracion
fast(info.format("Obteniendo datos de configuración del bot. -> main.py"))
try:
    with open('central/config.json', 'r') as data_config:
        config = json.load(data_config)
except Exception as Error:
    fast(error.format(f"Se produjo un error al importar el archivo de configuración.\nError: {Error}\nArchivo: main.py"))
    retry_after()

# Accediendo a las variables para configurar el bot
try:
    api_id = config['info_bot']['api_id']
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener el ID del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()
    
try:
    api_hash = config['info_bot']['api_hash']
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener el HASH del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    bot_token = config['info_bot']['bot_token']
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener el Token del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    version = config['info_bot']['version_sys']
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener la version del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    libreria = config['info_bot']['libreria']
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener la libreria del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    root_dir = config['root_dir']
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener el directorio raíz del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    platform = config['info_bot']["platform"]
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener la plataforma del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    name = config['info_bot']["name"]
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener el nombre del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    mention = config['info_bot']["mention"]
except Exception as Error:
    fast(error.format(f"Se produjo un error la etiqueta del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    url = config['info_bot']["url"]
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener la URL del bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

try:
    database_name = config['database']["database"]
except Exception as Error:
    fast(error.format(f"Se produjo un error al obtener el nombre de la base de datos usada por el bot.\nError: {Error}\nArchivo: main.py"))
    retry_after()

fast(done.format("Se logró obtener los valores necesarios. -> main.py"))

print (GG+"\n-- INFORMACIÓN OBTENIDA DEL BOT --")
print (f"{YY}- ID: {WW}{api_id}")
print (f"{YY}- HASH: {WW}{api_hash}")
print (f"{YY}- Token: {WW}{bot_token}")
print (f"{YY}- Version del sistema: {WW}{version}")
print (f"{YY}- Librería: {WW}{libreria}")
print (f"{YY}- Plataforma de uso: {WW}{platform}")
print (f"{YY}- Nombre del bot: {WW}{name}")
print (f"{YY}- Tag del bot: {WW}{mention}")
print (f"{YY}- URL de acceso: {WW}{url}")
print (f"{YY}- Nombre de la base de datos: {WW}{database_name}")
print (f"{YY}- Directorio raíz: {WW}{root_dir}\n")

# Creando el cliente de la API
fast(info.format("Creando el cliente para la comunicación de la API. -> main.py"))
try:
    bot_project = Client(
        name,
        api_id=api_id,
        api_hash=api_hash,
        bot_token=bot_token,
        plugins=dict(root=root_dir)
    )

except Exception as Error:
    fast(error.format(f"Se produjo un error al crear el cliente.\nError: {Error}\nArchivo: main.py"))
    retry_after()


fast(done.format("Se pudo crear el cliente exitosamente. -> main.py"))

# Ejecutando el bot
fast(info.format("Ejecutando el bot. -> main.py"))
try:
    bot_project.run()
except Exception as Error:
    fast(error.format(f"Se produjo un error al ejecutar el bot.\nError: {Error}"))
    retry_after()