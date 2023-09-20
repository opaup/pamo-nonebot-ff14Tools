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
    if len(items) == 0 :
        return '没有找到关于【' + itemName + '】的可售卖道具'
    result.append('查询【'+ dateCenter +'】中【' + items[0]['Name'] + '】的市场价格：\n')

    # 开始查询市场
    itemId = items[0]['ID']
    extPath = dateCenter + '/' + str(itemId) + '/'
    data = await sendCore.doSend(extPath, ifHQ)["listings"]
    if len(data) == 0 :
        return noOneSale % (itemName)
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
    if len(items) == 0 :
        return '没有找到关于【' + itemName + '】的可售卖道具'
    result.append('查询【'+ dateCenter +'】中【' + items[0]['Name'] + '】的市场信息：\n')
    # 开始查询市场
    itemId = items[0]['ID']
    extPath = dateCenter + '/' + str(itemId) + '/'
    data = await sendCore.doSend(extPath, ifHQ)
    if len(data["listings"]) == 0 :
        return noOneSale % (itemName)
    
    # 未售平均价格（NQ+HQ）
    currentAveragePrice = data['currentAveragePrice']
    # 未售平均价格（NQ
    currentAveragePriceNQ = data['currentAveragePriceNQ']
    # 未售平均价格（HQ
    currentAveragePriceHQ = data['currentAveragePriceHQ']
    # 平均日售量
    regularSaleVelocity = data['regularSaleVelocity']
    # NQ 售卖速度
    nqSaleVelocity = data['nqSaleVelocity']
    # HQ 售卖速度
    hqSaleVelocity = data['hqSaleVelocity']
    # 已售平均价格（NQ+HQ）
    averagePrice = data['averagePrice']
    # 已售平均价格（NQ
    averagePriceNQ = data['averagePriceNQ']
    # 已售平均价格（HQ
    averagePriceHQ = data['averagePriceHQ']
    # 最小销售单价（NQ+HQ）
    minPrice = data['minPrice']
    # 最小销售单价（NQ
    minPriceNQ = data['minPriceNQ']
    # 最小销售单价（HQ
    minPriceHQ = data['minPriceHQ']
    # 最大销售单价（NQ+HQ）
    maxPrice = data['maxPrice']
    # 最大销售单价（NQ
    maxPriceNQ = data['maxPriceNQ']
    # 最大销售单价（HQ
    maxPriceHQ = data['maxPriceHQ']




    return