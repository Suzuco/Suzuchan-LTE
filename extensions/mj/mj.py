
import random
import numpy as np

from nonebot import on_command, CommandSession

tiles = list(range(ord('\U0001F000'), ord('\U0001F022')))
tiles = tiles[7:] + tiles[0:4] + [tiles[6], tiles[5], tiles[4]]


@on_command("mj", aliases=["日麻", "麻将", "马酱"], only_to_me=False)
async def mj(session: CommandSession):
    """Inspired by fortune module """
    ss = session.current_arg_text.strip()
    rgen = random.Random()
    deck = rgen.sample(range(136), 15)
    hand = sorted(deck[1:-1])
    dora = tiles[deck[0] // 4]
    hand = "".join([chr(tiles[t // 4]) for t in hand])
    tumo = tiles[deck[14] // 4]
    return await session.send(f"\n宝牌 {dora}\n{hand} 自摸{tumo}", at_sender=True)
