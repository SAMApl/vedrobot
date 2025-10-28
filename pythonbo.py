from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8487910255:AAHe5WmQO5yDx7XSbboSjOHymVGXbvnyxpw"

TARGET_USER_ID = 5420403420  
GIF_URL = "https://media.giphy.com/media/v1.Y2lkPWVjZjA1ZTQ3eWZ1M3VqcnJja2s5NW1xb3AxN2JyYXE1aHVpMWNycTdrMnA3ZzNrciZlcD12MV9naWZzX3NlYXJjaCZjdD1n/LjXVOmTvaWj8GWkfy8/giphy.gif"
async def on_member_leave(update: Update, context: ContextTypes.DEFAULT_TYPE):
    member = update.message.left_chat_member
    if member.id == TARGET_USER_ID:
        await context.bot.send_animation(
            chat_id=update.effective_chat.id,
            animation=GIF_URL,
            caption=f"{member.full_name} покинул чат 😢"
        )
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, on_member_leave))
print("✅ Бот запущен!")
app.run_polling()