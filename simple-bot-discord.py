from email import message_from_string
from tkinter import messagebox
import discord
from discord.ext import commands
import random

#Commands:
#Say, Gen, Calc

bot = commands.Bot('!')

@bot.event
async def on_ready():
    print(f'Bot Running!')

#Gen number 0-999
@bot.command(name='gen')
async def send(ctx):
    await ctx.send(f'{ctx.author.name}, number: {random.randint(0,999)} ')

#Calc expression, * ** / // + - %
@bot.command(name='calc')
async def send(ctx, Expression):
    await ctx.send(f'{ctx.author.name}, result: {eval(Expression)} ')

#Say message
@bot.command(name='say')
async def send(ctx, *args):
    await ctx.send (' '.join(args))

bot.run('TOKEN HERE')