import discord
from discord.ext import commands
import instaloader

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def resources(ctx):
    await ctx.send("Main resource : [Main Resource](https://drive.google.com/drive/folders/1kG84_tEPph4bEQqu2GnYx84xUzbdFGLw)")

@bot.command()
async def history(ctx):
    await ctx.send("Ultimate AP history doc : [(]Ultimate AP History Doc](https://drive.google.com/file/d/1SJmA5dc_2lzkNhiBR_pevBQPOn2r9Myw/view?usp=sharing)")

@bot.command()
async def ultimate(ctx):
    await ctx.send("Ultimate AP doc : [Ultimate AP Doc](https://drive.google.com/file/d/1jyXdoHBQjI9HkNU7_IV48HMtGyuM5AIp/view?usp=sharing)")

@bot.command()
async def books(ctx):
    await ctx.send("[Books](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)")

@bot.command()
async def bio(ctx):
    await ctx.send("AP bio:\n"
                   "- [AP Bio Review](https://docs.google.com/document/d/17_9ZhQVCf61bRlch_e0gdQJzWz1k2doi7EcuLXEnyps/edit?usp=sharing)\n"
                   "- [AP Bio Study Guide](https://drive.google.com/file/d/1vFCZ1NlapvePVZlQwnOFC-P-WWWG9x02/view?usp=sharing)\n"
                   "- [AP Bio Weebly](https://apbiopenguins.weebly.com/)\n"
                   "- [AP Books Recommended By yours truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)\n"
                   "- [AP Bio FRQ'S](https://apcentral.collegeboard.org/courses/ap-biology/exam/past-exam-questions)\n")


@bot.command()
async def followers(ctx):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, "seoul.pearson")
        await ctx.send(f"seoul.pearson has {profile.followers:,} followers.")
    except Exception as e:
        await ctx.send(f"Couldn't fetch follower count. Error: {e}")

bot.run("YOUR_BOT_TOKEN_HERE")
