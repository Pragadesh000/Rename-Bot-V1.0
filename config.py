import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "27884084")

API_HASH = os.environ.get("API_HASH", "f41ef10f7e283ba0b6b18fac6fbe8226")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5981866762:AAG48TmlLfYGR08eQYJk1ivYRvETB5TGsi8") 

FORCE_SUB = os.environ.get("FORCE_SUB", "WebXBots") 

DB_NAME = os.environ.get("DB_NAME","cluster0")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Chittu:20urcm06@cluster0.ays8puc.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
