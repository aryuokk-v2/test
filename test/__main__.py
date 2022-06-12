import request

from pyrogram import client
from config import Aryan

aryu = Client("my_bot", 
            api_id = Aryan.api_id, 
            api_hash = Aryan.api_hash,
            session_string = Aryan.string, 
            bot_toekn = Aryan.bot_token, 
            plugins = dict(root="plugins")
            )

async def start():
    print('\n')
    print('------------------ Initalizing Bot --------------------')
    if aryu:
        aryu.start()
    print('------------------------ DONE --------------------------')
    print('------------------- INITIATED Bot ---------------------')
    print('     Logged in as User =>> {}'.format((await aryu.get_me()).first_name))
    if bot:
        print('     Logged in to Bots =>> {}'.format((await aryu.get_me()).first_name))
    print('--------------------------------------------------------')
    await idle()
if __name__ == '__main__':
    is_bot = bool(Aryan.bot_token)
    loop.run_until_complete(start())