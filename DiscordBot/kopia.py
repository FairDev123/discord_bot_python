
# [MODULES IMPORT]
import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, guild_only
from discord.utils import get
import sqlite3
import random
import math
import time
import requests
import json
from mojang import MojangAPI
from replit import db
from keep_alive import keep_alive

num = 1

data = {"flowers":["Rose","Violet","Poppy"], "meals":["Burger","Spaghetti","Lasagne"], "names":["Mick","Alex","Max"]}

# [DATABASE BASE]

con = sqlite3.connect("users.db")
cur = con.cursor()

try:
  create_table = "CREATE TABLE users(id, user, coins, gems)"
  cur.execute(create_table)
  print("Utworzono tablice 'users'")
except:
  pass

# [IMPORTANT THINGS]
walters = ["https://imgur.com/c2dqZkc","https://imgur.com/ZZX6plM","https://imgur.com/IFZmwI2","https://imgur.com/skZPRSE"]

diary = """
__**Klasa 1A**__

>>> `          UCZNIOWIE           `

**1**. Błaszczyk Oskar
**2**. Brom Kamil
**3**. Cichoń Marcel
**4**. Giza Klaudiusz
**5**. Guzek Łukasz
**6**. Hordejuk Jakub
**7**. Jęda Jakub
**8**. Josef Gracjan
**9**. Juranek Bartosz
**10**. Kapler Jakub
**11**. Klama Norbert
**12**. Koliński Igor
**13**. Koronkiwicz Kacper
**14**. Korpacki Mateusz
**15**. Kuraj Alan
**16**. Kurant Miłosz
**17**. Kuś Kacper
**18**. Lazarewicz Przemysław
**19**. Łoś Oliwier
**20**. Mikołajczyk Ksawier
**21**. Montak Mikołaj
**22**. Musiał Przemysław
**23**. Nawrocki Bartłomiej
**24**. Nowak Igor
**25**. Orłowski Arkadiusz
**26**. Przybysz Dawid
**27**. Rusin Wiktor
**28**. Rusiński Nikolas
**28**. Stefański Oskar
**29**. Wisielewski Oliwier
**30**. Wilczak Jastin
"""

#dziennik_image ="https://imgur.com/XXdjEGm"

finalper = False
tab = ["Kacper","Marcin","Łukasz"]

intents = discord.Intents().all()
client = commands.Bot(command_prefix='?', intents=intents)
intents.members = True

# [BOT EVENTS]

                return
@client.event
async def on_member_join(member):
    channel = client.get_channel(1024375951548760227)
    await channel.send(f'{member.mention} właśnie dołączył do drużyny!')

@client.event
async def on_member_leave(member):
    channel = client.get_channel(1024375951548760227)
    await member.send("ok")

 
  
@client.event
async def on_ready():
  channel = client.get_channel(1025734128303345734)
  channel2 = client.get_channel(973273824659382276)
  await client.change_presence(activity=discord.Game(name="?pomoc"))
  print("Bot został włączony")
  embed=discord.Embed(title="FairBOT Logs",description="Operacja: Bot został poprawnie włączony",color=0x00ff00)

#@client.event
#async def on_message(ctx):
    #if ctx.content.startswith('Gej'):
       #channel = ctx.channel
       #await channel.send("Sam jesteś gejem")
      
#@client.event
#async def on_command_error(ctx, error):
    #if isinstance(error, commands.MissingRequiredArgument):
        #await ctx.send('Zabrakło argumentu :rolling_eyes:.')
    #if isinstance(error, commands.MissingPermissions):
        #channel = client.get_channel(1025734128303345734)
        #await ctx.send(ctx.author.mention+" nie masz uprawnień 💀")
        #embed=discord.Embed(title="FairBOT Logs", description=f'Operacja: {ctx.author.mention} próbował wpisać komendę administratora')
        #embed.set_thumbnail(url="https://i.imgur.com/CDVo1v9.png")
        #await channel.send(embed=embed)

      #embed=discord.Embed(title="FairBOT Logs", description="Operacja: @zyzz próbował wpisać komendę administratora")
#embed.set_thumbnail(url="https://i.imgur.com/CDVo1v9.png")
#embed.add_field(name="Komenda:", value="?clear 5", inline=False)
#await ctx.send(embed=embed)
      
# [BOT COMMANDS]

@client.command()
async def data_test(ctx, table, index):
    flower = data[table]
    await ctx.send(flower[int(index)-1])

@client.command()
async def head_2d(ctx, nick):
  uuid = MojangAPI.get_uuid(nick)
  site = f'https://mc-heads.net/avatar/{nick}'
  await ctx.send(site)

@client.command()
async def mcprofile(ctx, nick):
  uuid = MojangAPI.get_uuid(nick)
  site = f'https://mc-heads.net/head/{uuid}'
  embed=discord.Embed()
  embed.set_thumbnail(url=site)
  embed.add_field(name=nick, value="_ _", inline=False)
  embed.set_footer(text=f'User uuid: {uuid}')
  await ctx.send(embed=embed)

@client.command()
async def skin_3d(ctx, nick):
  uuid = MojangAPI.get_uuid(nick)
  site = f'https://mc-heads.net/body/{uuid}/left'
  await ctx.send(site)
 #except:
  #await ctx.send("Nie znaleziono takiego miejsca")

@client.command()
async def dziennik(ctx):
    if ctx.channel.id == 1024374980663857242:
     channel = client.get_channel(1024374980663857242)
     await channel.send(diary)
    else:
     channel = client.get_channel(1024374980663857242)
     await channel.send(diary)
     await ctx.send("Ze względów bezpieczeństwa ta wiadomość pojawiła sie w sekcji klasowej")

@client.command()
@has_permissions(administrator=True)
async def adm_dziennik(ctx):
    await ctx.send(dziennik_image)
    await ctx.send(diary)     
@client.command()
async def database_name(ctx): 
    res = cur.execute("SELECT name FROM sqlite_master")
    name = str(res.fetchone())
    await ctx.send(name[2:-3])

@client.command()
async def add_user(ctx, id, user, coins, gems):
    data = (id, user, coins, gems)
    cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?)", (data,))
    con.commit()
    await ctx.send("Dodano")

@client.command()
async def delete(ctx, index):
    cur.execute(f'DELETE FROM currency WHERE rowid=?', (index))
    await ctx.send("Usunięto")
@client.command()
async def check(ctx):
       table_select = "SELECT * FROM users"
       res = cur.execute(table_select)
       records = res.fetchall()
       for row in records:
        await ctx.send(f'Id: {row[0]}')
        await ctx.send(f'User: {row[1]}')
        await ctx.send(f'Coins: {row[2]}')
        await ctx.send(f'Gems: {row[3]}')
        await ctx.send("_ _")

@client.command()
async def check_user(ctx, user):
    table_select = "SELECT * FROM users where user= ?"
    cur.execute(table_select, (user,))
    records = cur.fetchall()
    for row in records:
      await ctx.send(f'User: {row[1]}')
      await ctx.send(f'Coins: {row[2]}')
      await ctx.send(f'Gems: {row[3]}')
@client.command()
async def base(ctx):
     res = cur.execute("SELECT * FROM users")
     base = res.fetchall()
     await ctx.send(base)
  
@client.command()
async def my_acc(ctx):
    table_select = "SELECT * FROM users WHERE user= ?"
    author = ctx.author.mention
    res = cur.execute(table_select, (author,))
    records = res.fetchall()
    if records: 
     for row in records:
      await ctx.send(f'User: {row[1]}')
      await ctx.send(f'Coins: {row[2]}')
      await ctx.send(f'Gems: {row[3]}')
    else:
       await ctx.send("Dodano cię do bazy danych, proszę wpisz **?my_acc** jeszcze raz!")
       insert_com = "INSERT INTO users VALUES(?,?,?,?)"
       data = [1, author, 0, 0]
       cur.executemany(insert_com, (data,))
       con.commit()
      
@client.command()
async def wstawaj(ctx):
  await ctx.send("Wstałem")

@client.command()
async def set_bot_status(ctx, *,status):
    await client.change_presence(activity=discord.Game(name=status))

@client.command()
async def losowa_liczba(ctx):
    await ctx.send(random.randint(0,99))

@client.command()
async def gayrate(ctx, text):
  per = str(random.randint(0,100))+"%"
  embed = discord.Embed(title="Sprawdzamy:",description=text)
  embed.add_field(name="Jest gejem w:",value=per, inline=False)
  await ctx.send(embed=embed)

@client.command()
async def ship(ctx, ship1, ship2):
 if ship1==ship2:
  await ctx.send("Nie możesz tego zrobić pajacu 🤨")
 else:
  per = random.randint(0,100)
  love = str(per) + "%"
  if per<40 or per==40 or per==0:
    desc = "Zimno 🧊"
  if per>40 and per<50:
    desc = "Koleżeńsko 😅"
  if per>50 and per<80:
    desc = "Iskrzy ✨"
  if per>80:
    desc = "Gorąco 🔥"
  embed=discord.Embed(title="Ship:", description= ship1 + " ❤️ " + ship2, color=0xff00ff)
  embed.add_field(name="Poziom miłości:", value=love + " **(" + desc + ")**", inline=False)
  await ctx.send(embed=embed)

@client.command()
@has_permissions(administrator=True)
async def tab_add(ctx, text):
  tab.append(text)
  await ctx.send("Dodano")

@client.command()
@has_permissions(administrator=True)
async def tab_check(ctx):
 try:
  for i in tab:
    time.sleep(1)
    await ctx.send(i)
 except:
   await ctx.send("Nie ma nic na liście")

@client.command()
async def tab_clear(ctx):
    tab.clear()
    await ctx.send("Wyczyszczono")

@client.command()
async def pomoc(ctx):
  embed=discord.Embed(title="Komendy",  
  description="Komendy do bota Fair", 
  color=0x7b00ff)
  embed.add_field(name="?losowa_liczba", value="losuje liczbę", 
  inline=False)
  embed.add_field(name="?siema", value="witasz się z botem", inline=False)
  embed.add_field(name="?ship <osoba> <osoba>",value="sprawdza poziom miłości",inline=False)
  embed.add_field(name="?gayrate <osoba>", value="sprawdza poziom geja", inline=False)
  embed.add_field(name="?change_nick <osoba> <nowy_nick>",value="zmienia nick",inline=False)
  embed.add_field(name="?clear <liczba>", value="wyczyszcza ilość wiadomości", inline=False)
  embed.add_field(name="?walter", value="wysyła Włodzimierza", inline=False)
  embed.set_footer(text="okienko można wywołać za pomocą komendy ?pomoc")
  await ctx.send(embed=embed)

@client.command()
async def siema(ctx):
    siema = ["Dzieńdobry","Yo","Hej","Siema","Cześć","Witam"]
    await ctx.send(random.choice(siema))
                       
@client.command()
@has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, reason=None):
    channel = client.get_channel(1025734128303345734)
    if reason == None:
        await ctx.send(f"Ej {ctx.author.mention}, Musisz dać powód!")
    else:
        messageok = f"Dostałeś bana z {ctx.guild.name} z powodu: {reason}"
        await member.send(messageok)
        await member.ban(reason=reason)
        embed=discord.Embed(title="FairBOT Logs", description="Zbanowanie użytkownika",color=0xff0000)
        embed.set_thumbnail(url="https://static.wikia.nocookie.net/pixel-gun-3d/images/9/9b/Banhammerbig.png/revision/latest?cb=20200728091619")
        embed.add_field(name="Banujący:", value=ctx.author.mention)
        embed.add_field(name="Zbanowany:", value=member.mention)
        await channel.send(embed=embed)

@client.command()
@has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, reason=None):
    channel = client.get_channel(1025734128303345734)
    if reason == None:
        await ctx.send(f"Ej {ctx.author.mention}, Musisz dać powód!")
    else:
        messageok = f"Zostałeś wyrzucony {ctx.guild.name} z powodu: {reason}"
        await member.send(messageok)
        await member.kick(reason=reason)
        embed=discord.Embed(title="FairBOT Logs", description="Operacja: Wyrzucenie użytkownika",color=0xff0000)
        embed.add_field(name="Wyrzucający:", value=ctx.author.mention)
        embed.add_field(name="Wyrzucony:", value=member.mention)
        await channel.send(embed=embed)

@client.command(pass_context = True)
@has_permissions(administrator=True)
async def mute(ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="muted")
        await member.add_roles(role)
        await ctx.send("Dodano rangę")

@client.command(pass_context = True)
@has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member):
        role = discord.utils.get(ctx.guild.roles, name="muted")
        await member.remove_roles(role)
        await ctx.send("Usunięto rangę")
        embed=discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=0xff00f6)
        await bot.say(embed=embed)

@client.command()
@has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name,
                                               member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Odbanowano {user.mention}')
            return

@client.command()                      
async def test(ctx):
    await ctx.send(ctx.author.mention)
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
       user = ban_entry.user
       if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')

@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, number=5):
    channel = client.get_channel(1025734128303345734)
    await ctx.channel.purge(limit=number+1)
    embed = discord.Embed(title="FairBOT Logs", description=f'Operacja: {ctx.author.mention} użył komendy do usuwania wiadomości')
    embed.set_thumbnail(url="https://i.imgur.com/CDVo1v9.png")
    embed.add_field(name="Kanał:", value=ctx.channel.mention)
    embed.add_field(name="Liczba usuniętych wiadomości:", value=number)
    await channel.send(embed=embed)

@client.command()
async def walter(ctx):
    await ctx.send(random.choice(walters))
    await ctx.send("To ja")

@client.command()
async def walter_gallery(ctx):
    for i in walters:
      time.sleep(0.5)
      await ctx.send(i)

keep_alive()
token = "MTAyNDY5NjQxMzg0NzgyMjM0Ng.G17KbU.nheU1zlktLNq2Y5iXbyzlkz3GKhVd9lBPAsPlA"

client.run(token)