"""Simple Discord Bot for Using TeX/LaTeX in Discord, needs a modern Tex Distribution to run.
I recommend using this: https://miktex.org/download and restarting the System afterwards to correctly add it to PATH"""
import discord
import sympy
import time
import os
TOKEN = "TOKEN Einfügen"
Command = ";LaTeX"

print("Started")

err = "No Error occurred so far!"


class Bot(discord.Client):
    async def on_ready(self):
        print("online: " + str(self))

    async def on_message(self, message):
        curr_time = time.perf_counter()
        global err
        if message.content.lower().startswith(Command.lower()):
            try:
                sympy.preview(message.content[len(Command) + 1:], viewer="file", filename=f"rendered-{curr_time}.png")
                await message.channel.send(file=discord.File(f"rendered-{curr_time}.png"))
                time.sleep(2)
                os.remove(f"rendered-{curr_time}.png")
            except RuntimeError as e:
                print(e)
                err = e
                await message.channel.send("An Error during the LaTeX Rendering accoured" +
                                           ", if you want to see the Error Type 'y' otherwise irgnore this message.")

        elif message.content.lower() == "y":
            char_count = 0
            curr_msg = ""
            for char in str(err):

                curr_msg = curr_msg + char
                char_count += 1
                if char_count >= 1999:
                    await message.channel.send(curr_msg)
                    char_count = 0
                    curr_msg = ""
            await message.channel.send(curr_msg)


Client = Bot()
Client.run(TOKEN)
