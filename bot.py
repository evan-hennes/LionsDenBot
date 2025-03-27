import discord
from discord import app_commands
from discord.ext import commands
from datetime import timedelta
from typing import List

# global static vars
TOK = ''
offenders = [1252854926766379014, 1251254260742754425]
options = {
    'eucharistic adoration' : 'https://discord.com/channels/974038998416781372/1332210521251905586/1332210524632649791',
    'problem of evil' : 'https://discord.com/channels/974038998416781372/1332210521251905586/1337088399068368896',
    'theosis' : 'https://discord.com/channels/974038998416781372/1332210521251905586/1353435482851250292', 
    'hell' : 'https://discord.com/channels/974038998416781372/1332211100485419070/1332211103907713054',
    'unbaptized infants' : 'https://discord.com/channels/974038998416781372/1332211100485419070/1332211239744442411',
    'loved ones in hell' : 'https://discord.com/channels/974038998416781372/1332211100485419070/1332211354597068850',
    'fallen angels' : 'https://discord.com/channels/974038998416781372/1332211100485419070/1332211305523974145',
    'scriptural argument for miaphysis' : 'https://discord.com/channels/974038998416781372/1332211731581112350/1332211736199168093',
    'definitions of *prosopon*' : 'https://discord.com/channels/974038998416781372/1332211731581112350/1332212222033924147',
    'did christ fear death' : 'https://discord.com/channels/974038998416781372/1332211731581112350/1332212376925241407',
    'theosis contra protestantism' : 'https://discord.com/channels/974038998416781372/1332212773370990623/1332212778689101835',
    'intercession' : 'https://discord.com/channels/974038998416781372/1332212773370990623/1332213090296659968',
    'priesthood & women' : 'https://discord.com/channels/974038998416781372/1332212773370990623/1332213545860989019',
    'mary typology' : 'https://discord.com/channels/974038998416781372/1332212773370990623/1332213618250350654',
    'tradition' : 'https://discord.com/channels/974038998416781372/1332212773370990623/1332213678187090050',
    'icon veneration' : 'https://discord.com/channels/974038998416781372/1332212773370990623/1332213987231666226',
    'real presence' : 'https://discord.com/channels/974038998416781372/1332212773370990623/1344863346926682216',
    'passions of christ contra-islam' : 'https://discord.com/channels/974038998416781372/1332214698892066887/1332214702838648902',
    'infinite regress argument' : 'https://discord.com/channels/974038998416781372/1332214698892066887/1332215253177466880',
    'divinity of christ in john' : 'https://discord.com/channels/974038998416781372/1332214698892066887/1332217618551279738',
    'list' : '## Available FAQs:\n- Eucharistic Adoration\n- The Problem of Evil\n- Theosis\n- Hell\n- Unbaptized Infants\n- Fallen Angels\n- Loved Ones in Hell\n- Scriptural Arguments for Miaphysis\n- Definitions of *Prosopon*\n- Did Christ Fear Death?\n- Theosis Contra-Protestantism\n- Intercession of the Saints\n- Women & The Priesthood\n- Typology of St. Mary\n- Sacred Tradition\n- Icon Veneration\n- Real Presence\n- The Passions of Christ Contra-Islam\n- Infinite Regress Argument\n- Divinity of Christ in John'
}

# discord intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# setup bot command prefixes
bot = commands.Bot(command_prefix='>', intents=intents)

# slash command definitions
@app_commands.command(name='ping', description='Pings Bot to ensure it is working')
async def ping_bot(interaction):
    await interaction.response.send_message(f'Pong!\nLatency: **{bot.latency * 1000}**ms')
# end def ping_bot

@app_commands.command(name='faq', description='Links to certain FAQs')
async def faq(interaction, question : str):
    try:
        if question.lower() != 'list':
            await interaction.response.send_message(f'FAQ on {question.title()} -> {options[question]}')
        else:
            await interaction.response.send_message(options[question])
    # end if/else block
    except Exception as e:
        await interaction.response.send_message('Invalid Input - Please Try Again')
  # end try/except block
# end def faq

@faq.autocomplete('question')
async def faq_autocomplete(interaction, curr : str) -> List[app_commands.Choice[str]]:
    questions = options.keys()
    return [app_commands.Choice(name=question, value=question) for question in questions if curr.lower() in question.lower()]
# end def faq_autocomplete
    
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
            await after.channel.send(f'<@{after.author.id}> tried to be sneaky and edit his message to ping Staff (I am always two steps ahead)')
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
