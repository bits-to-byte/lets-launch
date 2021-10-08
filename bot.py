import discord
from discord.ext import commands
from discord.utils import get
import requests
import json
import os
from dotenv import load_dotenv
import asyncio
from time import gmtime
from time import strftime
from models.cldr import Calendar
from models.commands import Commands
 
load_dotenv()

intents = discord.Intents.all()
intents.members = True
bot=commands.Bot(command_prefix='$',intents=intents)
GUILD= {os.getenv('CHANNEL_NAME')}  #Your server name

#bot events
@bot.event
async def on_ready():
    for guild in bot.guilds:
        if guild.name == GUILD:
            break
    print(
        f'{bot.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')

@bot.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Welcome {0.mention} to {1.name}! 🎉'.format(member, guild)
        await guild.system_channel.send(to_send)

#bot commands
@bot.command(brief='🧪 test command')  #bot test command
async def ping (ctx, member):
    guild = member.guild
    if guild.system_channel is not None:
        to_send = 'Hello {0.mention} it seems you pinged the bot, what do you want to ask?\n type out $help to get all the availabe commands'.format(member)
        await ctx.send(to_send)

@bot.command(brief='🗒️ Show the list of channels on the server')  #channel list
async def List (ctx):

    for guild in bot.guilds:
        channels = '\n - '.join([channel.name for channel in guild.text_channels])
    await ctx.send (f'Channel name:🤓 \n - {channels} \n are the channels you can join')

@bot.command(brief='🐣 Easter egg')  #Easter egg
async def hello(ctx):
    quote=get_quote()
    await ctx.send(quote)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")                                                                   
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

#Create roles{Only for admins}
@bot.command(aliases=['make_role'],brief='🔒 Create roles{Only for admins}')
@commands.has_permissions(manage_roles=True) # Check if the user executing the command can manage roles
async def create_role(ctx, *, name):
	guild = ctx.guild
	await guild.create_role(name=name)
	await ctx.send(f'Role `{name}` has been created 🧗‍')

@bot.command(pass_context=True, name="kick")
@has_permissions(kick_members=True)
async def kick(ctx, *, target: Member):
    if target.server_permissions.administrator:
        await bot.say("Target is an admin")
    else:
        try:
            await bot.kick(target)
            await bot.say("Kicked user{target}")
        except Exception:
            await bot.say("Something went wrong") 
            
#Ask permission for volunteer role from admin
@bot.command(brief='🔑 Ask permission for volunteer role from admin')
async def ask_permission(ctx,role1: discord.Role,role2 : discord.Role):
    if(str(role1)=='Volunteer'):
        await ctx.send(f'We are awaiting Supreme Leader\'s confirmation 🤲')
        for person in role2.members:
            await person.create_dm()
            await person.dm_channel.send(f'Hello Supreme Leader :wink: {ctx.author.name} wants to join your army, Go to #manage-roles to manage permissions')

#Join roles based on interest
@bot.command(brief='🏏 Join roles based on interest')
async def join(ctx,role: discord.Role):
    if(str(role)=='Volunteer'):
        await ctx.send(f'You dont have permission to become a volunteer,ask the Supreme Leader 🤣')
    else:
        await ctx.author.add_roles(role)
        await ctx.send(f'Role {role} has been assigned to {ctx.author.name} 🥳')

# Give roles to others(only for admins)
@bot.command(pass_context=True , brief='✅ Give roles to others(only for admins)')
@commands.has_permissions(manage_roles=True)    # Check if the user executing the command can manage roles
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)
    await ctx.send(f"Hey! {ctx.author.name} {user.name} has been assigned the role : {str(role)} 🔫")
    channel = discord.utils.get(ctx.guild.channels, name='general')
    #channel_id = channel.id
    if(str(role)=='Volunteer'):
    	channel = discord.utils.get(ctx.guild.channels, name='general')
    	await ctx.send(f"Hey! {ctx.author.name} {user.name} is now a part of your army 🔫")
    	await channel.send(f' @here {user.name} is now a Volunteer 😲. If you want to join the army and volunteer for the channel let us know by asking for a permission 🥰 ')

@bot.command(brief='Help to add task')
@commands.has_permissions(manage_roles=True) 
async def add_task(ctx, user: discord.Member, task, role: discord.Role):
    if (str(role) == 'Volunteer' or str(role) == 'Admin'):
        channel = discord.utils.get(ctx.guild.channels, name='task')
    	await ctx.send(f"Hey! a new task is published on #task by {user.name}")
    	await channel.send(f'Hey all this is the new task {task}')    
    

@bot.command(pass_context=True , brief='🛒 Manage merchandise')
@commands.has_permissions(manage_roles=True)
async def post(ctx):
    await ctx.send(f"Hey! {ctx.author.name}, your merchandise has been successfully updated 🛒")

    channel = discord.utils.get(ctx.guild.channels, name='merchandise')
    #channel_id = channel.id
    Merch_list = ['link1', 'link2', 'link3']
    for guild in bot.guilds:
        merch = '\n - '.join([Merch_list[i] for i in range(len(Merch_list))])
    await channel.send(f'🛒New and Exciting Products !! Go Check them out : 🥳 \n - {merch}')

    channel = discord.utils.get(ctx.guild.channels, name='general')
    #channel_id = channel.id
    await channel.send(f'@here the Merchandise has been Updated with New and exciting products. Check them out !! 🛍️🛍️')

async def get_calendar_event(self):
    cldr = Calendar()
    cldr.launch()
    self.event_date = cldr.seconds_event
    self.name_event = cldr.name_event
    if cldr.info_event and cldr.link_event:
        self.link_event = cldr.link_event
    if self.event_date == 0:
        print("No event soon (last 10 minutes)")
    elif self.event_date < 0:
        print("Meeting '{}' has started since {:.2f} seconds".format(self.name_event, self.event_date))
    else:
        print("Meeting '{}' in {:.2f} seconds".format(self.name_event, self.event_date))
    await asyncio.sleep(3)

async def check_reunion_is_soon(self):
    if self.event_date and self.name_event and self.event_date > self.min_time_event and self.event_date < self.max_time_event:
        await self.send_channel_msg("{} will start in: {} ({})".format(self.name_event, strftime("%M:%S", gmtime(int(self.event_date))), self.link_event))
        await asyncio.sleep(self.event_date)
    elif self.event_date and self.name_event and self.event_date >= -60 and self.event_date <= 0:
        await self.send_channel_msg("@here {} has started, it's time!!".format(self.name_event))
        await asyncio.sleep(self.time_to_wait)
    await asyncio.sleep(3)

async def on_ready(self):
    self.main_channel = self.get_channel(self.id_main_channel)
    self.change_status("Working on the api")
    await self.change_presence(status=discord.Status.idle, activity=self.activity)
    while True:
        await self.get_calendar_event()
        await self.check_reunion_is_soon()
        await asyncio.sleep(3)

async def send_channel_msg(self, msg):
    await self.main_channel.send(msg)

async def on_message(self, message):
    if message.author == self.user:
        return
    msg_user_list = message.content.split()
    msg_user = msg_user_list[0]
    if msg_user_list[0][0] == self.identifier_cmd:
        cmd = Commands(msg_user_list)
        await message.channel.send(cmd.message_to_respond())


bot.run ('TOKEN')
