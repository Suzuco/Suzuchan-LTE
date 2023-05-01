
from os import path

import nonebot

import config

if __name__ == '__main__':
    nonebot.init(config)
    # nonebot.load_builtin_plugins()
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'extensions', 'gojb'), 'extensions.gojb'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'extensions', 'selector'), 'extensions.selector'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'extensions', 'fortune'), 'extensions.fortune'
    )
    nonebot.load_plugins(
        path.join(path.dirname(__file__), 'extensions', 'chatgpt'), 'extensions.chatgpt'
    )
    nonebot.run()
