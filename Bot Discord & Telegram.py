import discord # pip install discord.py
from discord.ext import commands
from discord import Embed, Member
from datetime import datetime
import requests , re , string , random,os,telepott,threading

def RandomString(n=10):
    letters = string.ascii_lowercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringUpper(n = 10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringUpper(n=10):
    letters = string.ascii_uppercase + '1234567890'
    return ''.join(random.choice(letters) for i in range(n))

def RandomStringChars(n=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(n))

def randomStringWithChar(stringLength=10):
    letters = string.ascii_lowercase + '1234567890'
    result = ''.join(random.choice(letters) for i in range(stringLength - 1))
    return RandomStringChars(1) + result
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66"}

bot = commands.Bot(command_prefix="$")
bot.remove_command('help')
class Discord_Bot_Settings:
	def __init__(self) -> object:
		bot.run("Put YOUR TOKEN HERE") #Token For Bot Discord

	@bot.event
	async def on_ready() -> bot:
		print("[+] Bot Is Online !")
		print(f"[+] Bot Username: {bot.user}")
		print(f"[+] Bot ID: {bot.user.id}")
		await bot.change_presence(status = discord.Status.idle, activity = discord.Game("$tik | Instagram : @1k3k"))
	
	@bot.event
	async def on_command_error(ctx,error) -> bot:
		print(error)



	@bot.command()
	async def ut(ctx) -> bot:
		bot.launch_time = datetime.utcnow()
		delta_uptime = datetime.utcnow() - bot.launch_time
		hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
		minutes, seconds = divmod(remainder, 60)
		days, hours = divmod(hours, 24)
		eme = discord.Embed(title = ":hourglass_flowing_sand: Bot Uptime !", description = f"**{days}** day, **{hours}** hours, **{minutes}** minutes and **{seconds}** seconds")
		await ctx.reply(embed = eme, mention_author=True)



	@bot.command(aliases=["help"])
	async def Help(ctx) -> bot:
		#print(ctx.author.id)
		eme = discord.Embed(title = "TTDownloaderHelp", description = f"**Tiktok Downloader ($Tik Url)**")
		await ctx.reply(embed = eme, mention_author=False)



	@bot.command(aliases=["tik","tok","Tik","Tok","Tiktok","TikTok"])
	async def tiktok(ctx,url) -> bot:
		await ctx.message.delete()
		try:
			
			await ctx.author.send(f"Wait a Moment To Upload Vedio")
			
			name = RandomString(20)
			sessionReq = requests.Session()
			try:
				req = sessionReq.get("https://musicaldown.com/",headers=headers)
				data = {
					re.findall('input name="(.*?)"',req.text)[0]:url,
					re.findall('input name="(.*?)"',req.text)[1]:re.findall('value="(.*?)"',req.text)[0],
					re.findall('input name="(.*?)"',req.text)[2]:re.findall('value="(.*?)"',req.text)[1]
					}
				req = sessionReq.post(f"https://musicaldown.com/download",data=data,headers=headers)
				if "Video is private or removed!" in req.text:
					print("[+] video private/removed")
					await ctx.author.send(f"video private/removed")
					
					
				res = re.findall(
					'<a style="margin-top:10px;" target="_blank" rel="noreferrer" href="(.*?)"',req.text
				)
				if len(res) == 0:
					pass
				content = requests.get(res[0]).content
				
				try:
					os.mkdir("Video")
				except:
					pass
				open(f"Video/{name}.mp4","wb").write(content)
				await ctx.author.send(file=discord.File(f"Video/{name}.mp4"))
				print(f"[+] Successfully Upload Video To Discord @{ctx.author}")
			except AttributeError:
				print(f"[+] Error Url @{ctx.author}")
				await ctx.author.send(f"Error Url @{ctx.author}")

		except :
			print(f"[+] I Cant DM You {ctx.author.mention}")
			await ctx.send(f"I Cant DM You {ctx.author.mention}")




class TeleGram_Downloader:
    def __init__(self) -> object:
        self.telegram_token = ' Put YOUR TOKEN HERE ' #Token For Bot TeleGram
        os.system("cls")
        self.bot = telepott.Bot(self.telegram_token)
		
        self.bot.message_loop(self.handle)
		
        while True:
            continue
        
        
    def download(self,url , chat_id,username):

        
        try:
            #print(f"[ / ] Wait For Check {url}")
            #self.bot.sendMessage(chat_id,f"[ / ] Wait For Check {url}")
            
            sessionReq = requests.Session()
            req = sessionReq.get("https://musicaldown.com/",headers=headers)
            data = {
                re.findall('input name="(.*?)"',req.text)[0]:url,
                re.findall('input name="(.*?)"',req.text)[1]:re.findall('value="(.*?)"',req.text)[0],
                re.findall('input name="(.*?)"',req.text)[2]:re.findall('value="(.*?)"',req.text)[1]
                }
            req = sessionReq.post(f"https://musicaldown.com/download",data=data,headers=headers)
            if "Video is private or removed!" in req.text:
                print("video private/removed")
                self.bot.sendMessage(chat_id,"video private/removed")
                return "private/removed"
            res = re.findall(
                '<a style="margin-top:10px;" target="_blank" rel="noreferrer" href="(.*?)"',req.text
            )
            if len(res) == 0:return False
            content = requests.get(res[0]).content
            name = RandomString(20) + username
            try:
                os.mkdir("Video")
            except:
                pass
            open(f"Video/{name}.mp4","wb").write(content)
            self.bot.sendVideo(chat_id,open(f"Video/{name}.mp4","rb"))
            print(f"[+] Successfully Upload Video To Telegram @{username}")
            

        except AttributeError:
            self.bot.sendMessage(chat_id,"Error Url")
            return False





    def handle(self,msg):
        content_type, chat_type, chat_id = telepott.glance(msg)
        user = self.bot.getUpdates(allowed_updates='message')
        message = user[0]['message']['text']
        try:
            username = user[0]['message']['from']['username']
        except:
            username = "Unknown"
        if "/start" in message:
            self.bot.sendMessage(chat_id,f"Welcome @{username} To Rayan Downloader bot\nIG : @1k3k\nTelegram : @Rayan1198")
        elif "tiktok" in message:
            self.download(message,chat_id,username)


def runDis():
	Discord_Bot_Settings()

	
def runTele():
		TeleGram_Downloader()


threading.Thread(target=runDis).start()
threading.Thread(target=runTele).start()
