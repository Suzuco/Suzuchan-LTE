import requests
import json

from nonebot import on_command, CommandSession


@on_command("gpt", aliases=["小铃同学"], only_to_me=False)
async def fortune(session: CommandSession):
    ss = session.current_arg_text.strip()

    res = requests.post(
        url="https://suzuco.moe:13450/api/neko-gpt/",
        data=json.dumps({"rq": ss}))

    return await session.send(f"""{res.text}""", at_sender=True)
