import discord
import sys, os
from discord.ext import commands
from ConsoleToStr import ConsoleToStrConverter

bot = commands.Bot(command_prefix="p.")
conv = ConsoleToStrConverter()

@bot.event
async def on_ready():
    print(f"Bot {bot.user.name}#{bot.user.discriminator} logged in!")

@bot.command()
async def run(ctx):
    code_to_be_exec = ctx.message.content.lstrip("p.run").lstrip(" ```python").rstrip("```")
    code_to_be_exec.replace("os.remove","forbidden_command=")
    conv.start()
    exec(code_to_be_exec)
    result = conv.stop()
    await ctx.send(f"Result is: ```\n{result}```")
@run.error
async def run_error(ctx, error):
    await ctx.send(f"```{str(error)}```")

@bot.command()
async def files(ctx):
    finalstr = ""
    for i in os.listdir():
        finalstr += i + "\n"
    await ctx.send(f"```All files in the main directory are:\n{finalstr}```")

@bot.command()
async def remove(ctx, file):
    if file in os.listdir():
        os.remove(file)
    else:
        await ctx.send("The file was not found in the current directory.")

bot.run('<ENTER TOKEN HERE>')
