
import re
import random

from nonebot import on_command, CommandSession

pattern = r"[\(（](.*?)[\)）]"


@on_command('rsel', only_to_me=False)
async def rsel(session: CommandSession):
    s = session.current_arg_text.strip()
    candidates = s.split()
    if s == '' or len(candidates) == 0:
        return await session.send("喵有签却要我嗯抽，也是一种抽签。\n"
                                  "（用法：rsel 选项1 [选项2 [选项3 [...]]]）")
    elif len(candidates) == 1:
        candidates.append(candidates[0])
        candidates.append("喵有" if candidates[0].endswith("了") else "不要")
    elif len(candidates) == 3 or len(candidates) == 4:
        candidates.append("小孩子才做选择，大人全都要")
    return await session.send(candidates[random.randint(0, len(candidates) - 1)] + "！")


@on_command('rcat', only_to_me=False)
async def rcat(session: CommandSession):
    s = session.current_arg_text.strip()
    result = re.sub(pattern,
                    lambda m: random.choice(m.group(1).split('/')),
                    s)
    result = "".join([str(random.randint(0, 9)) if s == '#' else s for s in result])
    return await session.send(result + "！")
