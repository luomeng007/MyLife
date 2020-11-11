# -*- coding: utf-8 -*-
"""
Wed Nov 11 09:21:03 2020
"""

import time

# =====================================================================================================================
# x = time.asctime()
# print(x)    # Wed Nov 11 09:21:03 2020
# =====================================================================================================================
x = time.localtime()
# print(x)    # time.struct_time(tm_year=2020, tm_mon=11, tm_mday=11, tm_hour=9, tm_min=23, tm_sec=52, tm_wday=2,
# tm_yday=316, tm_isdst=0)
# time.strftime() convert struct_time to string format
data = time.strftime("%d %m %Y", x)    # 11 11 2020
current_time = time.strftime("%H:%M:%S")
print(data)
print(current_time)

