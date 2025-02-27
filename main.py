import discord
from discord import app_commands

canal = "📱mychapter"

class MeuPrimeiroBot(discord.Client):
    def __init__(self):
        intents = discord.Intents.all()
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)
        self.canal_permitido_id = None

    async def setup_hook(self):
        await self.tree.sync()

    async def on_ready(self):
        print(f"O bot funcionou {self.user}")

        for guild in self.guilds:  # Itera sobre os servidores onde o bot está
            for channel in guild.text_channels:  # Procura nos canais de texto
                if channel.name == canal:
                    self.canal_permitido_id = channel.id
                    print(f"Reações ativadas no canal: {channel.name} (ID: {channel.id})")
                    break

    async def on_message(self, message):
        if self.canal_permitido_id is None or message.channel.id != self.canal_permitido_id:
            return  

    # Evita que o bot reaja às próprias mensagens
        if message.author == self.user:
            return 
            
        try:
            await message.add_reaction("❤️")  # Reação automática em todas as mensagens
            await message.add_reaction("🔁")
        except discord.errors.Forbidden:
            print("O bot não tem permissão para adicionar reações!")

bot = MeuPrimeiroBot()

@bot.tree.command(name="olá-mundo", description="Primeiro Bot")
async def olamundo(interaction: discord.Interaction):
    await interaction.response.send_message(f"Olá {interaction.user.mention}")

import os
bot.run(os.getenv("TOKEN"))
