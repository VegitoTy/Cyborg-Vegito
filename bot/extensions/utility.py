import discord
import json, asyncio
from discord.ext import commands

with open("./configs/config.json") as f:
    bot_config = json.load(f)

default_guilds = bot_config["bot"]["default_guild"]


class Verifyview(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='Agree', custom_id='agree_view', style=discord.ButtonStyle.green)
    async def _agree(self, interaction:discord.Interaction, button:discord.ui.Button):
        pass

class Utility(commands.Cog):
    """Shows All The Utility Commands."""

    COG_EMOJI = "🛠️"

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="Ping", aliases=['ping'], description="Shows The Latency Of The Bot.")
    async def ping(self, ctx:commands.Context):
        """Shows The Latency Of The Bot"""
        await ctx.send(f'Latency :- `{round(self.bot.latency * 1000)} ms`')

    @commands.command(name='AV', aliases=['av'], description=f"Shows Someone's Avatar.\nUsage:- &Av [user]")
    async def avatar(self, ctx:commands.Context, member:discord.Member=None):
        """Shows Someone's Avatar."""
        if member == None:
            member = ctx.message.author
        
        embed = discord.Embed(color=0x3498db, title=f"{member}'s avatar")
        embed.set_image(url=member.display_avatar)
        await ctx.reply(embed=embed)

    @commands.group(case_insensitive=True, invoke_without_command=True, name='Embed', description=f"Creates A Embed Separate The Title From The Description With |\nUsage:- &Embed Title|Description")
    @commands.check_any(commands.has_permissions(administrator=True), commands.is_owner())
    async def _embed(self, ctx:commands.Context, channel:discord.TextChannel, *, text:str):
        """Creates A Embed Separate The Title From The Description With |"""
        try:
            title, description = text.split("|", 1)
            embed = discord.Embed(title=title, description=description, color=0x3498db)
            await channel.send(embed=embed)
            await ctx.message.add_reaction("✅")
        except Exception as e:
            await ctx.message.add_reaction("❌")
            raise e
        
    @_embed.command(name='Verification', description='Send The Verification Embed\nUsage:- &Embed Verification')
    @commands.check_any(commands.has_permissions(administrator=True), commands.is_owner())
    async def _verificationembed(self, ctx:commands.Context):
        description = """1. No spamming. This includes begging, copypastas, and text walls

2. No inappropriate content. This includes NSFW material of any kind, excessive profanity, racial slurs, flashing images, and gifs that crash discord clients.

3. No advertising. This includes DM'ing random people in the server with advertisements/invites to other servers.

4. No doxxing. Do not reveal other people's real life info/photos without permission.

5. No selling, trading, or buying accounts. This will get you and the account banned. Be smart - don't give anyone your password, even if they say "its ok i'm just gonna farm on your account for you".

6. Do not ping owners. Pinging admins and mods is allowed, but have a legitimate reason and do not ping all of them.

7. Do not fight, debate, harass, or start drama with other users. Keep it in DMs.

8. Do not bait members into breaking the rules.

9. When DM’ing mods/admins for help, make your message exactly what you need help with. Don’t send a message saying “hi” and expect a response.

10. Do not Mass Ping."""
        embed = discord.Embed(color=0x3498db, title='Rules', description=description)

    @commands.command(name='Echo', aliases=['echo'], description=f"Make The Bot Send A Message\nUsage:- &Echo [message]")
    @commands.check_any(commands.has_permissions(administrator=True), commands.is_owner())
    async def _echo(self, ctx:commands.Context, *, message:str):
        """Make The Bot Send A Message"""
        await ctx.message.delete()
        await ctx.send(message)
        
    @commands.command(name='Userinfo', aliases=['whois', 'ui', 'UI'], description=f"Shows The Info Of A User\nUsage:- &Ui [User]")
    async def _ui(self, ctx:commands.Context, user:discord.User=None):
        """Shows The Info Of A User"""
        if not user:
            user = ctx.author
        
        member = await ctx.guild.query_members(user_ids=[user.id])
        if len(member) == 0:
            created_at = user.created_at
            embed = discord.Embed(colour=0x3498db, timestamp=ctx.message.created_at)
            embed.set_author(name=f'User Info - {user}')
            embed.set_thumbnail(url=user.avatar.url)
            embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.display_avatar.url)
            embed.add_field(name='ID: ', value=user.id, inline=False)
            embed.add_field(name='Name: ',value=user.name,inline=False)
            embed.add_field(name='Created at:',value=discord.utils.format_dt(dt=created_at),inline=False)
        else:
            member:discord.Member = member[0]
            created_at = member.created_at
            joined_at = member.joined_at
            rlist = []
            ignored_roles = 0
            for role in member.roles:
                if len(rlist) >= 15:
                    ignored_roles += 1
                if role.name != "@everyone" and len(rlist) < 15:
                    rlist.append(role.mention)
            e = ""
            for role in rlist:
                e += f"{role}, "     
            embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)
            embed.set_author(name=f'User Info - {member}')
            embed.set_thumbnail(url=member.avatar.url)
            embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.display_avatar.url)
            embed.add_field(name='ID: ',value=member.id,inline=False)
            embed.add_field(name='Name:',value=member.name,inline=False)
            embed.add_field(name='Created at:',value=discord.utils.format_dt(created_at),inline=False)
            embed.add_field(name='Joined at:',value=discord.utils.format_dt(joined_at),inline=False)
            if ignored_roles == 0:
                embed.add_field(name=f'Roles: {len(member.roles)}', value=f'{e[:-2]}',inline=False)
            else:
                embed.add_field(name=f'Roles: {len(member.roles)}', value=f'{e[:-2]} And {ignored_roles} more roles..',inline=False)
            embed.add_field(name='Top Role:',value=member.top_role.mention,inline=False)
        await ctx.send(f'Info about {user}', embed=embed)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(
        Utility(bot),
        guilds = [discord.Object(id = default_guilds)]
    )