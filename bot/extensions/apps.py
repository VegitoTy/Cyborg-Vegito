import discord, json, asyncio
from discord.ext import commands

with open("./configs/config.json") as f:
    bot_config = json.load(f)

default_guilds = bot_config["bot"]["default_guild"]

class AcceptDenyModView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='Accept', custom_id='accept_view', style=discord.ButtonStyle.green)
    async def accept(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(content="Are You Sure? Reply With Yes Or No", ephemeral=True)
        def check(message):
            return message.channel == interaction.channel and message.author == interaction.user
        
        bot = getattr(interaction, "client", interaction._state._get_client())

        try:
            yesnoreply = await bot.wait_for('message', check=check, timeout=60.0)
            yesnoreply_content = yesnoreply.content
            await yesnoreply.delete()
        except:
            await interaction.user.send('Timed Out')
            return
        
        if yesnoreply_content == 'yes': pass
        elif yesnoreply_content == 'no': return await interaction.user.send('Cancelled')
        else: return await interaction.user.send('Invalid Response! Retry')

        dmmessage = await interaction.user.send('Please Send The ID Of The User Your Accepting Application Of To Continue...')
        def check2(message):
            return interaction.user == message.author and message.channel == dmmessage.channel
        try:
            id = (await bot.wait_for('message', check=check2, timeout=140.0)).content
        except:
            await interaction.user.send('Timed Out')
            return
        
        try:
            integer_id = int(id)
        except:
            await interaction.user.send('Invalid ID.')
        
        user = await interaction.guild.query_members(user_ids=[integer_id])
        if not user:
            return await interaction.user.send('User Not Found.')
        user = user[0]
        role = discord.utils.get(interaction.guild.roles, id=1005036107257356298)
        await user.add_roles(role)
        await user.send('Congratulations! Your Application Has Been Accepted! Make Sure To Do Your Job Properly.')
        await interaction.channel.send(f'The Application For Moderator Of {user} Has Been Accepted By {interaction.user}.')
        await interaction.user.send(f"{user} Has Been Given The {role.name} Role And Has Been Dm'ed About Them Getting Accepted.")
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
    
    @discord.ui.button(label='Deny', custom_id='deny_view', style=discord.ButtonStyle.red)
    async def deny(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(content="Are You Sure? Reply With Yes Or No", ephemeral=True)
        def check(message):
            return message.channel == interaction.channel and message.author == interaction.user
        
        bot = getattr(interaction, "client", interaction._state._get_client())

        try:
            yesnoreply = await bot.wait_for('message', check=check, timeout=60.0)
            yesnoreply_content = yesnoreply.content
            await yesnoreply.delete()
        except:
            await interaction.user.send('Timed Out')
            return
        
        if yesnoreply_content == 'yes': pass
        elif yesnoreply_content == 'no': return await interaction.user.send('Cancelled')
        else: return await interaction.user.send('Invalid Response! Retry')

        dmmessage = await interaction.user.send('Please Send The ID Of The User Your Denying Application Of To Continue...')
        def check2(message):
            return interaction.user == message.author and message.channel == dmmessage.channel
        try:
            id = (await bot.wait_for('message', check=check2, timeout=140.0)).content
        except:
            await interaction.user.send('Timed Out')
            return
        
        try:
            integer_id = int(id)
        except:
            await interaction.user.send('Invalid ID.')

        user = await interaction.guild.query_members(user_ids=[integer_id])
        if not user:
            return await interaction.user.send('User Not Found.')
        user = user[0]
    
        await user.send('Sorry! But Your Appplication Has Been Denied. Put More Effort Into The Application Next Time!')
        await interaction.channel.send(f'The Application For Moderator Of {user} Has Been Denied By {interaction.user}.')
        await interaction.user.send(f"Application Of {user} Has Been Denied")
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)

class AcceptDenyFruitStockerView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='Accept', custom_id='accept_view', style=discord.ButtonStyle.green)
    async def accept(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(content="Are You Sure? Reply With Yes Or No", ephemeral=True)
        def check(message):
            return message.channel == interaction.channel and message.author == interaction.user
        
        bot = getattr(interaction, "client", interaction._state._get_client())

        try:
            yesnoreply = await bot.wait_for('message', check=check, timeout=60.0)
            yesnoreply_content = yesnoreply.content
            await yesnoreply.delete()
        except:
            await interaction.user.send('Timed Out')
            return
        
        if yesnoreply_content == 'yes': pass
        elif yesnoreply_content == 'no': return await interaction.user.send('Cancelled')
        else: return await interaction.user.send('Invalid Response! Retry')

        dmmessage = await interaction.user.send('Please Send The ID Of The User Your Accepting Application Of To Continue...')
        def check2(message):
            return interaction.user == message.author and message.channel == dmmessage.channel
        try:
            id = (await bot.wait_for('message', check=check2, timeout=140.0)).content
        except:
            await interaction.user.send('Timed Out')
            return
        
        try:
            integer_id = int(id)
        except:
            await interaction.user.send('Invalid ID.')
        
        user = await interaction.guild.query_members(user_ids=[integer_id])
        if not user:
            return await interaction.user.send('User Not Found.')
        user = user[0]
        role = discord.utils.get(interaction.guild.roles, id=1007671076219781290)
        await user.add_roles(role)
        await user.send('Congratulations! Your Application Has Been Accepted! Make Sure To Do Your Job Properly.')
        await interaction.channel.send(f'The Application For Fruit Stocker Of {user} Has Been Accepted By {interaction.user}.')
        await interaction.user.send(f"{user} Has Been Given The {role.name} Role And Has Been Dm'ed About Them Getting Accepted.")
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)
    
    @discord.ui.button(label='Deny', custom_id='deny_view', style=discord.ButtonStyle.red)
    async def deny(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(content="Are You Sure? Reply With Yes Or No", ephemeral=True)
        def check(message):
            return message.channel == interaction.channel and message.author == interaction.user
        
        bot = getattr(interaction, "client", interaction._state._get_client())

        try:
            yesnoreply = await bot.wait_for('message', check=check, timeout=60.0)
            yesnoreply_content = yesnoreply.content
            await yesnoreply.delete()
        except:
            await interaction.user.send('Timed Out')
            return
        
        if yesnoreply_content == 'yes': pass
        elif yesnoreply_content == 'no': return await interaction.user.send('Cancelled')
        else: return await interaction.user.send('Invalid Response! Retry')

        dmmessage = await interaction.user.send('Please Send The ID Of The User Your Denying Application Of To Continue...')
        def check2(message):
            return interaction.user == message.author and message.channel == dmmessage.channel
        try:
            id = (await bot.wait_for('message', check=check2, timeout=140.0)).content
        except:
            await interaction.user.send('Timed Out')
            return
        
        try:
            integer_id = int(id)
        except:
            await interaction.user.send('Invalid ID.')

        user = await interaction.guild.query_members(user_ids=[integer_id])
        if not user:
            return await interaction.user.send('User Not Found.')
        user = user[0]
    
        await user.send('Sorry! But Your Appplication Has Been Denied. Put More Effort Into The Application Next Time!')
        await interaction.channel.send(f'The Application For Fruit Stocker Of {user} Has Been Denied By {interaction.user}.')
        await interaction.user.send(f"Application Of {user} Has Been Denied")
        for item in self.children:
            item.disabled = True
        await interaction.message.edit(view=self)

class StaffAppsView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
    
    @discord.ui.button(label='Moderator', custom_id='moderator_app', emoji='<:moderator:1007613892974878741>')
    async def mod_app(self, interaction:discord.Interaction, button:discord.ui.Button):
        view = AcceptDenyModView()
        role = discord.utils.get(interaction.guild.roles, id=1005038327382159501)
        if not role in interaction.user.roles:
            await interaction.response.send_message(content='You Need To Be Atleast Level 5 To Apply For Moderator!', ephemeral=True)
            return
        await interaction.response.send_message(content='Check Your Dm!', ephemeral=True)
        questions = [
            "Send Your Username#Discriminator And Your ID",
            "How Long Have You Been In The Server?",
            "What Is Your Level In The Server?",
            "Do You Have Any Previous Modding Experience? If Yes Send The Server.",
            "Do You Understand The Job Of A Mod?",
            "What Does A Moderator Do?",
            "What Will You Do If Someone Is Spamming In General?",
            "What Will You Do If Another Moderator Is Abusing His/Her Powers?",
            "Whats Your Timezone?",
            "Any Other Thing You Want To Mention?"
        ]

        dmMessage = await interaction.user.send('Hi! I Am Going To Ask You Some Questions, Answer Them Wisely. Any Troll Responses Would Be Punished.\n\nYou Can Say Cancel Anytime To Cancel')
        def check(message):
            return message.author == interaction.user and message.channel == dmMessage.channel
        embed = discord.Embed(title=f'{interaction.user} Applied For Moderator!', description='The Users Answers Are Below!', color=0x3498db)
        bot = getattr(interaction, "client", interaction._state._get_client())

        await asyncio.sleep(2)

        question_count=0

        for question in questions:
            question_count+=1
            embed2=discord.Embed(title=f'Question #{question_count}', description=question, color=0x3498db)
            await interaction.user.send(embed=embed2)
            Reply = (await bot.wait_for('message', check=check)).content
            if Reply.lower() == 'cancel':
                return await interaction.user.send('Cancelled')
            embed.add_field(name=question, value=Reply)
        
        await interaction.user.send('Sending The Responses..')
        
        channel = discord.utils.get(interaction.guild.text_channels, id=1007655242965459074)
        await channel.send(embed=embed, view=view)

        await asyncio.sleep(2)
        await interaction.user.send('Thanks For Applying! Your Answers Have Been Recorded!')
    
    @discord.ui.button(label='Fruit Stocker', custom_id='fruit_stocker_app', emoji='🍎')
    async def fruit_stocker_app(self, interaction:discord.Interaction, button:discord.ui.Button):
        view = AcceptDenyFruitStockerView()
        await interaction.response.send_message(content='Check Your DM!', ephemeral=True)

        questions = [
            "Send Your Username#Discriminator And Your ID",
            "How Long Have You Been In The Server?",
            "What Is Your Level In The Server?",
            "Any Other Thing You Want To Mention?"
        ]

        dmMessage = await interaction.user.send('Hi! I Am Going To Ask You Some Questions, Answer Them Wisely. Any Troll Responses Would Be Punished.\n\nYou Can Say Cancel Anytime To Cancel')

        def check(message):
            return message.author == interaction.user and message.channel == dmMessage.channel

        embed = discord.Embed(title=f'{interaction.user} Applied For A Fruit Stocker!', description='The Users Answers Are Below!', color=0x3498db)

        bot = getattr(interaction, "client", interaction._state._get_client())

        await asyncio.sleep(2)

        question_count=0

        for question in questions:
            question_count+=1
            embed2=discord.Embed(title=f'Question #{question_count}', description=question, color=0x3498db)
            await interaction.user.send(embed=embed2)
            Reply = (await bot.wait_for('message', check=check)).content
            if Reply.lower() == 'cancel':
                return await interaction.user.send('Cancelled')
            embed.add_field(name=question, value=Reply)
        
        await interaction.user.send('Sending The Responses...')
        channel = discord.utils.get(interaction.guild.text_channels, id=1007655242965459074)
        await channel.send(embed=embed, view=view)

        await asyncio.sleep(2)
        await interaction.user.send('Thanks For Applying! Your Answers Have Been Recorded!')

class Apps(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
    
    @commands.command(name='StaffApps', aliases=['staffapps', 'SA', 'sa'], hidden=True)
    @commands.check_any(commands.has_permissions(administrator=True), commands.is_owner())
    async def _sa(self, ctx:commands.Context):
        "Sends The Staff Applications"

        view=StaffAppsView()

        await ctx.message.delete()
        apps=discord.Embed(title='Applications', description=f'> <:moderator:1007613892974878741> Click On The Moderator Button To Apply For Moderator!\n\n> 🍎 Click On The Fruit Stocker Button To Apply For A Fruit Stocker!', color=0x3498db)
        await ctx.send(embed=apps, view=view)

async def setup(bot:commands.Bot) -> None:
    await bot.add_cog(
        Apps(bot),
        guilds = [discord.Object(id = default_guilds)]
    )