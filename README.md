# UNSAscrapper 🖥️

## Descripción 📝

Este es un bot creado con fines informativos, desarrollado para consultar datos a la API libre del sistema de admisión de la UNSA (Universidad Nacional de San Agustín, Arequipa), con el que permite hacer un despliegue del proyecto en un bot de telegram.

## Objetivos 🎯

Evitar la desinformación o la búsqueda no fructífera de información en lo que respecta la obtención de datos referentes al exámen de admisión que lleva a cabo la Universidad Nacional de San Agustín, que publica para comprender diferentes ramas estadísticas que se encuentran al desarrollar un examen de admision.

## Funcionalidades 💡

Este bot fué creado para obtener datos de la plataforma pública de la UNSA para darse uso a través de la interfaz de telegram, usando unos simples comandos y manejarlo usando unos botones diseñados para su simple interacción.

## Requisitos 🛠️

- <code>Pyrogram</code> Librería para la interacción con la API de telegram.
- <code>TgCrypto</code> Librería para la interacción segura con la API de telegram.

## Instalación 💻

Para instalar correctamente el bot, sigue los siguientes pasos:

1) Obtener datos de acceso a la API:
    - Obtener el <code>API ID</code> que proporciona telegram.
    - Obtener el <code>API HASH</code> que proporciona telegram.
    - Obtener el <code>BOT TOKEN</code> que proporciona telegram.
    - Establecer el nombre del bot.

<br>

2) Clonar este repositorio:
    - Si vas a usar la terminal, usa el siguiente comando: <code>git clone https://github.com/TechAtlasDev/UNSAscrapper</code>

<br>

3) Configurar el bot a través del archivo JSON del bot:
    - Modificar las variables de acceso del bot a través del directorio <code>/central/config.json</code>

<br>

4) Instalar las dependencias:
    - La librería principal que permite comunicarse a la API no viene instalada por defecto en Python, por lo que, tenemos que instalarlo a través de <b>PIP</b>: <code>pip install pyrogram</code> y también <code>pip install tgcrypto</code>

<br>

5) Ejecutar el bot:
    - Luego de instalar las dependencias, ejecuta el bot con el comando <code>python main.py</code>
    - Ahora que el bot esté funcionando y no se presente algún error, tienes que ir al @ del bot que estableciste cuando obtuviste las credenciales de tu bot, y usa el comando /start
