# ABOUT
Twitch Plays allows you to have an interactive stream with your chat. Let the chat control your keyboard and mouse.
# INSTALLATION
**Requirements:**
- Python 3 or higher

**Installation**
- ``
git clone https://github.com/silentninja2/twitch-plays.git
``
- Copy .env.default and rename it to .env
- Add your Twitch username in lowercase to the .env file (ex. USERNAME="the_silentninja")
- Get your Twitch OAUTH Token from [Twitch Apps](https://twitchapps.com/tmi/) and set it as TOKEN in your .env
# CUSTOMIZATION
You can create more actions in the main.py file.
### Hold for seconds

With this function, your key gets activated for an amount of seconds.

In the example below, your "w" key gets activated for .3 seconds if any users types "w" in the chat.

``
if msg == "w": keyholder.holdForSeconds(msg, 0.3)
``

If you don't want the user to type the specific key, you can change the function like this:

``
if msg == "walkForward": keyholder.holdForSeconds("w", 0.3)
``

### Press

The keyholder.press() function triggers every key once.
Example:

``
if msg == "wasd": keyholder.press('w', 'a', 's', 'd')
``

### Press and hold & release
The keyholder.pressAndHold() function holds every key until they get released with the keypress.release() function.

In the example below, sprint holds 'w' and 'r' at the same time for 5 seconds, then releases both keys. 

```
if msg == "sprint":
    keyholder.pressAndHold('r', 'w')
    time.sleep(5)
    keyholder.release('r', 'w')
```
### Press hold and release
With the keyholder.pressHoldRelease() function, you can trigger keys for 2 seconds, then release them.

This function can be used for keyboard shortcuts like in the example below for paste your clipboard.

``
if msg == "paste": keyholder.pressHoldRelease('ctrl', 'v')
``

# CREDITS
Credits goes to [Geert Verhoeff](https://www.youtube.com/channel/UC51BxjwdWvwnmehHBWoB6bg) he originally made the code.

I changed it so it's python 3 compatible and made some other improvements.