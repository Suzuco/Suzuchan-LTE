import requests
import json

from nonebot import on_command, CommandSession

MEMORY_RETAIN = 1
history = {}


def api(session: CommandSession, channel: str):
    ss = session.current_arg_text.strip()

    ev = session.event
    gid = ev["group_id"]
    if gid not in history.keys():
        history[gid] = []

    if ev["message_type"] == "group" and ev["sub_type"] == "normal":
        user = ev["sender"]["card"] or ev["sender"]["nickname"]
        source = gid if channel == "premium" else 0
    else:
        user = ev["sender"]["nickname"]
        source = 0
    resp = requests.post(
        url="https://suzuco.moe:13450/api/neko-gpt/",
        data=json.dumps({"rq": ss, "by": user, "from": source,
                         "history": json.dumps(history[gid]) if len(history[gid]) != 0 else ""}))

    history[gid].append((ss, resp.text))
    if len(history[gid]) > MEMORY_RETAIN:
        history[gid] = history[gid][-MEMORY_RETAIN:]
    return resp


@on_command("gpt", aliases=["小铃同学"], only_to_me=False)
async def gpt(session: CommandSession):
    resp = api(session, "")
    return await session.send(f"""{resp.text}""", at_sender=True)


@on_command("gpt+", aliases=["grq", "grp"], only_to_me=False)
async def gpt_premium(session: CommandSession):
    resp = api(session, "premium")
    return await session.send(f"""{resp.text}""", at_sender=True)
