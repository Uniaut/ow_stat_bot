from useful import *

from orders_import import orders_list

async def act(client, msg):
    content = msg.content

    for orders in orders_list:
        for spell in orders:
            if content.startswith(spell) or content == spell:
                await orders[spell](client, msg)
                return None
    
    await client.send_message(msg.channel,
        embed = embed_format(
            title = '해당하는 명령어를 찾을 수 없습니다!',
            description = '***!도움말***를 이용해 명령어를 찾아보세요.',
            thumbnail = 'http://bitly.kr/UXesf'))