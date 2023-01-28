from discord.ext import commands
import discord
import requests

class APIS(commands.Cog):
    def __init__(self, client):
        self.client = client
   
    @commands.command()
    async def pogoda(self, ctx, miejsce, lang="pl"):
            lang = lang.lower()
            response = requests.get(f'http://api.weatherapi.com/v1/current.json?key=bc9d18e03bbf41f1912164725232801&q={miejsce}&lang={lang}&aqi=no')
            data = response.json()
            country = data['location']["country"]
            state = data['location']['name']
            celsius = data['current']['temp_c']
            time = data["location"]['localtime']
            behavior = data['current']['condition']['text']
            celsius_raw = int(celsius)
            if celsius<=15:
                recommend = "Ubierz sie ciepło!"
            if lang=="ang":
                recommend = "Wear yourself cosy"
            if celsius>15 and celsius<20:
                recommend = "Ubierz bluzę!"
            if lang=="ang":
                recommend = "Wear a hoodie"
            if celsius>20:
                recommend = "Ubierz koszulke"
            if lang=="ang":
                recommend="Wear a T-shirt"
            if lang=="pl":
                lang_cou="Kraj:"
                lang_city="Miasto:"
                lang_cel="Stopnie:"
                lang_time="Godzina:"
                lang_rec="Zalecenia:"
                lang_weather="Pogoda:"
            if lang=="ang":
                lang_cou="Country:"
                lang_city="City:"
                lang_cel="Degrees:"
                lang_time="Time:"
                lang_rec="Recommendation:"
                lang_weather="Weather:"
            embed=discord.Embed(title=f'Pogoda w {miejsce}', description="_ _")
            embed.add_field(name=lang_cou, value=country, inline=True)
            embed.add_field(name=lang_city, value=state, inline=True)
            embed.add_field(name=lang_cel, value=celsius, inline=True)
            embed.add_field(name=lang_time, value=time[11:16], inline=True)
            embed.add_field(name=lang_rec,value=recommend, inline=False)
            embed.add_field(name=lang_weather, value=behavior, inline=False)
            await ctx.send(embed=embed)
            print(data)     

async def setup(client):
    await client.add_cog(APIS(client))