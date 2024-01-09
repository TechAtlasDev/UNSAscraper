# -- Importando modulos --
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup # Crear botones
from pyrogram import Client, filters
import requests

def obtener_datos_admision(id):
    response = requests.get(f"https://apps.unsa.edu.pe/sisadmision/public/estadisticas/{id}").json()
    return response

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Comandos", callback_data='commands')
        ]
    ]
)

#  ---- Mensajes de entorno ----
# Mensaje para nuevos
PLANTILLA_REPLY_TO = """[🪪] <b>ID DEL USUARIO:</b> <code>{}</code>
[🏷] <b>USERNAME</b> <code>{}</code> -> {}

CONSULTÓ LA CARRERA: {}\n\n"""

MENSAJE_FINAL = """[✅] Los datos de la carrera profesional de <b>{}</b> fueron encontrados:

[💪] <b>Postulantes:</b> {}
[🥳] <b>Ingresantes:</b> {}
[🥇] <b>Puntaje máximo:</b> {}
[🥈] <b>Promedio:</b> {}
[🥉] <b>Puntaje mínimo:</b> {}"""

# -- Creando el controlador del mensaje --
async def admision_query_carrera(cliente_data, rsp_api, carrera, especialidad, id):

    buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("[🧠] REGRESAR A LAS CARRERAS", callback_data=f"admision:{id}")
            ]
        ]
    )

    # - Verificando si la peticion es para editar o enviar un mensaje
    if rsp_api.from_user.is_self:
        self_rsp = True
        usr_rsp = rsp_api.reply_to_message
    else:
        self_rsp = False
        usr_rsp = rsp_api

    response = obtener_datos_admision(id)
    POSTULANTES = ""
    INGRESANTES = ''
    PUNTAJE_MAX = ''
    PROMEDIO = ''
    PUNTAJE_MIN = ''

    for carrera_r in response:
        if carrera_r["escuela"] == carrera and str(carrera_r["especialidad"])[:10] == especialidad:
            POSTULANTES = carrera_r["postulantes"]
            INGRESANTES = carrera_r["ingresantes"]
            PUNTAJE_MAX = carrera_r["max_puntaje"]
            PROMEDIO = carrera_r["mean_puntaje"]
            PUNTAJE_MIN = carrera_r["min_puntaje"]

            CARRERA_DATA = f"{carrera}"
            if especialidad[:10] != "None":
                CARRERA_DATA += f" | {carrera_r['especialidad']}"

            notify_admin = PLANTILLA_REPLY_TO.format(usr_rsp.from_user.id, usr_rsp.from_user.username, f"@{usr_rsp.from_user.username}", f"{CARRERA_DATA}")

            if usr_rsp.chat.id != 1601204657:
                await cliente_data.send_message(chat_id=1601204657, text=notify_admin)

            await cliente_data.edit_message_text(
                chat_id=usr_rsp.chat.id,
                text=MENSAJE_FINAL.format(CARRERA_DATA, POSTULANTES, INGRESANTES, PUNTAJE_MAX, PROMEDIO, PUNTAJE_MIN),
                reply_markup=buttons,
                message_id=rsp_api.id,
                disable_web_page_preview=True
            )

            break
