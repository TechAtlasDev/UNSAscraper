# FUNCIÓN CREADA PARA MANEJAR CON BOTONES O FUNCIONES AÚN POR DESARROLLAR
# -- Importando modulos --
#from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup # Crear botones
import json

# ----- PUEDES CREAR LOS BOTONES SI DESEAS ------

json_data_r = "central/info_lost.json" # Modifica este archivo mencionado para poder controlar los datos de tus generadores

#  ---- Mensajes de entorno ----
# -- Creando el controlador del mensaje --
async def none(cliente_data, rsp_api, command_type):

    # - Verificando si la peticion es para editar o enviar un mensaje
    if rsp_api.from_user.is_self:
        self_rsp = True
        usr_rsp = rsp_api.reply_to_message
    else:
        self_rsp = False
        usr_rsp = rsp_api


    with open(json_data_r, 'r') as data_config:
        json_data = json.load(data_config)
    var_data = next((item for item in json_data if item['function'] == str(command_type)), None)

    message_data = f"""❗️<b>AL PARECER ESTE COMANDO SIGUE EN CONSTRUCCIÓN.</b>
    
- <b>DESCRIPCIÓN DEL COMANDO:</b> {var_data["description"]}

- <b>MENSAJE DEL DESARROLLADOR:</b> {var_data["mensaje_dev"]}

- <b>FECHA APROXIMADA DE SALIDA:</b> {var_data["fecha_fin"]}
"""

    # --- Inicio del control de flujo ---
    if self_rsp: # Si se tiene que editar el mensaje
        await cliente_data.edit_message_text(
            chat_id=usr_rsp.chat.id,
            text=message_data,
            message_id=rsp_api.id,
            disable_web_page_preview=True
        )
    else: 
        await rsp_api.reply(text=message_data, quote=True) # Respuesta al usuario final