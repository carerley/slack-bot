import logging
logging.basicConfig(level=logging.DEBUG)

from slack_bolt import App

# export SLACK_SIGNING_SECRET=***
# export SLACK_BOT_TOKEN=xoxb-***
app = App()

# Add functionality here
@app.message("hello")
def handle_message_hello(body, say, logger):
    print("receive message")
    print(body["event"]["text"])
    say("what's up?")

    app.client.chat_postMessage(channel="#bot-cast", text=body["event"]["text"])

if __name__ == "__main__":
    print("starting slack app ...")
    app.start(3000)  # POST http://localhost:3000/slack/events