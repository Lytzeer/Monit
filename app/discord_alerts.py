"""Discord alerts module for monitoring"""

import json
from discord_webhook import DiscordWebhook, DiscordEmbed


def ram_alert(usage):
    """Send a Discord alert when the RAM is overloaded"""
    with open("/etc/monit/conf.d/alerts.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)["ram"]
    webhook_url = data["webhook"]
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="RAM Overloaded", color=0xF58F00)
    embed.set_author(
        name="Monitoring",
        icon_url="https://cdn.discordapp.com/emojis/804823764004765786.gif?size=128&quality=lossless",
    )
    embed.add_embed_field(name="RAM Usage :", value=usage, inline=False)
    embed.set_image(
        url="https://gitlab.com/it4lik/b2-linux-2023/-/raw/master/tp/dev/3/img/monit.jpg"
    )
    embed.set_footer(
        text="Lytzeer",
        icon_url="https://wallpapers-clan.com/wp-content/uploads/2023/11/star-wars-darth-maul-black-red-desktop-wallpaper-preview.jpg",
    )
    webhook.add_embed(embed)
    webhook.execute()


def cpu_alert(usage):
    """Send a Discord alert when the CPU is overloaded"""
    with open("/etc/monit/conf.d/alerts.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)["cpu"]
    webhook_url = data["webhook"]
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="CPU Overloaded", color=0xF58F00)
    embed.set_author(
        name="Monitoring",
        icon_url="https://cdn.discordapp.com/emojis/804823764004765786.gif?size=128&quality=lossless",
    )
    embed.add_embed_field(name="CPU Usage :", value=usage, inline=False)
    embed.set_image(
        url="https://gitlab.com/it4lik/b2-linux-2023/-/raw/master/tp/dev/3/img/monit.jpg"
    )
    embed.set_footer(
        text="Lytzeer",
        icon_url="https://wallpapers-clan.com/wp-content/uploads/2023/11/star-wars-darth-maul-black-red-desktop-wallpaper-preview.jpg",
    )
    webhook.add_embed(embed)
    webhook.execute()


def disk_alert(usage):
    """Send a Discord alert when the Disk is overloaded"""
    with open("/etc/monit/conf.d/alerts.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)["disk"]
    webhook_url = data["webhook"]
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="Disk Overloaded", color=0xF58F00)
    embed.set_author(
        name="Monitoring",
        icon_url="https://cdn.discordapp.com/emojis/804823764004765786.gif?size=128&quality=lossless",
    )
    embed.add_embed_field(name="Disk Usage :", value=usage, inline=False)
    embed.set_image(
        url="https://gitlab.com/it4lik/b2-linux-2023/-/raw/master/tp/dev/3/img/monit.jpg"
    )
    embed.set_footer(
        text="Lytzeer",
        icon_url="https://wallpapers-clan.com/wp-content/uploads/2023/11/star-wars-darth-maul-black-red-desktop-wallpaper-preview.jpg",
    )
    webhook.add_embed(embed)
    webhook.execute()


def ram_alert_critical(usage):
    """Send a critical Discord alert when the RAM is overloaded"""
    with open("/etc/monit/conf.d/alerts.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)["ram"]
    webhook_url = data["webhook"]
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="RAM Overloaded", color=0xF50000)
    embed.set_author(
        name="Monitoring",
        icon_url="https://cdn.discordapp.com/emojis/804823764004765786.gif?size=128&quality=lossless",
    )
    embed.add_embed_field(name="RAM Usage :", value=usage, inline=False)
    embed.set_image(
        url="https://gitlab.com/it4lik/b2-linux-2023/-/raw/master/tp/dev/3/img/monit.jpg"
    )
    embed.set_footer(
        text="Lytzeer",
        icon_url="https://wallpapers-clan.com/wp-content/uploads/2023/11/star-wars-darth-maul-black-red-desktop-wallpaper-preview.jpg",
    )
    webhook.add_embed(embed)
    webhook.execute()


def cpu_alert_critical(usage):
    """Send a critical Discord alert when the CPU is overloaded"""
    with open("/etc/monit/conf.d/alerts.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)["cpu"]
    webhook_url = data["webhook"]
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="CPU Overloaded", color=0xF50000)
    embed.set_author(
        name="Monitoring",
        icon_url="https://cdn.discordapp.com/emojis/804823764004765786.gif?size=128&quality=lossless",
    )
    embed.add_embed_field(name="CPU Usage :", value=usage, inline=False)
    embed.set_image(
        url="https://gitlab.com/it4lik/b2-linux-2023/-/raw/master/tp/dev/3/img/monit.jpg"
    )
    embed.set_footer(
        text="Lytzeer",
        icon_url="https://wallpapers-clan.com/wp-content/uploads/2023/11/star-wars-darth-maul-black-red-desktop-wallpaper-preview.jpg",
    )
    webhook.add_embed(embed)
    webhook.execute()


def disk_alert_critical(usage):
    """Send a critical Discord alert when the Disk is overloaded"""
    with open("/etc/monit/conf.d/alerts.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)["disk"]
    webhook_url = data["webhook"]
    webhook = DiscordWebhook(url=webhook_url)
    embed = DiscordEmbed(title="Disk Overloaded", color=0xF50000)
    embed.set_author(
        name="Monitoring",
        icon_url="https://cdn.discordapp.com/emojis/804823764004765786.gif?size=128&quality=lossless",
    )
    embed.add_embed_field(name="Disk Usage :", value=usage, inline=False)
    embed.set_image(
        url="https://gitlab.com/it4lik/b2-linux-2023/-/raw/master/tp/dev/3/img/monit.jpg"
    )
    embed.set_footer(
        text="Lytzeer",
        icon_url="https://wallpapers-clan.com/wp-content/uploads/2023/11/star-wars-darth-maul-black-red-desktop-wallpaper-preview.jpg",
    )
    webhook.add_embed(embed)
    webhook.execute()


if __name__ == "__main__":
    ram_alert_critical()
    cpu_alert_critical()
    disk_alert_critical()
    ram_alert()
    cpu_alert()
    disk_alert()
