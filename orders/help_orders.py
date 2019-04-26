from useful import embed_format

async def help(client, msg):
    await client.send_message(msg.channel, 
        embed = embed_format(
            title = 
                '도움말!',
            description =
                '**!도움말**을 이용해 볼 수 있는 항목입니다.\n'
                + '--------------------------',
            thumbnail = 
                'http://bitly.kr/Uq0XTW',
            format = 
                '!전적 [닉네임] [숫자]$배틀태그를 입력받아 전적을 검색합니다.$'
                +'!업데이트 [닉네임] [숫자]$배틀태그를 입력받아 전적을 업데이트 합니다.$'
                +'!결정 [후보1] [후보2] [후보3] ...$후보 중 하나를 결정해줍니다!$'
                +'!익명 [내용]$메시지를 보내지만... 누구의 것인지 알 수 없습니다.'
        )
    )

    
orders = {
    '!도움말':help
}