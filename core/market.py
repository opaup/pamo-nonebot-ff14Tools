from ..utils import sendCore

async def searchPrice(cmds):
    
    noneCmd = '未知指令内容，请使用 ff help 来查询相关指令帮助。'

    # 初始化
    length = len(cmds)
    itemName = ''
    dateCenter = ''
    if length < 3:
        return noneCmd
    if length >= 3:
        itemName = cmds[2]
        dateCenter = '莫古力'
    if length >= 4:
        dateCenter = cmds[3]
    result = []

    ifHQ = 'false'
    if itemName.lower().endswith("hq"):
        # HQ筛选搜索
        itemName = itemName[:-2]
        ifHQ = 'true'
    items = await sendCore.searchItem(item=itemName)
    if len(items) == 0 :
        return '没有找到关于【' + itemName + '】的可售卖道具'
    result.append('查询【'+ dateCenter +'】中【' + items[0]['Name'] + '】的市场价格：\n')

    # 开始查询市场
    itemId = items[0]['ID']
    extPath = dateCenter + '/' + str(itemId) + '/'
    data = await sendCore.doSend(extPath, ifHQ)
    if len(data) == 0 :
        return '没有找到关于【' + itemName + '】的市场信息\n宋娜？居然没人卖？'
    i = 0
    for item in data:
        i+=1
        result.append(str(i))
        result.append('.' + items[0]['Name'])
        if item['hq'] == True:
            result.append('(★)')
        result.append('(' + str(item['quantity']) + 'x' + str(item['pricePerUnit']) + ' = ' + str(item['total']) + ')')
        result.append(' 服务器：' + item['worldName'])
        result.append(' 雇员：' + item['retainerName'])
        if i != len(data) :
            result.append('\n')
    if len(items)>=2:
        otherItems = ''
        for item in items:
            otherItems += ' ' + item['Name']
        result.append('\n你可能想要搜索：' + otherItems)

    return "".join(result)
