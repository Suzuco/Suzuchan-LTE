import math
import random
import hashlib
from datetime import date
import numpy as np

from nonebot import on_command, CommandSession

ast_deck = ["太阳神之衡", "世界树之干", "战争神之枪",
            "放浪神之箭", "建筑神之塔", "河流神之瓶"]
ast_seal = "\U00002600\U0001F319\U0001F31F"

tiles = list(range(ord('\U0001F000'), ord('\U0001F022')))
tiles = tiles[7:] + tiles[0:4] + [tiles[6], tiles[5], tiles[4]]


@on_command("运势", only_to_me=False)
async def fortune(session: CommandSession):
    uid = str(session.event['user_id'])
    token = uid + "@" + str(date.isoformat(date.today()))
    cookies = list(hashlib.sha1(token.encode('utf-8')).digest())

    rp = int((cookies[0] + cookies[1]) / 5.1)

    alcana = np.sum(cookies[0:18])
    str_alcana = ast_deck[alcana % 6]
    alcana //= 6
    str_alcana += " / "
    str_alcana += "王冠之领主" if alcana % 2 == 1 else "王冠之贵妇"
    alcana //= 2
    str_alcana += " / "
    for i in range(3):
        str_alcana += ast_seal[alcana % 3]
        alcana //= 3

    seed_mj = cookies[19] + cookies[18] * 256 + cookies[17] * 65536 + cookies[16] * 16777216
    rgen = random.Random(seed_mj)
    hand = rgen.sample(range(136), 14)
    hand.sort()
    str_hand = "".join([chr(tiles[t // 4]) for t in hand])

    return await session.send(f"""今日人品：{rp}
袖内抽塔：{str_alcana}
一把起手：{str_hand}""", at_sender=True)
