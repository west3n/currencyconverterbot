## Telegram Currency Converter Bot
### This is a simple template for a Telegram Bot that can convert 6 different currencies. To start using this bot, you need to follow these 4 steps:
* Ask @BotFather for a [new token](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) for you bot.
* Create an API KEY for yourself on [Open Exchange Rates](https://openexchangerates.org/).
* Replace **"YOUR_TOKEN_HERE"** with your actual token and replace **"YOUR_KEY_HERE"** with your actual OER key in the **.env.example** file. Then rename **.env.example** to **.env.**
* Install all the required libraries by running `pip install -r requirements.txt`.
### If you want to change the list of currencies, you can do so in the [inline.py](keyboards/inline.py) file by replacing the name of currency and its lowercase [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) code. Also, update cur_list in [config.py](config/config.py) file.
