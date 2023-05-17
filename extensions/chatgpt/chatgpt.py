import requests
import json

from nonebot import on_command, CommandSession


def api(session: CommandSession, premium: bool):
    ss = session.current_arg_text.strip()

    ev = session.event
    if ev["message_type"] == "group" and ev["sub_type"] == "normal":
        user = ev["sender"]["card"] or ev["sender"]["nickname"]
        source = ev["group_id"] if premium else 0
    else:
        user = ev["sender"]["nickname"]
        source = 0
    return requests.post(
        url="https://suzuco.moe:13450/api/neko-gpt/",
        data=json.dumps({"rq": ss, "by": user, "from": source}))


@on_command("gpt", aliases=["小铃同学"], only_to_me=False)
async def gpt(session: CommandSession, premium=False):
    res = api(session, False)
    return await session.send(f"""{res.text}""", at_sender=True)


@on_command("grq", only_to_me=False)
async def gpt_premium(session: CommandSession):
    res = api(session, True)
    return await session.send(f"""{res.text}""", at_sender=True)
