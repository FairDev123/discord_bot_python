from discord.ext import commands
from discord.ext.commands import has_permissions
import discord

class Moderation(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    @has_permissions(administrator=True)
    async def ping(self, ctx):
       channel = self.client.get_channel(1025734128303345734)
       await channel.send("pong")

    @commands.Cog.listener()
    async def on_message_delete(self, ctx):
        channel = self.client.get_channel(1025734128303345734)
        if len(ctx.mentions) == 0:
            deleted = discord.Embed(title=f'**FairBOT Logs**', description=f'Operacja: {ctx.author.mention} usunął wiadomość', color=0xff0000, timestamp=ctx.created_at)
            deleted.set_thumbnail(url="https://i.imgur.com/1bbatUP.png")
            deleted.add_field(name="Kanał:", value=ctx.channel.mention)
            deleted.add_field(name="Treść wiadomości", value=ctx.content)
            await channel.send(embed=deleted)
        if len(ctx.mentions) > 0:
            print(ctx.author.name)
            ghostping = discord.Embed(title=f'FairBOT Logs',description=f'Operacja: {ctx.author.mention} usunął wiadomość w której oznaczył użytkownika (Ghost Ping)',color=0xFF0000, timestamp=ctx.created_at)  
            ghostping.add_field(name='**Usunięta wiadomość:**', value=f'{ctx.content}')
            ghostping.set_thumbnail(
                url='https://bot.to/wp-content/uploads/2020/10/anti-ghost-ping_5f7e1433e80c3.png')
            try:
                await ctx.channel.send(embed=ghostping)
            except:
                pass
                try:
                    await ctx.author.send(embed=ghostping)
                except:
                    pass

    @commands.command()
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, number=5):
        channel = self.client.get_channel(1025734128303345734)
        await ctx.channel.purge(limit=number+1)
        embed = discord.Embed(title="FairBOT Logs", description=f'Operacja: {ctx.author.mention} użył komendy do usuwania wiadomości')
        embed.set_thumbnail(url="https://i.imgur.com/CDVo1v9.png")
        embed.add_field(name="Kanał:", value=ctx.channel.mention)
        embed.add_field(name="Liczba usuniętych wiadomości:", value=number)
        await channel.send(embed=embed)

async def setup(client):
    await client.add_cog(Moderation(client))