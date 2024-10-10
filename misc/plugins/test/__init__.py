from nonebot import get_plugin_config, on_command
from nonebot.plugin import PluginMetadata
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.params import ArgPlainText

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="test",
    description="",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)


weather = on_command(
    "天气", rule=to_me(), aliases={"weather", "查天气"}, priority=10, block=True
)


@weather.handle()
async def handle_function(args: Message = CommandArg()):
    # await weather.finish(f"city")
    pass


@weather.receive("city")
@weather.got("location", prompt="请输入地名")
async def got_location(key1: Event = Received("city"), location: str = ArgPlainText()):
    await weather.finish(f"今天{location}的天气是...")
