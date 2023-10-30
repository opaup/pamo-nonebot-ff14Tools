from ..utils import sendCore

noOneSale = '没有找到关于【{}】的市场信息\n宋娜？居然没人卖？'
noSellableItems = ''
existedRelatedItems = '\n你可能想要搜索：{}'


async def searchPrice(cmds):
    # 初始化
    length = len(cmds)
    itemName = ''
    dateCenter = ''
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
    if len(items) == 0:
        return '没有找到关于【' + itemName + '】的可售卖道具'
    result.append('查询【' + dateCenter + '】中【' + items[0]['Name'] + '】的市场价格：\n')

    # 开始查询市场
    itemId = items[0]['ID']
    extPath = dateCenter + '/' + str(itemId) + '/'
    data = await sendCore.doSend(extPath, ifHQ)["listings"]
    if len(data) == 0:
        return noOneSale % itemName
    i = 0
    for item in data:
        i += 1
        result.append(str(i))
        result.append('.' + items[0]['Name'])
        if item['hq']:
            result.append('(★)')
        result.append('(' + str(item['quantity']) + 'x' + str(item['pricePerUnit']) + ' = ' + str(item['total']) + ')')
        result.append(' 服务器：' + item['worldName'])
        result.append(' 雇员：' + item['retainerName'])
        if i != len(data):
            result.append('\n')
    if len(items) >= 2:
        otherItems = ''
        for item in items:
            otherItems += ' ' + item['Name']
        result.append('\n你可能想要搜索：' + otherItems)

    return "".join(result)


async def searchInfo(cmds):
    # 初始化
    length = len(cmds)
    itemName = ''
    dateCenter = ''
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
    if len(items) == 0:
        return '没有找到关于【' + itemName + '】的可售卖道具'
    result.append('查询【' + dateCenter + '】中【' + items[0]['Name'] + '】的市场历史行情：\n')
    # 开始查询市场
    itemId = items[0]['ID']
    extPath = dateCenter + '/' + str(itemId) + '/'
    data = await sendCore.doSend(extPath, ifHQ)
    if len(data["listings"]) == 0:
        return noOneSale % itemName

    # 未售平均价格（NQ+HQ）
    currentAveragePrice = data['currentAveragePrice']
    result.append("未售平均价格（NQ+HQ）：" + currentAveragePrice)
    # 未售平均价格（NQ）
    currentAveragePriceNQ = data['currentAveragePriceNQ']
    result.append("\n未售平均价格（NQ）：" + currentAveragePriceNQ)
    # 未售平均价格（HQ）
    currentAveragePriceHQ = data['currentAveragePriceHQ']
    result.append("\n未售平均价格（HQ）：" + currentAveragePriceHQ)
    # 平均日售量
    regularSaleVelocity = data['regularSaleVelocity']
    result.append("\n平均日售量：" + regularSaleVelocity)
    # NQ 售卖速度
    nqSaleVelocity = data['nqSaleVelocity']
    result.append("\nNQ 售卖速度：" + nqSaleVelocity)
    # HQ 售卖速度
    hqSaleVelocity = data['hqSaleVelocity']
    result.append("\nHQ 售卖速度：" + hqSaleVelocity)
    # 已售平均价格（NQ+HQ）
    averagePrice = data['averagePrice']
    result.append("\n已售平均价格（NQ+HQ）：" + averagePrice)
    # 已售平均价格（NQ）
    averagePriceNQ = data['averagePriceNQ']
    result.append("\n已售平均价格（NQ）：" + averagePriceNQ)
    # 已售平均价格（HQ）
    averagePriceHQ = data['averagePriceHQ']
    result.append("\n已售平均价格（HQ）：" + averagePriceHQ)
    # 最小销售单价（NQ+HQ）
    minPrice = data['minPrice']
    result.append("\n最小销售单价（NQ+HQ）：" + minPrice)
    # 最小销售单价（NQ）
    minPriceNQ = data['minPriceNQ']
    result.append("\n最小销售单价（NQ）：" + minPriceNQ)
    # 最小销售单价（HQ）
    minPriceHQ = data['minPriceHQ']
    result.append("\n最小销售单价（HQ）：" + minPriceHQ)
    # 最大销售单价（NQ+HQ）
    maxPrice = data['maxPrice']
    result.append("\n最大销售单价（NQ+HQ）：" + maxPrice)
    # 最大销售单价（NQ）
    maxPriceNQ = data['maxPriceNQ']
    result.append("\n最大销售单价（NQ）：" + maxPriceNQ)
    # 最大销售单价（HQ）
    maxPriceHQ = data['maxPriceHQ']
    result.append("\n最大销售单价（HQ）：" + maxPriceHQ)

    if len(items) >= 2:
        otherItems = ''
        for item in items:
            otherItems += ' ' + item['Name']
        result.append('\n你可能想要搜索：' + otherItems)

    return
