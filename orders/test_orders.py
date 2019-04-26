from useful import *

async def test1(client, msg):
    await client.send_message(msg.channel,
        embed = embed_format(
        title = '테스트 1',
        description = 'ㅁㄴㅇㄻㄴㄻㄴㅇㄹㅇㄻㄴㅇㄻㄴㅇㄻㄴㅇㄹ.',
        thumbnail = 'http://bitly.kr/x8BqK'))

orders = {
    '!test1':test1
}