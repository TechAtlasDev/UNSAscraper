# -- Importando modulos --
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup # Crear botones

# -- Botones del mensaje --
buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("[🔎] Menú de ciclos | ADMISION", callback_data='ciclos_admision')
        ]
    ]
)

#  ---- Mensajes de entorno ----
# Mensaje para clientes nuevos
MENSAJE_NUEVOS = """[👋] Hola!, Este bot te permitirá obtener información que necesitas de los procesos de <b>admisión de la UNSA</b>."""

# -- Creando el controlador del mensaje --
@Client.on_message(filters.command(['start', 'inicio', 'iniciar'], prefixes=['/',',','.','!','$','-'], case_sensitive=False) & filters.text)
async def start(cliente_data, rsp_api):

    # - Verificando si la peticion es para editar o enviar un mensaje
    if rsp_api.from_user.is_self:
        self_rsp = True
        usr_rsp = rsp_api.reply_to_message
    else:
        self_rsp = False
        usr_rsp = rsp_api

    # --- Inicio del control de flujo ---
    if True: # SI EL USUARIO SI EXISTE EN LA BASE DE DATOS
        # Extrayendo e indicando los datos
        if self_rsp: # Si se tiene que editar el mensaje
            await cliente_data.edit_message_text(
                chat_id=usr_rsp.chat.id,
                text=MENSAJE_NUEVOS,
                message_id=rsp_api.id,
                reply_markup=buttons,
                disable_web_page_preview=True
            )
        else: 
            await rsp_api.reply(text=MENSAJE_NUEVOS,
                                reply_markup=buttons,
                                quote=True) # Respuesta al usuario final