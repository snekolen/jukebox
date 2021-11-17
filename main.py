import discord
from discord import voice_client
from discord.embeds import EmptyEmbed
from discord.ext import commands
from discord.utils import get
from finder import findSong, findUrl, TOKEN
from countries import allCountries, countryExists
from info import Info, updateAllT, updateTopT, s, updateRecentS

client = commands.Bot(command_prefix = "+")
client.remove_command("help")

#Organize things into classes (Song and Top) 
#Top points to class to get info about country and decade and takes name/id of server as parameter
#Make a help page

@client.event
async def on_ready():
    print("Bot is ready") #Message prints out to the console when using an IDE

@client.event
async def on_command_error(ctx, error): #Add for CommandNotFound
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Invalid command")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Missing argument")
    elif isinstance(error, commands.BadArgument):
        await ctx.send("Unable to convert between data types")

#Cog class
class Cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

#Pulls up songs and help page (Need to update)
class Menu(commands.Cog):
    @client.command(name = "help")
    async def help(ctx):
        embed = discord.Embed(color = discord.Color.green(), title = "Commands")
        topCountries = "`+top countries`\n Shows the top 3 most searched countries in the server\n"
        topDecades = "`+top decades`\n Shows the top 3 most searched decades in the server\n"
        topSongs = "`+top songs`\n Shows the top 3 most liked songs in the server (react with :heart: to like a song)"
        topText = topCountries + topDecades + topSongs
        embed.add_field(name = "+list", value = "`+list [decade]`\n Sends a list of countries in the world by decade ranging from 1900 to 2020", inline = False)
        embed.add_field(name = "+song", value = "`+song [country] [decade]`\n Sends a song released from the inputted country during the specified decade\n (ex: +song Japan 1980)", inline = False)
        embed.add_field(name = "+top", value = topText)
        await ctx.send(embed = embed)

    #Pulls up list of countries
    @client.command(name = "list") #Pulls up list of countries for each decade
    async def _list(ctx, year: int): 
        clist = []
        try:
            if year < 1900 or year > 2020:
                raise Exception("Year must be between 1900 and 2020")
            elif year % 10 != 0:
                raise Exception("Year must end in 0")
        except Exception as e: #Other exceptions include MissingRequiredArgument and BadArgument
            await ctx.send(e)
        else:
            clist = allCountries(year)

        page1 = discord.Embed(
            title = str(year) + "s Countries (1/" + str(len(clist)) + ")",
            description = clist[0],
            color = discord.Color.blurple()
        )
        page2 = discord.Embed(
            title = str(year) + "s Countries (2/" + str(len(clist)) + ")",
            description = clist[1],
            color = discord.Color.blurple()
        )

        page3 = discord.Embed(
            title = str(year) + "s Countries (3/" + str(len(clist)) + ")",
            description = clist[2],
            color = discord.Color.blurple()
        )

        pages = [page1, page2, page3]

        if len(clist) >= 4:
            page4 = discord.Embed(
                title = str(year) + "s Countries (4/" + str(len(clist)) + ")",
                description = clist[3],
                color = discord.Color.blurple()
            )
            pages.append(page4)
        
        if len(clist) >= 5:
            page5 = discord.Embed(
                title = str(year) + "s Countries (5/" + str(len(clist)) + ")",
                description = clist[4],
                color = discord.Color.blurple()
            )
            pages.append(page5)
        
        if len(clist) >= 6:
            page6 = discord.Embed(
                title = str(year) + "s Countries (6/" + str(len(clist)) + ")",
                description = clist[5],
                color = discord.Color.blurple()
            )
            pages.append(page6)
        
        if len(clist) >= 7:
            page7 = discord.Embed(
                title = str(year) + "s Countries (7/" + str(len(clist)) + ")",
                description = clist[6],
                color = discord.Color.blurple()
            )
            pages.append(page7)

        
        def check(reaction, user):
                return user == ctx.author

        i = 0
        #await ctx.send(embed = pages[0])
        message = await ctx.send(embed = pages[i])
        await message.add_reaction('⏮')
        await message.add_reaction('◀')
        await message.add_reaction('▶')
        await message.add_reaction('⏭')

        while True:
            reaction, user = await client.wait_for("reaction_add", timeout = 60, check = check)
            if str(reaction.emoji) == '⏮':
                i = 0 
            elif str(reaction.emoji) == '◀':
                if i > 0:
                    i -= 1
            elif str(reaction.emoji) == '▶':
                if i < (len(clist)) - 1: 
                    i += 1
            elif str(reaction.emoji) == '⏭':
                i = len(clist) - 1
            
            message1 = await ctx.channel.fetch_message(message.id)
            await message1.edit(embed = pages[i])
            

m = None

@client.command(name = "song", pass_context = True) #Plays music based on command
async def song(ctx, *args): #Args include word(s) in the country's name and year
    country = " ".join(args[0:len(args) - 1])
    year = args[len(args) - 1]
    valid = True
    #s = Songs() #Variable used to access Songs class
    try:
        if len(args) == 1 or args[len(args) - 1].isnumeric() == False: 
            raise Exception("Please re-enter your command in the format '+song [country] [year]'")
        elif int(year) < 1900 or int(year) > 2020:
            raise Exception("Year must be between 1900 and 2020")
        elif int(year) % 10 != 0:
            raise Exception("Year must end in 0")
        elif countryExists(country, int(year)) == False:
            raise Exception(country + " did not exist in the " + str(year)+ "s")
    except Exception as e:
        valid = False
        await ctx.send(e)

    updateAllT(country, year)
    updateTopT(country, year)

    #Finding and playing songs
    if valid == True:
        songDict = findSong(country, int(year))
        songDict = findUrl(songDict)
        imgLink = "https://img.youtube.com/vi/" + songDict["ID"] + "/0.jpg"

        link = "**[" + songDict["Song"] + "](" + songDict["URL"] + ")**"
        embed = discord.Embed(
            color= discord.Colour.orange(),  # or any color you want
            title = "𝄞♫♪♩",
            description = link
        )
        
        embed.add_field(name = "Artist", value = songDict["Artist"], inline = False)
        embed.add_field(name = "Released", value = songDict["Year"], inline = True)
        embed.add_field(name = "Country ", value = country, inline = True)
        embed.set_thumbnail(url = imgLink)

        m = await ctx.send(embed=embed)

        '''
        m = await ctx.channel.fetch_message(message.id)

        reaction = get(m.reactions, emoji = '❤️')
        num_reactions = reaction.count

        updateRecentS(songDict["Song"], songDict["Artist"], 0)
        '''

'''
async def count_react(message):
    def check(message):
        return message.author.id == 899002742989791273
'''
    
    #Use message.channel to get channel
    #899002742989791273
#Create a class to keep track of top countries, decades, and songs
@client.command(name = "top") #Pulls up list of top countries, decades, and songs
async def top(ctx, category):
    name = ctx.message.guild.name
    if category == "terms":
        topList = discord.Embed(
            title = "Top Search Terms in " + name,
            color = discord.Color.red()
        )
        #await ctx.send(topList.title)
        await ctx.send("t")
    elif category == "songs":
        counter = 0
        async for message in ctx.channel.history(limit = 200):
            embeds = message.embeds
            reactions = message.reactions
            for reaction in reactions:
                if str(reaction.emoji) == '❤️':
                    rCount = reaction.count
                    #print(rCount)
            for embed in embeds:
                e = embed.to_dict()
                if "♫" in e["title"]:
                    #print("a")
                    counter += 1
            
        await ctx.send(counter)
    else:
        try:
            raise Exception("Plase re-enter your command in the format '+top [category]', where the only valid terms for [category] are 'terms' and 'songs'")
        except Exception as e:
            await ctx.send(e)

def setup(bot):
    pass #Add classes to Cog

client.run(TOKEN)

