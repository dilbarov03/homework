from telegram import Update

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import wikipedia
from gtts import gTTS


def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user

    update.message.reply_html(
        f"Hello {user.mention_html()}! I will find you data from wikipedia.\n\nJust send something"    
   )




def echo(update: Update, context: CallbackContext) -> None:
   try:
      query = update.message.text

      results = wikipedia.summary(query, sentences=15)

      res = f"Wikipedia says: \n\n{results}"

      update.message.reply_text(res)

      tts = gTTS(res)
      tts.save('wiki.mp3')
      audio = open('wiki.mp3', 'rb')

      context.bot.send_audio(chat_id=update.effective_user.id, audio=audio)


   except:
      update.message.reply_text("Sorry, I could not find anything")

def main() -> None:

    updater = Updater("5569624379:AAHYBXfa7ST9i80NgGgIik2qRBfTFvG0EkA")
    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))

    # on non command i.e message - echo the message on Telegram
    dispatcher.add_handler(MessageHandler(
        Filters.text & ~Filters.command, echo))

    # Start the Bot
    updater.start_polling()
    updater.idle()



if __name__ == "__main__":

    main()