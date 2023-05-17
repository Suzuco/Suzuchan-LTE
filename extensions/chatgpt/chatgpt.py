import requests
import json

from nonebot import on_command, CommandSession


@on_command("gpt", aliases=["小铃同学"], only_to_me=False)
async def gpt(session: CommandSession):
    ss = session.current_arg_text.strip()

    ev = session.event
    if ev["message_type"] == "group" and ev["sub_type"] == "normal":
        user = ev["sender"]["card"] or ev["sender"]["nickname"]
        # source = await session.bot.get_group_info(group_id=ev["group_id"])
        # source = source["group_name"]
        source = ev["group_id"]
    else:
        user = ev["sender"]["nickname"]
        # source = ""
        source = 0

    res = requests.post(
        url="https://suzuco.moe:13450/api/neko-gpt/",
        data=json.dumps({"rq": ss, "by": user, "from": source}))  # , "from": source}))

    return await session.send(f"""{res.text}""", at_sender=True)
