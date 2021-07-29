# discord-py-interpreter

The source for a Discord bot script that, while running, can take python code from within a Discord channel, execute it, and return the output back on the same channel.

## Pre-requisites

* A version of Python 3.x
* discord.py - Easiest way to install is by running `pip install discord` in a terminal.
* ConsoleToStr.py - Can be obtained from [here](https://github.com/afk-echo/ConsoleToStr).

## Usage

1. Grab the latest source code archive(.zip) from [here](https://github.com/afk-echo/discord-py-interpreter/releases).
2. Extract the file into a folder of your choice on your machine.
3. Open `main.py` with a text editor and change the value of `command_prefix` to a prefix of your choice. (Default is `p.`)
4. Run main.py. (can be run by simply double clicking the file)

## Commands

1. `run`: Runs the code that is provided to the bot from a message.
Usage of run: 
````
<prefix>run ```python
<Enter code here>
```
````
