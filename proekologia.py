import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def ekologia(ctx):
    await ctx.send(f'Jak dorośli mogą ograniczyć ilość odpadów wytwarzanych w domu:')
    await ctx.send(f'1. Recykling - segregowanie odpadów, np. plastik, papier, szkło itd.')
    await ctx.send(f'2. oszczędzanie - redukcja zużycia energii i wody')
    await ctx.send(f'3. spalanie paliwa - założenie energii fotowoltanicznej,częstsze używanie komunikacji miejskiej lub jeżdżenie rowerem itp.')
    await ctx.send(f'4. kompostowanie - Rozważenie kompostowania odpadów, np resztki jedzenia, kawałki warzyw i owoców.')
    await ctx.send(f'5. Zero waste w kuchni - unikanie jednorazowych przedmiotów kuchennych, np folia spożywcza lub woreczki na śmieci.')
    await ctx.send(f'6. Świadome przygotowanie jedzenia - planowanie posiłków żeby nie marnować jedzenia, a resztki zostawiać na kolejne dania.')
