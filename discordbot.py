from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot('$')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def split(ctx, num: int, args):
    sp = args.split(" ")
    filtered = filter(lambda str: str != ' ', sp)
    ls = list(filtered)
    namelist = random.sample(ls, len(ls))
    result = [namelist[i::num] for i in range(num)]
    await ctx.send(result)


@bot.command()
async def bear(ctx):
    await ctx.send(":bear:")


bot.run(token)
