# Telegram AI Image Analysis Bot

A Telegram bot that uses OpenAI's GPT-4 Vision to analyze images and answer questions about them. The bot can also engage in educational conversations and answer general queries.

## Features

- 🖼️ Image Analysis: Send any image to get AI-powered analysis
- ❓ Follow-up Questions: Ask specific questions about previously sent images
- 🎓 Educational Assistant: Ask general educational questions
- ⚡ Real-time Responses: Quick processing and response times
- 🤖 GPT-4 Integration: Powered by OpenAI's advanced language models

## Prerequisites

- **Python 3.10.12**
- A Telegram Bot Token (obtained from [@BotFather](https://t.me/botfather))
- An OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/achuajays/telegram_image_and-text_assistent.git
cd telegram-ai-bot
```

2. Install required packages:
```bash
pip install python-telegram-bot openai requests
```

3. Set up environment variables:
```bash
export OPENAI_API_KEY="your-openai-api-key"
export TELEGRAM_BOT_TOKEN="your-telegram-bot-token"
```

## Configuration

The bot uses environment variables for configuration. You can also create a `.env` file in the project root:

```env
OPENAI_API_KEY=your-openai-api-key
TELEGRAM_BOT_TOKEN=your-telegram-bot-token
```

## Usage

1. Start the bot:
```bash
python telegram_aibot.py
```

2. In Telegram, start a conversation with your bot:
   - Send `/start` to begin
   - Send `/help` to see available commands
   - Send any image to get analysis
   - Ask follow-up questions about the image
   - Ask any educational questions

## Bot Commands

- `/start` - Initialize the bot and get welcome message
- `/help` - Display help information and usage instructions

## Features in Detail

### Image Analysis
- Send any image to the bot
- Receives AI-powered analysis of the image content
- Can ask follow-up questions about specific aspects of the image

### Text Queries
- Ask educational questions
- Get detailed responses powered by GPT-4
- Natural conversation flow

## Error Handling

The bot includes robust error handling for:
- Invalid images
- API failures
- Network issues
- Invalid queries

## Technical Details

- Uses `python-telegram-bot` for Telegram integration
- Implements OpenAI's GPT-4 Vision for image analysis
- Maintains conversation context for follow-up questions
- Asynchronous processing for better performance

## Limitations

- Image size may be limited by Telegram and OpenAI API restrictions
- Responses depend on OpenAI API availability
- Processing times may vary based on server load

## Contributing

Feel free to submit issues and enhancement requests!



## Acknowledgments

- OpenAI for providing the GPT-4 API
- Telegram for the Bot API
- Python Telegram Bot community

