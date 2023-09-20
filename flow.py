from .core.market import *

noneCmd = '未知指令内容，请使用 ff help 来查询相关指令帮助。'
help = f"""
usage：
    一个简单的FF14工具组，目前只实现了市场价格查询，后续可能会更新其他功能。
    简单指令： /ff market search [道具名] [数据中心]
    道具名为模糊匹配，数据中心不填默认为莫古力，支持国际服查询
""".strip()


async def doFlow(cmdStr):
    # 去除开头空格
    # str = str.lower().replace('ff','').lstrip()
    cmdStr = cmdStr.lower().lstrip()
    cmds = cmdStr.split()
    marketDic = {'market', '市场'}
    helpDic = {'help', '帮助'}

    if len(cmds) == 0:
        return noneCmd
    if cmds[0] in marketDic:
        return await marketType(cmds)
    if cmds[0] in helpDic:
        return help
    else:
        return noneCmd


# =======二级指令
#  ======市场类
async def marketType(cmds):
    search = {'search', 'price', '搜索', '价格查询', '查价格', '查价', '查询'}
    info = {'info', '详情', '信息', '趋势', '行情'}

    if len(cmds) < 3:
        return noneCmd
    if cmds[1] in search:
        return await searchPrice(cmds)
    if cmds[1] in info:
        return await searchInfo(cmds)
    else:
        return noneCmd
