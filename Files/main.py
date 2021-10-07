#!/usr/bin/python3
import discord, colorama, time
from discord.ext import commands
from colorama import Fore, Style

colorama.init()

prefix = ">"
auth_token = "PASTE TOKEN HERE"
client = commands.Bot(command_prefix=prefix)
client.remove_command("help")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game(f"Flask | {prefix}help"))
    print(Fore.LIGHTCYAN_EX)
    print("[Discord Token Authorized!]")
    time.sleep(1)
    print(f"[Discord API Connected To {client.user}]")

@client.command()
async def help(ctx):
    await ctx.channel.send(f"""> **{prefix}info**
    > **{prefix}ping**
    > **{prefix}ban**
    > **{prefix}kick**
    > **{prefix}unban**
    > **{prefix}clear**""", delete_after=10)
    await ctx.message.delete()

@client.command()
async def info(ctx):
    await ctx.channel.send("""> **Creator: Azlo**
        > **Created On: 05/10/2021**
        > **Last Updated: 05/10/2021**
        > **https://discord.gg/j597aF5FK8**""", delete_after=10)
    await ctx.message.delete()

@client.command()
async def ping(ctx):
    await ctx.channel.send(f"**SPEED:** {round(client.latency * 1000)}", delete_after=5)
    await ctx.message.delete()

@client.command()
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount)
    await ctx.channel.send("**Purged messages.**", delete_after=5)
    await ctx.message.delete()

@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
    await member.ban(reason = reason)
    await ctx.channel.send("**User was banned.**", delete_after=5)
    await ctx.message.delete()

@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
    await member.kick(reason = reason)
    await ctx.channel.send("**User was kicked.**", delete_after=5)
    await ctx.message.delete()

@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split("#")

    for ban_entry in banned_users:
        user = ban_entry.user

        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("**User was unbanned.**", delete_after=5)
            await ctx.message.delete()
            return

client.run(auth_token)
