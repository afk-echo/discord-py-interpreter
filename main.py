import discord
import sys, os
from discord.ext import commands
from ConsoleToStr import ConsoleToStrConverter

command_prefix = "p."  # change this to a prefix of your choice
# creates a Bot with command prefix p. - can be changed to whatever you like.
bot = commands.Bot(command_prefix=command_prefix)
 
# Actual bot code starts here.

# Prints the bot's username when the bot is ready to use.
@bot.event
async def on_ready():
    print(f"Bot {bot.user.name}#{bot.user.discriminator} logged in!")

# The main function that allows you to run the code fed by a user.
@bot.command()
async def run(ctx):
    '''
    Input format for the code:
    
    <prefix>.run ```python
     --enter code here--
    ```
    '''
    conv = ConsoleToStrConverter() # start capturing console outputs
    code_to_be_exec = ctx.message.content.lstrip(f"{command_prefix}run").lstrip(" ```python").rstrip("```")
    code_to_be_exec.replace("os.remove","forbidden_command=")
    conv.start()
    exec(code_to_be_exec)
    result = conv.stop()
    await ctx.send(f"Result is: ```\n{result}```")
@run.error
async def run_error(ctx, error):
    '''
    Returns the errors raised by the bot as a whole(including the ones raised by the user's code.)
    '''
    await ctx.send(f"```{str(error)}```")

@bot.command()
async def files(ctx):
    '''
    Returns all the files stored in the bot's working directory.
    '''
    finalstr = ""
    for i in os.listdir():
        finalstr += i + "\n"
    await ctx.send(f"```All files in the main directory are:\n{finalstr}```")

@bot.command()
async def remove(ctx, file):
    '''
    Removes a file from the bot's working directory.
    '''
    if file in os.listdir():
        os.remove(file)
    else:
        await ctx.send("The file was not found in the current directory.")

bot.run('<ENTER TOKEN HERE>')
