import discord
from discord.ext import commands
from datetime import timedelta

# global static vars
TOK = ''
UID = 1101564218257445065

# discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# setup bot command prefixes
bot = commands.Bot(command_prefix='!', intents=intents)

# bot functions
@bot.event
async def on_ready():
    print(f'get ready dawit')
# end def on_ready()

@bot.event
async def on_message(message):
    # ignore msgs sent by bot
    if message.author == bot.user:
        return
    # end if statement
    # check if msg author matches target UID
    if message.author.id == UID and '1136470146463039600' in message.content:
        end = discord.utils.utcnow() + timedelta(hours=1)
        try:
            await message.author.timeout(end, reason='wompity womp womp bozo lmao')
            await message.channel.send(f'<@{UID}> automatically timed out for pinging Staff (most likely for a goofy reason)')
        except discord.Forbidden:
            await message.channel.send('Give me perms')
        except discord.HTTPException as e:
            await message.channel.send(f'error {e} :(')
        # end try/except block
    # end if statement

    await bot.process_commands(message)
# end def on_message()

# run bot code
bot.run(TOK)