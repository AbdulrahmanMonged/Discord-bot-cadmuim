import discord
from discord.ext import commands
import requests
from discord import Embed
import random
from urllib.parse import urlparse
import psycopg
import asyncio
import os


TENOR_API_KEY = os.getenv("TENOR_API_KEY")

DB_URI = os.getenv("DB_URI")
db_uri = urlparse(DB_URI)
host = db_uri.hostname
database = db_uri.path[1:]
user = db_uri.username
password = db_uri.password
port= db_uri.port


class Interactions(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        async with await psycopg.AsyncConnection.connect(host=host, dbname=database, user=user, password=password, port=port) as db:
                    async with db.cursor() as cursor:
                        await cursor.execute("""CREATE TABLE IF NOT EXISTS INTERACTIONS(
            USER1_ID BIGINT NOT NULL,
            USER2_ID BIGINT NOT NULL,
            NUM_KISSES BIGINT,
            NUM_HUGS BIGINT,
            NUM_CUDDLES BIGINT,
            NUM_SLAPS BIGINT,
            NUM_PATS BIGINT,
            NUM_LICKS BIGINT)""")
                        
                  
    @commands.command(description="kisses a member")
    async def kiss(self, ctx, member: discord.Member, *):
        async with await psycopg.AsyncConnection.connect(host=host, dbname=database, user=user, password=password, port=port) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT count(*) FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                db_result = await cursor.fetchone()
                if db_result[0] == 0:
                    await cursor.execute(f"INSERT INTO INTERACTIONS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ctx.author.id, member.id, 0, 0, 0, 0, 0, 0,))
                await db.commit()
                await cursor.execute("SELECT NUM_KISSES FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                results = await cursor.fetchone()
                kisses = results[0] + 1
                await cursor.execute("UPDATE INTERACTIONS set NUM_KISSES = NUM_KISSES + 1 where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                await db.commit()
        apikey = TENOR_API_KEY
        lmt = 20
        ckey = "my_test_app"  
        search_term = "anime kiss gif"
        r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))
        random_data = random.choice(r.json()["results"])
        img = random_data["media_formats"]["gif"]["url"]
        embed = Embed(title=f"{ctx.author.name} kisses {member.name} !", color=ctx.author.color, timestamp=ctx.message.created_at)
        embed.set_image(url=img)
        if ctx.author.avatar != None:
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        else:
            embed.set_author(name=ctx.author.name)
        embed.set_footer(text=f"That's {kisses} kisses !")
        await ctx.send(embed=embed)
        
        
    @commands.command(description="hugs a member")
    async def hug(self, ctx, *, member: discord.Member):
        async with await psycopg.AsyncConnection.connect(host=host, dbname=database, user=user, password=password, port=port) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT count(*) FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                db_result = await cursor.fetchone()
                if db_result[0] == 0:
                    await cursor.execute(f"INSERT INTO INTERACTIONS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ctx.author.id, member.id, 0, 0, 0, 0, 0, 0,))
                await db.commit()
                await cursor.execute("SELECT NUM_HUGS FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                results = await cursor.fetchone()
                hugs = results[0] + 1
                await cursor.execute("UPDATE INTERACTIONS set NUM_HUGS = NUM_HUGS + 1 where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                await db.commit()
        apikey = TENOR_API_KEY
        lmt = 20
        ckey = "my_test_app"  
        search_term = "anime hug gif"
        r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))
        random_data = random.choice(r.json()["results"])
        img = random_data["media_formats"]["gif"]["url"]
        embed = Embed(title=f"{ctx.author.name} hugs {member.name} !", colour=ctx.author.color, timestamp=ctx.message.created_at)
        embed.set_image(url=img)
        if ctx.author.avatar != None:
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        else:
            embed.set_author(name=ctx.author.name)
        embed.set_footer(text=f"That's {hugs} hugs !")
        await ctx.send(embed=embed)
        
    @commands.command(description="cuddles a member")
    async def cuddle(self, ctx, *, member: discord.Member):
        async with await psycopg.AsyncConnection.connect(host=host, dbname=database, user=user, password=password, port=port) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT count(*) FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                db_result = await cursor.fetchone()
                if db_result[0] == 0:
                    await cursor.execute(f"INSERT INTO INTERACTIONS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ctx.author.id, member.id, 0, 0, 0, 0, 0, 0,))
                await db.commit()
                await cursor.execute("SELECT NUM_CUDDLES FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                results = await cursor.fetchone()
                cuddles = results[0] + 1
                await cursor.execute("UPDATE INTERACTIONS set NUM_CUDDLES = NUM_CUDDLES + 1 where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                await db.commit()
        apikey = TENOR_API_KEY
        lmt = 20
        ckey = "my_test_app"  
        search_term = "anime cuddle gif"
        r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))
        random_data = random.choice(r.json()["results"])
        img = random_data["media_formats"]["gif"]["url"]
        embed = Embed(title=f"{ctx.author.name} cuddles {member.name} !", colour=ctx.author.color, timestamp=ctx.message.created_at)
        embed.set_image(url=img)
        if ctx.author.avatar != None:
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        else:
            embed.set_author(name=ctx.author.name)
        embed.set_footer(text=f"That's {cuddles} cuddles !")
        await ctx.send(embed=embed)
        
    @commands.command(description="slaps a member")
    async def slap(self, ctx, *, member: discord.Member):
        async with await psycopg.AsyncConnection.connect(host=host, dbname=database, user=user, password=password, port=port) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT count(*) FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                db_result = await cursor.fetchone()
                if db_result[0] == 0:
                    await cursor.execute(f"INSERT INTO INTERACTIONS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ctx.author.id, member.id, 0, 0, 0, 0, 0, 0,))
                await db.commit()
                await cursor.execute("SELECT NUM_SLAPS FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                results = await cursor.fetchone()
                slaps = results[0] + 1
                await cursor.execute("UPDATE INTERACTIONS set NUM_SLAPS = NUM_SLAPS + 1 where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                await db.commit()
        apikey = TENOR_API_KEY
        lmt = 20
        ckey = "my_test_app"  
        search_term = "anime slap gif"
        r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))
        random_data = random.choice(r.json()["results"])
        img = random_data["media_formats"]["gif"]["url"]
        embed = Embed(title=f"{ctx.author.name} slaps {member.name} !", colour=ctx.author.color, timestamp=ctx.message.created_at)
        embed.set_image(url=img)
        if ctx.author.avatar != None:
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        else:
            embed.set_author(name=ctx.author.name)
        embed.set_footer(text=f"That's {slaps} slaps !")
        await ctx.send(embed=embed)
    
    @commands.command(description="pat a member")
    async def pat(self, ctx, *, member: discord.Member):
        async with await psycopg.AsyncConnection.connect(host=host, dbname=database, user=user, password=password, port=port) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT count(*) FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                db_result = await cursor.fetchone()
                if db_result[0] == 0:
                    await cursor.execute(f"INSERT INTO INTERACTIONS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ctx.author.id, member.id, 0, 0, 0, 0, 0, 0,))
                await db.commit()
                await cursor.execute("SELECT NUM_PATS FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                results = await cursor.fetchone()
                pats = results[0] + 1
                await cursor.execute("UPDATE INTERACTIONS set NUM_PATS = NUM_PATS + 1 where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                await db.commit()
        apikey = TENOR_API_KEY
        lmt = 20
        ckey = "my_test_app"  
        search_term = "anime pat gif"
        r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))
        random_data = random.choice(r.json()["results"])
        img = random_data["media_formats"]["gif"]["url"]
        embed = Embed(title=f"{ctx.author.name} pats {member.name} !", colour=ctx.author.color, timestamp=ctx.message.created_at)
        embed.set_image(url=img)
        if ctx.author.avatar != None:
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        else:
            embed.set_author(name=ctx.author.name)
        embed.set_footer(text=f"That's {pats} pats !")
        await ctx.send(embed=embed)
        
    @commands.command(description="licks a member")
    async def lick(self, ctx, *, member: discord.Member):
        async with await psycopg.AsyncConnection.connect(host=host, dbname=database, user=user, password=password, port=port) as db:
            async with db.cursor() as cursor:
                await cursor.execute("SELECT count(*) FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                db_result = await cursor.fetchone()
                if db_result[0] == 0:
                    await cursor.execute(f"INSERT INTO INTERACTIONS VALUES (%s, %s, %s, %s, %s, %s, %s, %s)", (ctx.author.id, member.id, 0, 0, 0, 0, 0, 0,))
                await db.commit()
                await cursor.execute("SELECT NUM_LICKS FROM INTERACTIONS where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                results = await cursor.fetchone()
                licks = results[0] + 1
                await cursor.execute("UPDATE INTERACTIONS set NUM_LICKS = NUM_LICKS + 1 where USER1_ID = %s and USER2_ID = %s", (ctx.author.id, member.id))
                await db.commit()
        apikey = TENOR_API_KEY
        lmt = 20
        ckey = "my_test_app"  
        search_term = "anime lick someone gif"
        r = requests.get("https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=%s" % (search_term, apikey, ckey,  lmt))
        random_data = random.choice(r.json()["results"])
        img = random_data["media_formats"]["gif"]["url"]
        embed = Embed(title=f"{ctx.author.name} licks {member.name} !", colour=ctx.author.color, timestamp=ctx.message.created_at)
        embed.set_image(url=img)
        if ctx.author.avatar != None:
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar)
        else:
            embed.set_author(name=ctx.author.name)
        embed.set_footer(text=f"That's {licks} licks !")
        await ctx.send(embed=embed)
    
    ########################################## ERROR SECTION ###############################
    @kiss.error
    async def kiss_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = Embed(title="ERROR!", colour=ctx.author.color, timestamp=ctx.message.created_at)
            embed.add_field(name="KISS ERROR", value="Please mention a specific member to kiss them !")
            await ctx.send(embed=embed)
            

    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = Embed(title="ERROR!", colour=ctx.author.color, timestamp=ctx.message.created_at)
            embed.add_field(name="HUG ERROR", value="Please mention a specific member to hug them !")
            await ctx.send(embed=embed)

    @cuddle.error
    async def cuddle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = Embed(title="ERROR!", colour=ctx.author.color, timestamp=ctx.message.created_at)
            embed.add_field(name="CUDDLE ERROR!", value="Please mention a specific member to cuddle them !")
            await ctx.send(embed=embed)

    @slap.error
    async def slep_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = Embed(title="ERROR!", colour=ctx.author.color, timestamp=ctx.message.created_at)
            embed.add_field(name="SLAP ERROR!", value="Please mention a specific member to slep them !")
            await ctx.send(embed=embed)
            
    @pat.error
    async def pat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = Embed(title="ERROR!", colour=ctx.author.color, timestamp=ctx.message.created_at)
            embed.add_field(name="PAT ERROR!", value="Please mention a specific member to pat them !")
            await ctx.send(embed=embed)
    
    @lick.error
    async def lick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = Embed(title="ERROR!", colour=ctx.author.color, timestamp=ctx.message.created_at)
            embed.add_field(name="LICK ERROR!", value="Please mention a specific member to lick them !")
            await ctx.send(embed=embed)
            
    #################################################
def setup(bot):
    bot.add_cog(Interactions(bot)) 
