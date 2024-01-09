# -- Importando los módulos --
from pyrogram import Client # Crear un cliente

# Importamos las funciones creadas y adaptadas para operar con callbacks
from central.usage.commands.cmd_start import start # Manejar el comando start
from central.usage.none_found import none # Manejar comandos sin desarrollar aún
from central.usage.menu.cmd_cmds import commands # Manejar el comando cmds
from central.usage.menu.cmd_gates import gate # Manejar el comando gates
from central.usage.menu.cmd_gen import gen # Manejar el comando gen
from central.usage.menu.cmd_tools import tools_menu # Manejar el comando tools
from central.usage.menu.cmd_admision import admision_query_carreras
from central.usage.menu.cmd_carrera_admision import admision_query_carrera

# -- CONTROLADOR DE LOS CALLBACKs --
@Client.on_callback_query()
async def button(Client, update):
      data_update = update.data
      try:
            if update.message.reply_to_message.from_user.id == update.from_user.id:
                if "start" in data_update: # CONTROLAR EL COMANDO "/start"
                    await start(Client, update.message)
                elif "ciclos_admision" in data_update: # CONTROLAR EL COMANDO "/cmds"
                    await commands(Client, update.message)
                elif "gates" in data_update: # CONTROLAR EL COMANDO "/gates"
                    await gate(Client, update.message)
                elif "gen" in data_update: # CONTROLAR EL COMANDO "/gen"
                    await gen(Client, update.message)
                elif "tools" in data_update: # CONTROLAR EL COMANDO "/tools"
                    await tools_menu(Client, update.message)
                elif "admision:" in data_update[:14]: # CONTROLAR SOLICITUDES DE ADMISION
                    ID = data_update.split(":")[1]
                    await admision_query_carreras(Client, update.message, ID)
                elif "admision_carrera" in data_update:
                    dq = data_update.split(":")[1]
                    CARRERA = dq.split("|")[0]
                    ESPECIALIDAD = dq.split("|")[1]
                    id = dq.split("|")[2]
                    await admision_query_carrera(Client, update.message, CARRERA, ESPECIALIDAD, id)

                else: # CONTROLAR COMANDOS INEXISTENTES
                    await none(Client, update.message, str(data_update))

            else:
                await Client.answer_callback_query(
            callback_query_id=update.id,
            text="⚠️ NO PUEDES USAR ESTE MENÚ PORQUE ES DE OTRO USUARIO!",
            show_alert="true"
          )
      except Exception as Error:
          print(Error)