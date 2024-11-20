import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from openai import OpenAI
import base64
from io import BytesIO
import requests

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

client = OpenAI(api_key=OPENAI_API_KEY)


# Function to download and encode image from Telegram
async def download_and_encode_image(file_path):
    response = requests.get(file_path)
    return base64.b64encode(response.content).decode('utf-8')


# OpenAI function for getting responses (text-only queries)
async def get_openai_response(user_query):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": user_query}]
        )
        return response.choices[0].message.content
    except Exception as e:

        return "Sorry, I couldn't process that. Please try again later."


# OpenAI function for image analysis
async def analyze_image(base64_image, question="What is in this image?"):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": question,
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
        )
        return response.choices[0].message.content
    except Exception as e:

        return "Sorry, I couldn't analyze the image. Please try again later."


# Start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hello! I am your image analysis and educational assistant. "
        "You can:\n"
        "1. Send me any image to analyze\n"
        "2. Ask me questions about the image\n"
        "3. Ask me any educational questions"
    )


# Help command handler
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Here's how to use this bot:\n"
        "- Send an image to get analysis\n"
        "- Send text questions about the image\n"
        "- Ask any educational questions\n"
        "- Use /start to begin\n"
        "- Use /help to see this message"
    )


# Handle text messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_chat_action(action="typing")

    # If we have a recent image in context, treat this as a question about the image
    if 'last_image' in context.user_data:
        response = await analyze_image(context.user_data['last_image'], update.message.text)
    else:
        response = await get_openai_response(update.message.text)

    await update.message.reply_text(response)


# Handle images
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.message.reply_chat_action(action="typing")

        # Get the photo file
        photo = update.message.photo[-1]  # Get the largest photo size
        file = await context.bot.get_file(photo.file_id)

        # Download and encode the image
        base64_image = await download_and_encode_image(file.file_path)

        # Store the image in context for follow-up questions
        context.user_data['last_image'] = base64_image

        # Analyze the image
        response = await analyze_image(base64_image)

        await update.message.reply_text(response)
        await update.message.reply_text("You can ask me specific questions about this image!")

    except Exception as e:
        print(f"Error processing image: {e}")
        await update.message.reply_text("Sorry, I couldn't process that image. Please try again.")


# Main function to set up the bot
def main():
    application = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Run the bot
    print("Bot is running...")
    application.run_polling()


if __name__ == "__main__":
    main()