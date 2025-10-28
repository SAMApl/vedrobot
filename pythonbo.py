from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8487910255:AAHe5WmQO5yDx7XSbboSjOHymVGXbvnyxpw"

TARGET_USER_ID = 1310130564  
GIF_URL = "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdXg0YjUycGR2cTNnYjYwcGR3M3p3MGk5NzFkMnBlYzBkZXNzY2JqeSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YV6rWBvUkWHF39V1sZ/giphy.gif"
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