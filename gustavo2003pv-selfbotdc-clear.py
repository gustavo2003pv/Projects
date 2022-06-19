from colorama import Fore, init
from time import sleep
from discord.ext import commands
import os

init()
print(f'{Fore.LIGHTCYAN_EX} GUSTAVO2003PV CLEAR 3.0')

token = str(input('''
            TOKEN
-> '''))

client = commands.Bot(command_prefix="!", self_bot=True)

@client.event
async def on_ready():
    clear = lambda: os.system('cls')
    clear()
    print(f'{Fore.LIGHTGREEN_EX} GUSTAVO2003PV CLEAR 3.0')
    print(f'{Fore.LIGHTGREEN_EX} USE: !clear to delete all your messages')


@client.command()
async def clear(ctx, limit: int = None):
    passed = 0
    failed = 0
    async for msg in ctx.message.channel.history(limit=limit):
        if msg.author.id == client.user.id:
            try:
                await msg.delete()
                sleep(.25)
                passed += 1
            except:
                failed += 1
    print(
        f"{Fore.LIGHTGREEN_EX}It was excluded {passed} messages, and {Fore.LIGHTRED_EX}{failed} {Fore.LIGHTGREEN_EX} error.")


try:
    client.run(token.replace("\"", ""), bot=False)
except token.errors.LoginFailure:
    clear()
    print(Fore.LIGHTRED_EX +'Invalid token!')
    quit(0)

client.run(token, bot=False)
