import discord
from discord.ext import commands
from discord.utils import get
import requests
import json
import os
from dotenv import load_dotenv
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


bot.run ('TOKEN')
