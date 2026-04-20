import discord, requests, json


def get_meme():
    response = requests.get("https://meme-api.com/gimme")
    json_data = json.loads(response.text)
    return json_data["url"]


def get_coffee():
    response = requests.get("https://coffee.alexflipnote.dev/random.json")
    json_data = json.loads(response.text)
    return json_data["file"]


def get_dog():
    response = requests.get("https://random.dog/woof.json")
    json_data = json.loads(response.text)
    return json_data["url"]


def get_duk():
    response = requests.get("https://random-d.uk/api/v2/random")
    json_data = json.loads(response.text)
    return json_data["url"]


def get_fox():
    response = requests.get("https://randomfox.ca/floof/")
    json_data = json.loads(response.text)
    return json_data["image"]


class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}".format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())

        if message.content.startswith("$coffee"):
            await message.channel.send(get_coffee())

        if message.content.startswith("$dog"):
            await message.channel.send(get_dog())

        if message.content.startswith("$duk"):
            await message.channel.send(get_duk())

        if message.content.startswith("$fox"):
            await message.channel.send(get_fox())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run("SECRET UwU")
