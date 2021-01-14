import config
import discord
from discord.ext import commands
import random
import tokens
import time

client = commands.Bot(command_prefix = config.prefix)

@client.event
async def on_ready():
    print("Client ready.")

if config.messageOnJoin == True:
    @client.event
    async def on_member_join(member):
        print(f'{member} ' + config.onMemberJoin)

if config.messageOnRemove == True:
    @client.event
    async def on_member_remove(member):
        print(f'{member} ' + config.onMemberRemove)

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases = ["8ball", "8Ball"])
async def _8Ball(ctx, *, question):
    responses = ["Certainly!", "Absolutely.", "Without a doubt.", "Yes. For definite.", "You can rely on it.", "Probably", "Seems good to me.", "yes.", "meh, more like a yes though.", "Response hazy. Ask again.", "not rn, ask later.", "better not tell you now.", "Can't predict now", "Ok, FOCUS, and ask again.", "Don't count on it", "My reply is no.", "my sources say no.", "Doesn't look too good to me.", "more like a no..."]
    await ctx.send(f"Question: {question} \nAnswer: {random.choice(responses)}")

@client.command()
async def spam(ctx, amount = 10):
    time.sleep(2)
    for index in range(0, amount):
        await ctx.send(f"Spam")

@client.command(aliases = ["surprise", "rr"])
async def rickroll(ctx):
    rr = open("tiger/rickroll.txt", "r")
    await ctx.send(f"Here goes. \nReady?")
    time.sleep(2)
    for word in rr:
        await ctx.send(word)

@client.command()
async def clear(ctx, amount = 5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def quit(ctx):
    await ctx.send("tiger is going offline.")
    quit()

client.run(tokens.token)