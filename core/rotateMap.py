import time
import datetime
import pytz
import random


japan_tz = pytz.timezone('Asia/Tokyo')
specified_time = japan_tz.localize(datetime.datetime(2023, 10, 30))
start_timestamp = int(specified_time.timestamp())
hours_add = 18 * 3600
tc_maps = ['机关大殿', '角力学校', '火山之心', '机关大殿', '角力学校', '九霄云上', ]


def get_zc():
    timestamp = int(time.time())
    passed = (timestamp - start_timestamp) // 86400
    remainder = passed % 3
    result_map = ""
    if remainder == 0:
        result_map = "碎冰冰"
    if remainder == 1:
        result_map = "大草原"
    if remainder == 2:
        result_map = "尘封秘岩"
    msg = [
        f"今天是{result_map}哦，狼王们快冲！",
        f"小真寻夜观天象，原来今天的战场是...{result_map}",
        f"今天的战场是{result_map}，有没有那个....圆圆的(*/ω＼*)"
    ]
    result_msg = random.choice(msg)
    return result_msg


def get_tc():
    # 90分钟一轮换，先计算出首轮的地图
    # 计算经过的90分钟区间
    current_timestamp = int(time.time())
    elapsed_seconds = current_timestamp - start_timestamp
    elapsed_intervals = elapsed_seconds // (90 * 60) % len(tc_maps) - 1
    result_map = tc_maps[elapsed_intervals]
    next_map = tc_maps[elapsed_intervals + 1]

    # 计算距离下一个90分钟的时间（单位为 x 分 y 秒）
    remaining_seconds = (90 * 60) - (elapsed_seconds % (90 * 60))
    minutes, seconds = divmod(remaining_seconds, 60)


    return f"当前推车地图是[{result_map}]，距离[{next_map}]还剩{minutes}分{seconds}秒"
