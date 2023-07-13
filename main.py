import app.bot_command as bc


def main() -> None:
    bc.bot.infinity_polling(none_stop=True)
    

if __name__ == '__main__':
    main()