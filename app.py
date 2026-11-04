import os
import logging
from flask import Flask, request, jsonify
from rubpy.bot import BotClient
from rubpy.bot.models import Update
from rubpy.bot.filters import text, private
import asyncio

# ۱. تنظیمات لاگ
logging.basicConfig(level=logging.INFO)

# ۲. توکن ربات پنجم شما
TOKEN = "CIFCHE0MNIVPJTRICRRRGJEHBETUOKQTTLFYJFAHBMXSDPBPSHAUXLTQPRYMCXUF"

# ۳. ساخت ربات
bot = BotClient(TOKEN)

# --- شروع دستورات ربات ---
@bot.on_update(text("start") | text("/start") | text("/START"), private)
async def start_command(client, update: Update):
    await update.reply(
        "⚡ به ربات خوش آمدید!\n\n"
        "برای فعال‌سازی خدمات، ابتدا در هر دو لینک زیر عضو شوید:\n\n"
        "🔗 Link 1:\nhttps://rubika.ir/joinc/FBIGDDHE0LSYBPATLJVHMSEZKEVUFFSG\n\n"
        "🔗 Link 2:\nhttps://rubika.ir/joing/EHACIABJ0OSWHRPZLOIMCMDQKQALNBFG\n\n"
        "✅ پس از عضویت، روی دستور /Join کلیک کنید تا خدمات ربات فعال شود.\n\n"
        "💎 موفق باشید!"
    )

@bot.on_update(text("join") | text("/join") | text("/Join"), private)
async def join_command(client, update: Update):
    await update.reply(
        "🔖 | خـدمـات‌ربـات ↓\n\n"
        "⟨🔹⟩ مـشـاهـده‌آیــدی‌دسـتـیـاران ⇙\n📲 /ADMINS\n\n"
        "⟨🔹⟩ مـشـاهـده‌مـدارک‌اعـتـمـاد ⇙\n📲 /TRUST\n\n"
        "⟨🔹⟩ عـضــویـت‌درگــروه‌اصــلی ⇙\n📲 /GROUP\n\n"
        "⟨🔹⟩ ‌گـپ‌ریـپـورت‌چـت ⇙\n📲 /REPORT\n\n"
        "⟨🔹⟩ شـاپ‌اگـهـی‌اکـانـت ⇙\n📲 /STORE\n\n\n"
        "مـعـامــلــات‌ خـود‌ را ایـمـن‌ انـجـام‌ دهـیـد!"
    )

@bot.on_update(text("admins") | text("/admins") | text("/ADMINS"), private)
async def admins_command(client, update: Update):
    await update.reply("🌐 | تـنـهـا آیـدی دسـتـیـاران بـنـده :\nhttps://rubika.ir/VaSeTe_MaTiN_le/JIBCHHHADJJHJEJ")

@bot.on_update(text("trust") | text("/trust") | text("/TRUST"), private)
async def trust_command(client, update: Update):
    await update.reply("🤝 | مــدارک اعـتـمـاد مـشـتـریـان :\niD : @ETEMAD_MaTiN_Le")

@bot.on_update(text("group") | text("/group") | text("/GROUP"), private)
async def group_command(client, update: Update):
    await update.reply("💭 | گــروه اصــلی واسـطـه گــری :\nhttps://rubika.ir/joing/BBJEBDABF0LXYUBBTJLKCNUAYEZIPZUK")

@bot.on_update(text("report") | text("/report") | text("/REPORT"), private)
async def report_command(client, update: Update):
    await update.reply("💭 | گــروه ریـپـورت چــت :\nhttps://rubika.ir/joing/BBJEBBHEA0XHTXBYTKYAVMPCHTZJXYNT")

@bot.on_update(text("store") | text("/store") | text("/STORE"), private)
async def store_command(client, update: Update):
    await update.reply("🛍 | شـاپ خـریـد و فـروش اکـانـت :\n@Pes_Foroshgah")
# --- پایان دستورات ربات ---


# ۴. تنظیم وب‌سرور برای Render
app = Flask(__name__)

@app.route('/')
def home():
    return "Rubika Bot is Alive!"

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    try:
        update = Update.model_validate(data)
        asyncio.run(bot.process_update(update))
    except Exception as e:
        logging.error(f"Error processing update: {e}")
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
