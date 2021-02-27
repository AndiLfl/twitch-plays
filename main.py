import twitch
import keypresser
import keyholder
import os
import dotenv

dotenv.load_dotenv()
t = twitch.Twitch()
k = keypresser.Keypresser()

username = os.getenv("USER")
key = os.getenv("TOKEN")
t.twitch_connect(username, key)

while True:
    new_messages = t.twitch_recieve_messages()
 
    if not new_messages:
        continue
    else:
        for message in new_messages:
            msg = message['message'].lower()
            username = message['username'].lower()
            print((username + ": " + msg).encode('utf-8'))

            if msg == "w": keyholder.holdForSeconds(msg, 0.3)
            if msg == "s": keyholder.holdForSeconds(msg, 0.3)
            if msg == "a": keyholder.holdForSeconds(msg, 0.1)
            if msg == "d": keyholder.holdForSeconds(msg, 0.1)
            if msg == "e": keyholder.holdForSeconds(msg, 0.5)
            if msg == "q": keyholder.holdForSeconds(msg, 0.1)
            if msg == "t": keyholder.holdForSeconds(msg, 0.5)