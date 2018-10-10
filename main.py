import discord
from discord.ext import commands
from discord.ext.commands import errors
import sys
import timeit
import time
import os
import asyncio
import webcolors
import SinBase
import Mode

		
startup_extensions = ["Mode"]
#startup_extensions = ["Owner"]
#Client = commands.Bot(command_prefix = commands.when_mentioned_or('...'))

async def check_pref(ctx, bot, message):
	SinBase.Database.check_prefix(ctx.message.server.id)
	return "prefix"
	
prefix = '...'
Client = commands.Bot(command_prefix = commands.when_mentioned_or(check_pref))



async def status_task():
	while True:
		await Client.change_presence(game=discord.Game(name='... Prefix is ...',type=1))
		await asyncio.sleep(10) 
		await Client.change_presence(game=discord.Game(name='With New codes', type=1))
		await asyncio.sleep(10)
		await Client.change_presence(game=discord.Game(name='OverLord', type=3))
		await asyncio.sleep(10)
		await Client.change_presence(game=discord.Game(name=str(len(Client.servers))+' Severs', type=3))
		await asyncio.sleep(20)








@Client.event
async def on_ready():
	Client.loop.create_task(status_task())
	print(' ')
	print("Logged in as:")
	print(Client.user.name)
	print("ID:"+" "+Client.user.id)
	print("Ready to use:")
	print(" ")
	print("Use this to invite your bot")

	
		
				
@Client.command(pass_context=True)
async def invite(ctx):
	channel = ctx.message.channel
	V = await Client.create_invite(destination = channel,max_age=0)
	await Client.say(V)
	
@Client.command(pass_context=True)
async def p(ctx):
	await Client.check
	await Client.say(V)


@Client.command(pass_context=True)
async def NL(ctx):
	await Client.say('hello\nHow are you')

@Client.command(name="Color" , pass_context=True)
async def name_to_hex(ctx, color):
	webcolors.name_to_hex(color)
	await Client.say(webcolors.name_to_rgb(color))
					
if __name__ == "__main__":
	for extension in startup_extensions:
		try:
			Client.load_extension(extension)
		except Exception as e:
			exc = '{}: {}'.format(type(e).__name__, e)
			print('Failed to load extension {}\n{}'.format(extension, exc))	

				
																		



@Client.command(pass_context = True)
#@commands.check(OwnerIs)
async def kick(ctx, user: discord.User = None ,* , reason:str=None):
	 reason = reason or 'none provided'
	 channel = ctx.message.channel
	 if user is None:
	 	await Client.say('You did not mention a user')
	 elif user.id == ctx.message.author.id:
	 		await Client.say("{} self harm is bad".format(ctx.message.author.mention))
	 else:
	 	rem = await Client.send_message(channel, "Do you want to kick {}".format(user.mention))
	 	msg = await Client.send_message(channel,'No 👎/Yes 👍')
	 	res = await Client.wait_for_reaction(['👍', '👎'], message=msg)
	 	Confirm = '{0.reaction.emoji}'.format(res)
	 	if Confirm == '👎':
	 		pass
	 	try:
	 		if user.id is not ctx.message.author.id:
	 			if Confirm == '👍':
	 				await Client.kick(user)
	 				await Client.say("User \n {} \n User Id \n {} \nwas kicked for".format(user.mention,user.id))
	 				await Client.say('```Reason:```/n'+reason)
	 	except errors.DiscordException:
	 		await Client.say('PermissionError')
	 		await Client.say('Cannot kick ')
	 	await Client.delete_message(msg)
	 	await Client.delete_message(rem)
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 
	 

@Client.command(pass_context = True)
#@commands.check(OwnerIs)
async def ban(ctx, user: discord.User = None):
		
	 A = '{}'.format(user)
	 channel = ctx.message.channel
	 await Client.send_message(channel, 'Do you want to ban '+str(A))
	 msg = await Client.say('No 👎/Yes 👍')
	 
	 res = await Client.wait_for_reaction(['👍', '👎'], message=msg)
	 
	 Confirm = '{0.reaction.emoji}'.format(res)
	 if Confirm == '👎':
	 	exit
	 try:
	 	if Confirm == '👍':
	 		await Client.ban(user)
	 except errors.DiscordException:
	 	Client.say('Unknow user')
	 	Client.say('PermissionError')





def run_client():
	Client.run(')
		
run_client()			
#retry()		