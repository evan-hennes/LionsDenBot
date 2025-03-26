import discord
from discord import app_commands
from discord.ext import commands
from datetime import timedelta

# global static vars
TOK = ''
offenders = [1252854926766379014, 1251254260742754425]

# discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# setup bot command prefixes
bot = commands.Bot(command_prefix='>', intents=intents)

# slash command definitions
@bot.tree.command(
	name='ping',
    description='Pings Bot to ensure it is working'
)
async def ping_bot(interaction):
    await interaction.response.send_message(f'Pong!\nLatency: **{bot.latency * 1000}**ms')
# end def ping_bot

@bot.tree.command(
	name='faq',
    description='Links to certain FAQs',
    guild=discord.Object(id=974038998416781372)
)
async def faq(interaction, arg : str):
    if arg == 'Eucharistic Adoration':
        await interaction.response.send_mssage('https://discord.com/channels/974038998416781372/1332210521251905586/1332210524632649791')
    else:
        await interaction.response.send_message('Invalid Input - Please Try Again')
    # end if/else logic
# end def faq
    
# bot functions
@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f'Ready!')
# end def on_ready()

@bot.event
async def on_message(message):
    # ignore msgs sent by bot
    if message.author == bot.user:
        return
    # end if statement
    # check if msg author matches target UID & user has pinged staff/satff
    if message.author.id in offenders and ('1136470146463039600' in message.content or '1353955148489297960' in message.content):
        end = discord.utils.utcnow() + timedelta(hours=1)
        try:
            await message.author.timeout(end, reason='wompity womp womp bozo lmao')
            await message.channel.send(f'<@{message.author.id}> automatically timed out for pinging Staff (most likely for a goofy reason)')
        except discord.Forbidden:
            await message.channel.send('Give me perms')
        except discord.HTTPException as e:
            await message.channel.send(f'error {e} :(')
        # end try/except block
    # end if statement

    await bot.process_commands(message)
# end def on_message()

@bot.event
async def on_message_edit(before, after):
        # ignore msgs sent by bot
    if before.author == bot.user:
        return
    # end if statement
    # check if msg author matches target UID & user has pinged staff/satff
    if before.author.id in offenders and ('1136470146463039600' in after.content or '1353955148489297960' in after.content):
        end = discord.utils.utcnow() + timedelta(hours=1)
        try:
            await after.author.timeout(end, reason='wompity womp womp bozo lmao')
            await after.channel.send(f'<@{message.author.id}> tried to be sneaky and edit his message to ping Staff (I am always two steps ahead)')
        except discord.Forbidden:
            await after.channel.send('Give me perms')
        except discord.HTTPException as e:
            await after.channel.send(f'error {e} :(')
        # end try/except block
    # end if statement

    await bot.process_commands(after)
# end def on_message_edit()

# run bot code
bot.run(TOK)
