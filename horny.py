import discord
import asyncio
 
discord.Intents(voice_states = True)

class MyClient(discord.Client):
    async def on_ready(self):
        print("Logged on as {0}!".format(self.user))
        # print(self.get_all_channels())

    async def on_message(self, message):
        print("Message from {0.author}: {0.content}".format(message))
        if message.author == self.user:
            return

        if message.content == "ping":
            await message.channel.send("pong", tts = True)

    async def on_voice_state_update(self, member, before, after):
        if after.channel.id == 763999136697548813 and member.id != 765436933295833089:
            print("User joined horny jail")
            channel = client.get_channel(651412560792518689)
            await channel.send("Go to horny jail. BONK", tts = True)
            channel = client.get_channel(763999136697548813)
            vc = await channel.connect()
            vc.stop()
            vc.play(discord.FFmpegPCMAudio(executable="C:/Users/Nasty/Desktop/ffmpeg-2020-10-11-git-7ea4bcff7b-full_build/bin/ffmpeg.exe", source = "henta-girl.mp3"))
            while vc.is_playing():
                await asyncio.sleep(1)
            vc.stop()
            await vc.disconnect()

client = MyClient()
client.run("NzY1NDM2OTMzMjk1ODMzMDg5.X4Uysg.T3d8oM6WyyQC5sGd-EZUpakL_d8")


