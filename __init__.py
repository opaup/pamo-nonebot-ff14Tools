from nonebot import get_driver, on_command
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.onebot.v11 import MessageSegment, GroupMessageEvent, PrivateMessageEvent, Message, MessageEvent
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from .flow import doFlow

__zx_plugin_name__ = "帕沫的FF14工具包"
__plugin_usage__ = f"""
usage：
    一个简单的FF14工具组，目前实现了市场价格查询与当前pvp地图查询。
    请使用 /ff help 来查询相关指令帮助。
""".strip()
__plugin_des__ = f"一个简单的FF14工具包"
__plugin_cmd__ = ["/ff"]
__plugin_type__ = ("ff14", "工具")
__plugin_version__ = 1.0
__plugin_author__ = "opaup"
__plugin_settings__ = {
    "level": 5,
    "default_status": True,
    "limit_superuser": False,
    "cmd": ["/ff help"],
}

errMsg = '真寻停止了思考...ff14工具包似乎出现了奇怪的问题'


async def use(msg):
    try:
        result = await doFlow(msg)
        return result
    except Exception:
        return errMsg


# response = on_command(cmd=r'^(/|\\)ff\s+(.*)', block=True)
response = on_command(
    "/ff", aliases={"\\ff", "/FF", "\\FF"}, priority=5, block=True
)


@response.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State, arg: Message = CommandArg()):
    msg = arg.extract_plain_text().strip()
    if msg.startswith('/'):
        msg = msg[1:]
    if msg.startswith('\\'):
        msg = msg[1:]
    result = await use(str(msg))
    await response.finish(result)
