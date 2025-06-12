# test_telegram.py

import os
from dotenv import load_dotenv
import asyncio
import telegram

# Cargar variables del entorno
load_dotenv()

# Leer credenciales
token = os.getenv("TELEGRAM_BOT_TOKEN")
chat_id = os.getenv("TELEGRAM_CHAT_ID")

async def enviar_mensaje():
    if not token or not chat_id:
        print("❌ Faltan credenciales en .env")
        return

    try:
        bot = telegram.Bot(token=token)
        async with bot:
            await bot.send_message(chat_id=chat_id, text="✅ ¡Prueba exitosa desde tu IA bursátil!")
            print("✅ Mensaje enviado por Telegram")
    except Exception as e:
        print(f"❌ Error al enviar mensaje: {e}")

# Ejecutar la función asíncrona
asyncio.run(enviar_mensaje())