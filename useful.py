import discord
import math

from preference import embed_color

def embed_format(title = '', description = '', 
                    author = '', author_link = '', author_icon = '', 
                    thumbnail = '', title_link = '',
                    format = ''):

    embed = discord.Embed(title = title, description = description, color = embed_color)
    embed.set_author(name = author, url = author_link, icon_url = author_icon)
    embed.set_thumbnail(url = thumbnail)

    contents = format.split('$')
    cnt = math.floor(len(contents)/2)
    for index in range(cnt):
        embed.add_field(name = contents[index * 2 + 0], value = contents[index * 2 + 1])

    return embed