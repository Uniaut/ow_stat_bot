from useful import embed_format
from orders.stat import read_stat


async def stat_up(client, msg):
    temp = msg.content.split(' ')

    if len(temp) != 3:
        up_embed = embed_format(
            author = 
                '이해가 안됩니다.',
            thumbnail = 
                'http://bitly.kr/fMDYZF',
            description =
                '!전적 <배틀태그> <숫자> 를 입력해 주세요!'
        )
        await client.send_message(msg.channel, embed = up_embed)
        return None

    name = temp[1]
    code = temp[2]
    wait_msg = await client.send_message(msg.channel, 
        embed = embed_format(
            title = 
                name + '#' + code + '님의 전적을 검색중입니다.',
            description =
                '이 메시지는 검색이 완료되면 자동으로 삭제됩니다.',
            thumbnail = 
                'http://bitly.kr/oEhMgL'
            )
        )
    
    read_stat.read(name, code)

    if read_stat.valid():
        read_stat.update(name, code)

        if not read_stat.alert_check():
            up_embed = embed_format(
                author = 
                    name + '#' + code + '님의 전적이 업데이트 되었습니다!',
                thumbnail = 
                    'http://bitly.kr/cQcct',
                description =
                    '!전적 을 이용해 전적을 확인하세요.'
            )
        else:
            up_embed = embed_format(
                author = 
                    name + '#' + code + '님의 업데이트에 실패했습니다.',
                thumbnail = 
                    'http://bitly.kr/P1G9ZE',
                description =
                    '프로필 비공개 상태이거나, 블리자드 내부 서버의 오류입니다.'
            )
    else:
        up_embed = embed_format(
            author = 
                name + '#' + code + '님이 존재하지 않습니다.',
            thumbnail = 
                'http://bitly.kr/fMDYZF',
            description =
                '배틀태그가 정확한지, 프로필이 공개 상태로 되어있는지 확인해주세요.'
        )
    
    await client.delete_message(wait_msg)
    await client.send_message(msg.channel, embed = up_embed)


async def stat(client, msg):
    temp = msg.content.split(' ')

    if len(temp) != 3:
        stat_embed = embed_format(
            author = 
                '이해가 안됩니다.',
            thumbnail = 
                'http://bitly.kr/fMDYZF',
            description =
                '!전적 <배틀태그> <숫자> 를 입력해 주세요!'
        )
        await client.send_message(msg.channel, embed = stat_embed)
        return None

    name = temp[1]
    code = temp[2]
    wait_msg = await client.send_message(msg.channel, 
        embed = embed_format(
            title = 
                name + '#' + code + '님의 전적을 검색중입니다.',
            description =
                '이 메시지는 검색이 완료되면 자동으로 삭제됩니다.',
            thumbnail = 
                'http://bitly.kr/oEhMgL'
            )
        )
    read_stat.read(name, code)
    

    if read_stat.valid():
        try:
            stat_embed = embed_format(
                author = 
                    name + '#' + code + '님의 전적 확인하기(op.gg 링크로 연결).',
                author_icon =
                    read_stat.get_tier_ai(),
                author_link =
                    'https://overwatch.op.gg/search/?playerName=' + name + '%23' + code,
                title =
                    '**현재 점수: ' + read_stat.get_score() + '**',
                description =
                    '**' + read_stat.get_rank() + '**',
                thumbnail = 
                    read_stat.get_hero_pic(0),
                format = 
                    '플레이 타임 Top 3 영웅 : $------------------------'
            )
            for index in range(3):
                stat_embed.add_field(
                    name = 
                        str(index+1) + '위 : ' + read_stat.get_hero_name(index) + ': ' + read_stat.get_hero_pt(index) +
                        ' ('+ read_stat.get_hero_pp(index) + ')',
                    value = 
                        '승률 ' + read_stat.get_hero_vd(index) + 
                        ', 목숨당 처치 ' + read_stat.get_hero_kd(index),
                    inline = 
                        False
                )
            stat_embed.set_footer(
                text = 
                '마지막 업데이트 : ' + read_stat.get_last_up() +
                '(!업데이트 <배틀태그> 를 이용해 업데이트 할 수 있습니다.)'
            )
        except:
            stat_embed = embed_format(
                author = 
                    name + '#' + code + '님의 전적 확인하기(op.gg 링크로 연결).',
                author_link =
                    'https://overwatch.op.gg/search/?playerName=' + name + '%23' + code,
                title =
                    '오류 발생!',
                description =
                    '**경쟁전 기록이 올바르지 않습니다!**\n'
                    + '이 오류는 일반적으로 경쟁전 배치를 끝마치지 않았을 경우 발생합니다.',
                thumbnail = 
                    'http://bitly.kr/P1G9ZE'
            )
    else:
        stat_embed = embed_format(
            author = 
                name + '#' + code + '님이 존재하지 않습니다!',
            thumbnail = 
                'http://bitly.kr/fMDYZF',
            description =
                '존재하지 않거나 전적이 업데이트 되지 않은 것으로 보입니다.'
        )
    await client.delete_message(wait_msg)
    await client.send_message(msg.channel, embed = stat_embed)


orders = {
    '!전적': stat,
    '!업데이트' : stat_up
}