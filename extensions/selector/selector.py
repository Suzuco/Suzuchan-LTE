
import re
import random

from nonebot import on_command, CommandSession

pattern = r"[\(（](.*?)[\)）]"


@on_command('rcat', only_to_me=False)
async def rcat(session: CommandSession):
    s = session.current_arg_text.strip()
    result = re.sub(pattern,
                    lambda m: random.choice(m.group(1).split('/')),
                    s)
    result = "".join([str(random.randint(0, 9)) if s == '#' else s for s in result])
    return await session.send(result + "！")
