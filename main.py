import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from flask import Flask
import threading

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True  # ✅ THIS IS REQUIRED
bot = commands.Bot(command_prefix='!', intents=intents, help_command=None)

@bot.command()
async def resources(ctx):
    await ctx.send("Main resource : [Main Resource](<https://drive.google.com/drive/folders/1kG84_tEPph4bEQqu2GnYx84xUzbdFGLw>)")

@bot.command()
async def history(ctx):
    await ctx.send("Ultimate AP history doc : [Ultimate AP History Doc](<https://drive.google.com/file/d/1SJmA5dc_2lzkNhiBR_pevBQPOn2r9Myw/view?usp=sharing>)")

@bot.command()
async def ultimate(ctx):
    await ctx.send("Ultimate AP doc : [Ultimate AP Doc](<https://drive.google.com/file/d/1jyXdoHBQjI9HkNU7_IV48HMtGyuM5AIp/view?usp=sharing>)")

@bot.command()
async def books(ctx):
    await ctx.send("[Books](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def notes(ctx):
    await ctx.send("[Notes](<https://drive.google.com/drive/folders/1fxW4qSZWQ84ZNOSWOcBCcO_XENyl2zhh>)")

@bot.command()
async def bio(ctx):
    await ctx.send("AP Bio:\n"
                   "- [AP Bio Review](<https://docs.google.com/document/d/17_9ZhQVCf61bRlch_e0gdQJzWz1k2doi7EcuLXEnyps/edit?usp=sharing>)\n"
                   "- [AP Bio Study Guide](<https://drive.google.com/file/d/1vFCZ1NlapvePVZlQwnOFC-P-WWWG9x02/view?usp=sharing>)\n"
                   "- [AP Bio Weebly](<https://apbiopenguins.weebly.com/>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)\n"
                   "- [AP Bio FRQ'S](<https://apcentral.collegeboard.org/courses/ap-biology/exam/past-exam-questions>)\n"
                   "- [AP Bio Study Guide Supplements](<https://drive.google.com/file/d/1o2BsjfHPkSFzACbHAvHW9M6cs876Qzun/view?usp=sharing>)")

@bot.command()
async def calc(ctx):
    await ctx.send("AP Calc:\n"
                   "- [AP Calc Study Guide](<https://support.ebsco.com/LEX/AP-Calculus-BC-Study-Guide.pdf>)\n"
                   "- [AP Calc Study Guide 2](<https://docs.google.com/document/d/1iBpqlLvhZhThJ_OOsgRR27E_aKgJAmmibdkRdVya7rc/edit?usp=sharing>)\n"
                   "- [AP Calc Study Guide 3](<https://drive.google.com/file/d/1EmMMbltrE8zzaOeaNl9EWziX0x8WSdDS/view>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)\n"
                   "- [AP Calc Review Sheet](<https://drive.google.com/file/d/0Bx50M-1D0Q0WNHllRmFDd21VZVk/view?resourcekey=0-0O1JQbsJKKlVQAiObBj1AQ>)\n"
                   "- [AP Calc AB FRQ'S](<https://apcentral.collegeboard.org/courses/ap-calculus-ab/exam/past-exam-questions>)\n"
                   "- [AP Calc BC FRQ'S](<https://apcentral.collegeboard.org/courses/ap-calculus-bc/exam/past-exam-questions>)")

@bot.command()
async def chem(ctx):
    await ctx.send("AP Chem:\n"
                   "- [AP Chem Review](<https://docs.google.com/document/d/1LLFUpQ3Vgzv--MWzW286_Dio-v8n0NfR3KDvWGbqj-Q/edit?usp=sharing>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)\n"
                   "- [AP Chem FRQ'S](<https://apcentral.collegeboard.org/courses/ap-chemistry/exam/past-exam-questions>)")

@bot.command()
async def compgov(ctx):
    await ctx.send("AP Comp Gov:\n"
                   "- [AP Comp Gov Study Guide](<https://drive.google.com/file/d/14uFsIpb_FGg-k07oFiVIOfJUhCItP__W/view?usp=sharing>)\n"
                   "- [AP Comp Gov Doc](<https://docs.google.com/document/d/1XKNibHnw63Wq-2mHT-P0pMqtKUdfAEJqRuCvjQfpkRE/edit?usp=sharing>)\n"
                   "- [AP Comp Gov FRQ'S](<https://apcentral.collegeboard.org/courses/ap-comparative-government-and-politics/exam/past-exam-questions>)")

@bot.command()
async def csa(ctx):
    await ctx.send("AP CSA:\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)\n"
                   "- [AP CSA Study Guide](<https://drive.google.com/file/d/122tDTodwHCudKZeuVRL8aS78SIr5Dfkz/view?usp=sharing>)\n"
                   "- [AP CSA CSAwesome](<https://runestone.academy/ns/books/published/csawesome2/csawesome2.html>)\n"
                   "- [AP CSA CodingBat](<https://codingbat.com/java>)\n"
                   "- [AP CSA Knowt](<https://knowt.com/exams/AP/AP-Computer-Science-A>)\n"
                   "- [AP CSA FRQ'S](<https://apcentral.collegeboard.org/courses/ap-computer-science-a/exam/past-exam-questions>)")

@bot.command()
async def lang(ctx):
    await ctx.send("AP Lang:\n"
                   "- [AP Lang ChatGPT](<https://chatgpt.com/>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)\n"
                   "- [AP Lang CoachHallWrites](<https://www.youtube.com/@CoachHallWrites/videos>)\n"
                   "- [AP Lang FRQ'S](<https://apcentral.collegeboard.org/courses/ap-english-language-and-composition/exam/past-exam-questions>)")

@bot.command()
async def lit(ctx):
    await ctx.send("AP Lit:\n"
                   "- [AP Lit Study Guide](<https://drive.google.com/file/d/1CaZNq2TJiwuGV2MX4pg15T1NV5Px67Vk/view?usp=sharing>)\n"
                   "- [AP Lit FRQ'S](<https://apcentral.collegeboard.org/courses/ap-english-literature-and-composition/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def envsci(ctx):
    await ctx.send("AP Env Sci:\n"
                   "- [AP Env Sci Study Guide](<https://drive.google.com/file/d/14SSP1sFmKM_uOLXe6qX_eMqxm8-NKLAc/view>)\n"
                   "- [AP Env Sci FRQ'S](<https://apcentral.collegeboard.org/courses/ap-environmental-science/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def euro(ctx):
    await ctx.send("AP Euro:\n"
                   "- [Ap Euro Study Guide](<https://drive.google.com/file/d/1jjSqlYaba-uqMtjBspy1BoXB8v_dIyn5/view?usp=drive_link>)\n"
                   "- [AP Euro FRQ'S](<https://apcentral.collegeboard.org/courses/ap-european-history/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def hgap(ctx):
    await ctx.send("HGAP:\n"
                   "- [HGAP Study Guide](<https://drive.google.com/file/d/1hbPV0hWetWQxdrthu38h6qLmEjhKWuQR/view?usp=sharing>)\n"
                   "- [HGAP FRQ'S](<https://apcentral.collegeboard.org/courses/ap-human-geography/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def macro(ctx):
    await ctx.send("AP Macro:\n"
                   "- [AP Macro Review Econ](<https://www.youtube.com/@ReviewEcon>)\n"
                   "- [AP Macro By Jacob Clifford](<https://www.youtube.com/channel/UCCQEbqDL8i40d83Au55lYMQ>)\n"
                   "- [AP Macro Cheat Sheet](<https://lopiccolo.weebly.com/uploads/7/7/7/4/7774746/ap_macro_ultimate_cheat_sheet_key.pdf>)\n"
                   "- [AP Macro Study Guide](<https://drive.google.com/drive/folders/1fxW4qSZWQ84ZNOSWOcBCcO_XENyl2zhh>)\n"
                   "- [AP Macro FRQ'S](<https://apcentral.collegeboard.org/courses/ap-macroeconomics/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def micro(ctx):
    await ctx.send("AP Micro:\n"
                   "- [AP Micro Study Guide](<https://drive.google.com/file/d/1t8ssdIhdSwEi0sfRU75_0gPK0KkzTC0w/view?usp=sharing>)\n"
                   "- [AP Micro FRQ'S](<https://apcentral.collegeboard.org/courses/ap-microeconomics/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def phys1(ctx):
    await ctx.send("AP Phys1:\n"
                   "- [AP Phys1 Study Guide](<https://drive.google.com/file/d/1nwhXBwahbEjHk6KUccKB-HVfa8Zpsb6w/view?usp=sharing>)\n"
                   "- [AP Phys1 FRQ'S](<https://apcentral.collegeboard.org/courses/ap-physics-1/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def phys2(ctx):
    await ctx.send("AP Phys2:\n"
                   "- [AP Phys2 Study Guide](<https://drive.google.com/file/d/1DJZx5ISUOV_GPj7d9jMuLkDlD4Tp4Vyy/view?usp=sharing>)\n"
                   "- [AP Phys2 FRQ'S](<https://apcentral.collegeboard.org/courses/ap-physics-2/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def physc(ctx):
    await ctx.send("AP PhysC:\n"
                   "- [AP PhysC Mechanics Lectures](<https://www.apphysicslectures.com/ap-physics-mechanics>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)\n"
                   "- [AP PhysC Mechanics FRQ'S](<https://apcentral.collegeboard.org/courses/ap-physics-c-mechanics/exam/past-exam-questions>)\n"
                   "- [Ap PhysC & E&M Videos](<https://www.youtube.com/@AllenTsaoSTEMCoach/videos>)\n"
                   "- [AP PhysC E&M Videos](<https://www.youtube.com/@onlearningcurve/videos>)\n"
                   "- [AP PhysC E&M FRQ'S](<https://apcentral.collegeboard.org/courses/ap-physics-c-electricity-and-magnetism/exam/past-exam-questions>)\n"
                   "- [AP PhysC E&M Lectures](<https://www.apphysicslectures.com/ap-physics-em>)")

@bot.command()
async def psych(ctx):
    await ctx.send("AP Psych:\n"
                   "- [AP Psych Study Guide](<https://drive.google.com/file/d/1Y-fbM-Mm0CzuvI8VIctRd-E4xfUO1Xk9/view?usp=sharing>)\n"
                   "- [AP Psych MrSinn](<https://www.youtube.com/c/MrSinn>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)\n"
                   "- [AP Psych FRQ'S](<https://apcentral.collegeboard.org/courses/ap-psychology/exam/past-exam-questions>)")

@bot.command()
async def stats(ctx):
    await ctx.send("AP Stats:\n"
                   "- [AP Stats Study Guide](<https://drive.google.com/file/d/1ofNZ1lLI279Bf0Tf-SJ_zmHYb7UTJd8i/view?usp=sharing>)\n"
                   "- [AP Stats FRQ'S](<https://apcentral.collegeboard.org/courses/ap-statistics/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def gov(ctx):
    await ctx.send("AP Gov:\n"
                   "- [AP Gov Study Guide](<https://docs.google.com/document/d/18jeARsST6IXmVjASNAaZXLi6YKAh6xBxqYL7fx4X488/edit?usp=sharing>)\n"
                   "- [AP Gov FRQ'S](<https://apcentral.collegeboard.org/courses/ap-united-states-government-and-politics/exam/past-exam-questions>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)")

@bot.command()
async def apush(ctx):
    await ctx.send("APUSH:\n"
                   "- [APUSH Study Guide](<https://docs.google.com/document/d/1jCHQsaYkP5zwrl8yLnsdZv-5ihlGwEKTl-Hh05Pexx4/edit?tab=t.0#heading=h.nxwivvotvuh2>)\n"
                   "- [APUSH DBQ Guide](<https://docs.google.com/document/d/1g_eWMx3JgkX2omglypbmbnl5RkK7ANhtK_jOLKLiS5Y/edit?tab=t.0>)\n"
                   "- [AP Books Recommended By Yours Truly](<https://www.amazon.com/shop/seoul.pearson/list/1NZ0VQJAPPFHK?linkCode=spc&tag=onamzpeterhon-20&ref_=aip_sf_list_spv_ofs_mixed_d>)\n"
                   "- [APUSH FRQ'S](<https://apcentral.collegeboard.org/courses/ap-united-states-history/exam/past-exam-questions>)\n"
                   "- [APUSH MCQ](<https://apcentral.collegeboard.org/media/pdf/ap-united-states-history-ced-practice-exam.pdf>)\n"
                   "- [ChatGPT](<https://chatgpt.com>)\n"
                   "- [APUSH Study Guide #2](<https://docs.google.com/document/d/1LFoA6letcr0AfOQoUEoEt7ZEQwsWqfrOPRS3EZS_y78/edit?usp=sharing>)")

@bot.command()
async def whap(ctx):
    await ctx.send("WHAP:\n"
                   "- [WHAP Full Study Guide](<https://docs.google.com/document/d/1Xrs0tLkEGB7LAhqUOXaYeRC7kfgcFQSXo4Mo5Gfvmn8/edit?usp=sharing>)")

@bot.command()
async def say(ctx, *, message):
    """Repeats whatever you say"""
    await ctx.send(message)

@bot.command()
async def help(ctx):
    """Displays a categorized list of available commands"""
    embed = discord.Embed(
        title="📚 AP Study Bot Help",
        description="Use `!command` for resources. Example: `!bio` for Biology\n\n"
                    "**Need a specific subject?** Use these categories:",
        color=discord.Color.blue()
    )

    # Categories with emojis
    categories = {
        "🔬 Sciences": ["bio", "chem", "phys1", "phys2", "physc", "envsci"],
        "📐 Math/CS": ["calc", "stats", "csa"],
        "🌍 Social Studies": ["apush", "gov", "hgap", "euro", "whap", "compgov"],
        "💵 Economics": ["macro", "micro"],
        "📝 English": ["lang", "lit"],
        "🧠 Psychology": ["psych"],
        "📂 General": ["resources", "history", "ultimate", "books", "notes"]
    }

    # Build the embed fields
    for category, commands in categories.items():
        cmd_list = ", ".join(f"`!{cmd}`" for cmd in commands)
        embed.add_field(name=category, value=cmd_list, inline=True)

    embed.add_field(
        name="🔍 Need more details?",
        value="Type any command to see its specific resources\n"
             "Example: `!bio` for AP Biology resources",
        inline=False
    )

    embed.set_footer(text="Bot created to help AP students | Use !help for this menu")

    await ctx.send(embed=embed)


app = Flask(__name__)

@app.route('/health')
def health_check():
    return {"status": "healthy"}, 200

def run_flask():
    app.run(host='0.0.0.0', port=int(os.getenv("PORT", 8080)))

# Start Flask in background
flask_thread = threading.Thread(target=run_flask)
flask_thread.daemon = True
flask_thread.start()

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

bot.run(os.getenv("DISCORD_TOKEN"))