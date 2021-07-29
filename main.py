import discord
import sys, os
from discord.ext import commands
from ConsoleToStr import ConsoleToStrConverter

# creates a Bot with command prefix p. - can be changed to whatever you like.
bot = commands.Bot(command_prefix="p.")

# A helper function for execution of the code. Helps in making the code a bit more modular.
def run_in_diff_console(code):
    
    '''
    A helper function that helps execute the code given as an argument to the bot.
    '''
    
    # generates 2 files - tempcode.py and output.txt, from where the code fed by the user will be executed and stored respectively.
    with open("tempcode.py","w") as f:
        f.write("from ConsoleToStr import ConsoleToStrConverter\n")
        f.write("conv = ConsoleToStrConverter()\n")
        f.write("conv.start()\n")
        f.write(code)
        f.write("result = conv.stop()\n")
        f.write("""
with open('output.txt','w') as f:
    f.write(result)
""")
    
    os.system("python tempcode.py")
    result = ""
    
    with open("output.txt","r") as f:
        line = " "
        while line:
            line = f.readline()
            result += line
    return result
 
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
    code_to_be_exec = ctx.message.content.lstrip("p.run").lstrip(" ```python").rstrip("```")
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
