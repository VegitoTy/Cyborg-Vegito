import discord, json, os, pathlib
from dotenv import load_dotenv
from discord.ext import commands
from bot.extensions.utility import Verifyview
from bot.extensions.apps import StaffAppsView, AcceptDenyFruitStockerView, AcceptDenyModView

dotenv_path = pathlib.Path('./.env')
load_dotenv(dotenv_path=dotenv_path)

TOKEN = os.getenv("TOKEN")

with open("./configs/config.json") as f:
    bot_config = json.load(f)

class Berserker(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or("&"),
            status=discord.Status.idle,
            activity=discord.Activity(type=discord.ActivityType.watching, name="Berserkers"),
            intents=discord.Intents.all()
        )

    async def setup_hook(self):
        default_guilds = bot_config["bot"]["default_guild"]
        for filename in os.listdir('./bot/extensions'):
            if filename.endswith('.py'):
                extension = f"bot.extensions.{filename[:-3]}"
                await self.load_extension(extension)
        await self.load_extension('bot.help.cog')
        await self.load_extension('jishaku')
        self.add_view(AcceptDenyModView())
        self.add_view(AcceptDenyFruitStockerView())
        self.add_view(StaffAppsView())
        self.add_view(Verifyview())
        await bot.tree.sync(guild = discord.Object(id = default_guilds))
    
    async def on_ready(self):
        channel = self.get_channel(bot_config["logging"]["startup"])
        await channel.send('Bot Has Started')
        print(f'Logged In As {self.user}')

bot = Berserker()
bot.run(TOKEN)