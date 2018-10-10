import discord
from discord.ext import commands
import SinBase

class Mode:
	def __init__(self, Client):
		self.bot = Client
		self.database = SinBase.Database(self.bot)
		
	Owner_is = lambda ctx: ctx.message.author.id == '320256494132002817'	

	
		
				
	def check_pref(self, ctx, serverid):
		A = "{}".format(self.database.check_prefix(serverid))
		print(A)

	
		
			
					
	@commands.command(name="prefix", pass_context=True, help="")
	async def check_prefix(self, ctx):
		await self.bot.say("The current prefix is  {}".format(self.database.check_prefix(ctx.message.server.id)))
		self.check_pref(ctx.message.server.id)
		
	@commands.command(name="set_prefix",pass_context=True)
	async def set_prefix(self, ctx, prefix=None):
		A =ctx.message.server.id
		if prefix is None:
			await self.bot.say("Didn't input your desired prefix")
		else:
			self.database.set_prefix(serverid=A, prefix =prefix)
			await self.bot.say("{} has changed the prefix to ".format(ctx.message.author.mention)+prefix)
		
		
		
def setup(Client):
	 Client.add_cog(Mode(Client))