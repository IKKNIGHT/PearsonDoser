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
async def notes(ctx):
    await ctx.send("[Notes](https://drive.google.com/drive/folders/1fxW4qSZWQ84ZNOSWOcBCcO_XENyl2zhh)")

@bot.command()
async def bio(ctx):
    await ctx.send("AP Bio:\n"
                   "- [AP Bio Review](https://docs.google.com/document/d/17_9ZhQVCf61bRlch_e0gdQJzWz1k2doi7EcuLXEnyps/edit?usp=sharing)\n"
                   "- [AP Bio Study Guide](https://drive.google.com/file/d/1vFCZ1NlapvePVZlQwnOFC-P-WWWG9x02/view?usp=sharing)\n"
                   "- [AP Bio Weebly](https://apbiopenguins.weebly.com/)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)\n"
                   "- [AP Bio FRQ'S](https://apcentral.collegeboard.org/courses/ap-biology/exam/past-exam-questions)\n"
                   "- [AP Bio Study Guide Supplements](https://drive.google.com/file/d/1o2BsjfHPkSFzACbHAvHW9M6cs876Qzun/view?usp=sharing)")

@bot.command()
async def calc(ctx):
    await ctx.send("AP Calc:\n"
                   "- [AP Calc Study Guide](https://support.ebsco.com/LEX/AP-Calculus-BC-Study-Guide.pdf)\n"
                   "- [AP Calc Study Guide 2](https://docs.google.com/document/d/1iBpqlLvhZhThJ_OOsgRR27E_aKgJAmmibdkRdVya7rc/edit?usp=sharing)\n"
                   "- [AP Calc Study Guide 3](https://drive.google.com/file/d/1EmMMbltrE8zzaOeaNl9EWziX0x8WSdDS/view)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)\n"
                   "- [AP Calc Review Sheet](https://drive.google.com/file/d/0Bx50M-1D0Q0WNHllRmFDd21VZVk/view?resourcekey=0-0O1JQbsJKKlVQAiObBj1AQ)\n"
                   "- [AP Calc AB FRQ'S](https://apcentral.collegeboard.org/courses/ap-calculus-ab/exam/past-exam-questions)\n"
                   "- [AP Calc BC FRQ'S](https://apcentral.collegeboard.org/courses/ap-calculus-bc/exam/past-exam-questions)")

@bot.command()
async def chem(ctx):
    await ctx.send("AP Chem:\n"
                   "- [AP Chem Review](https://docs.google.com/document/d/1LLFUpQ3Vgzv--MWzW286_Dio-v8n0NfR3KDvWGbqj-Q/edit?usp=sharing)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)\n"
                   "- [AP Chem FRQ'S](https://apcentral.collegeboard.org/courses/ap-chemistry/exam/past-exam-questions)")

@bot.command()
async def compgov(ctx):
    await ctx.send("AP Comp Gov:\n"
                   "- [AP Comp Gov Study Guide](https://drive.google.com/file/d/14uFsIpb_FGg-k07oFiVIOfJUhCItP__W/view?usp=sharing)\n"
                   "- [AP Comp Gov Doc](https://docs.google.com/document/d/1XKNibHnw63Wq-2mHT-P0pMqtKUdfAEJqRuCvjQfpkRE/edit?usp=sharing)\n"
                   "- [AP Comp Gov FRQ'S](https://apcentral.collegeboard.org/courses/ap-comparative-government-and-politics/exam/past-exam-questions)")

@bot.command()
async def csa(ctx):
    await ctx.send("AP CSA:\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)\n"
                   "- [AP CSA Study Guide](https://drive.google.com/file/d/122tDTodwHCudKZeuVRL8aS78SIr5Dfkz/view?usp=sharing)\n"
                   "- [AP CSA CSAwesome](https://runestone.academy/ns/books/published/csawesome2/csawesome2.html)\n"
                   "- [AP CSA CodingBat](https://codingbat.com/java)\n"
                   "- [AP CSA Knowt](https://knowt.com/exams/AP/AP-Computer-Science-A)\n"
                   "- [AP CSA FRQ'S](https://apcentral.collegeboard.org/courses/ap-computer-science-a/exam/past-exam-questions)")

@bot.command()
async def lang(ctx):
    await ctx.send("AP Lang:\n"
                   "- [AP Lang ChatGPT](https://chatgpt.com/)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)\n"
                   "- [AP Lang CoachHallWrites](https://www.youtube.com/@CoachHallWrites/videos)\n"
                   "- [AP Lang FRQ'S](https://apcentral.collegeboard.org/courses/ap-english-language-and-composition/exam/past-exam-questions)")

@bot.command()
async def lit(ctx):
    await ctx.send("AP Lit:\n"
                   "- [AP Lit Study Guide](https://drive.google.com/file/d/1CaZNq2TJiwuGV2MX4pg15T1NV5Px67Vk/view?usp=sharing)\n"
                   "- [AP Lit FRQ'S](https://apcentral.collegeboard.org/courses/ap-english-literature-and-composition/exam/past-exam-questions)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)")

@bot.command()
async def envsci(ctx):
    await ctx.send("AP Env Sci:\n"
                   "- [AP Env Sci Study Guide](https://drive.google.com/file/d/14SSP1sFmKM_uOLXe6qX_eMqxm8-NKLAc/view)\n"
                   "- [AP Env Sci FRQ'S](https://apcentral.collegeboard.org/courses/ap-environmental-science/exam/past-exam-questions)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)")

@bot.command()
async def euro(ctx):
    await ctx.send("AP Euro:\n"
                   "- [Ap Euro Study Guide](https://drive.google.com/file/d/1jjSqlYaba-uqMtjBspy1BoXB8v_dIyn5/view?usp=drive_link)\n"
                   "- [AP Euro FRQ'S](https://apcentral.collegeboard.org/courses/ap-european-history/exam/past-exam-questions)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)")

@bot.command()
async def hgap(ctx):
    await ctx.send("HGAP:\n"
                   "- [HGAP Study Guide](https://drive.google.com/file/d/1hbPV0hWetWQxdrthu38h6qLmEjhKWuQR/view?usp=sharing)\n"
                   "- [HGAP FRQ'S](https://apcentral.collegeboard.org/courses/ap-human-geography/exam/past-exam-questions)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)")

@bot.command()
async def macro(ctx):
    await ctx.send("AP Macro:\n"
                   "- [AP Macro Review Econ](https://www.youtube.com/@ReviewEcon)\n"
                   "- [AP Macro By Jacob Clifford](https://www.youtube.com/channel/UCCQEbqDL8i40d83Au55lYMQ)\n"
                   "- [AP Macro Cheat Sheet](https://lopiccolo.weebly.com/uploads/7/7/7/4/7774746/ap_macro_ultimate_cheat_sheet_key.pdf)\n"
                   "- [AP Macro Study Guide](https://drive.google.com/drive/folders/1fxW4qSZWQ84ZNOSWOcBCcO_XENyl2zhh)\n"
                   "- [AP Macro FRQ'S](https://apcentral.collegeboard.org/courses/ap-macroeconomics/exam/past-exam-questions)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)")

@bot.command()
async def micro(ctx):
    await ctx.send("AP Micro:\n"
                   "- [AP Micro Study Guide](https://drive.google.com/file/d/1t8ssdIhdSwEi0sfRU75_0gPK0KkzTC0w/view?usp=sharing)\n"
                   "- [AP Micro FRQ'S](https://apcentral.collegeboard.org/courses/ap-microeconomics/exam/past-exam-questions)\n"
                   "- [AP Books Recommended By Yours Truly](https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d)")

@bot.command()
async def phys1(ctx):
    await ctx.send("AP Phys1:\n"
                   "- [AP Phys1 Study Guide](https://drive.google.com/file/d/1nwhXBwahbEjHk6KUccKB-HVfa8Zpsb6w/view?usp=sharing)\n"
                   "- [AP Phys1 FRQ'S](https://apcentral.collegeboard.org/courses/ap-physics-1/exam/past-exam-questions)")

@bot.command()
async def followers(ctx):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, "seoul.pearson")
        await ctx.send(f"seoul.pearson has {profile.followers:,} followers.")
    except Exception as e:
        await ctx.send(f"Couldn't fetch follower count. Error: {e}")

bot.run("YOUR_BOT_TOKEN_HERE")
