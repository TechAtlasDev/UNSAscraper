# -- Importando modulos --
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup # Crear botones
from pyrogram import Client, filters
import json

def cargar_datos_config(ruta_acceso="central/config.json"):
    with open(ruta_acceso, "r", encoding="utf-8") as datos:
        return json.load(datos)

#  ---- Mensajes de entorno ----
# Mensaje para nuevos
message_data = """✅ Este apartado contiene datos de los ciclos de admisión <b>organizados por la UNSA</b>

<i>Datos basados en: https://apps.unsa.edu.pe/sisadmision/public/estadistica</i>"""

# -- Creando el controlador del mensaje --
@Client.on_message(filters.command(['cmds', "cmd"], prefixes=['/',',','.','!','$','-'], case_sensitive=False) & filters.text)
async def commands(cliente_data, rsp_api):

    # - Verificando si la peticion es para editar o enviar un mensaje
    if rsp_api.from_user.is_self:
        self_rsp = True
        usr_rsp = rsp_api.reply_to_message
    else:
        self_rsp = False
        usr_rsp = rsp_api

    config = cargar_datos_config()

    # Accediendo a la lista de datos
    lista = config["DATA_UNSA"]
    lista_f = [[InlineKeyboardButton("[🏁] REGRESAR AL MENÚ", callback_data="start")]]
    for data in lista:
        lista_f.append([InlineKeyboardButton(lista[data]["data"], callback_data=f'admision:{lista[data]["id"]}')])

    cmd_cmds_buttons = InlineKeyboardMarkup(
                                    lista_f
                                )


    # --- Inicio del control de flujo ---
    if self_rsp: # Si se tiene que editar el mensaje
        await cliente_data.edit_message_text(
            chat_id=usr_rsp.chat.id,
            text=message_data,
            reply_markup=cmd_cmds_buttons,
            message_id=rsp_api.id,
            disable_web_page_preview=True
        )
    else: 
        await rsp_api.reply(text=message_data, quote=True, reply_markup=cmd_cmds_buttons) # Respuesta al usuario final
    # --- Fin del control de flujo ---