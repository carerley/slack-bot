import os
import logging
logging.basicConfig(level=logging.DEBUG)

from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

@app.message("hello")
def message_hello(message, say):
    print("receive message")
    print(message)
    # say() sends a message to the channel where the event was triggered
    say(f"Hey there <@{message['user']}>!")

if __name__ == "__main__":
    print("app starting...")
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
    