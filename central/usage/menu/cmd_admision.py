# -- Importando modulos --
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup # Crear botones
from pyrogram import Client, filters
import requests

def obtener_datos_admision(id):
    response = requests.get(f"https://apps.unsa.edu.pe/sisadmision/public/estadisticas/{id}").json()
    return response

#  ---- Mensajes de entorno ----
# Mensaje para nuevos

# -- Creando el controlador del mensaje --
async def admision_query_carreras(cliente_data, rsp_api, id):

    # - Verificando si la peticion es para editar o enviar un mensaje
    if rsp_api.from_user.is_self:
        self_rsp = True
        usr_rsp = rsp_api.reply_to_message
    else:
        self_rsp = False
        usr_rsp = rsp_api

    MENSAJE_FINAL = """✅ Puedes <b>buscar datos</b> de las siguientes carreras profesionales!."""

    response = obtener_datos_admision(id)

    lista_f = [[InlineKeyboardButton("[📖] REGRESAR A LOS CICLOS", callback_data="ciclos_admision")]]

    for carrera in response[:60]:
        ESPECIALIDAD = carrera.get("especialidad", "a")
        CARRERA = carrera["escuela"]
        mensaje_t = f"{CARRERA}"
        if ESPECIALIDAD:
            mensaje_t += f" | {ESPECIALIDAD}"
            ESPECIALIDAD = ESPECIALIDAD[:10]

        #print (mensaje_t, f'[SEPARATE] admision_carrera:{CARRERA}|{ESPECIALIDAD}|{id}')
        lista_f.append([InlineKeyboardButton(mensaje_t, callback_data=f'admision_carrera:{CARRERA}|{ESPECIALIDAD}|{id}')])    
        
    buttons = InlineKeyboardMarkup(
                                    lista_f
                                )

    await cliente_data.edit_message_text(
        chat_id=usr_rsp.chat.id,
        text=MENSAJE_FINAL,
        reply_markup=buttons,
        message_id=rsp_api.id,
        disable_web_page_preview=True
    )