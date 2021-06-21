import os
import pynvml
import re
import time


pynvml.nvmlInit()
max_temp = 0
ave_temp = 0
gpu_nums = pynvml.nvmlDeviceGetCount()
handle_list = [pynvml.nvmlDeviceGetHandleByIndex(i) for i in range(gpu_nums)]

def get_gpu_info():
    max_temp = 0
    device_temp = 0
    ave_temp = 0
    for i in range(len(handle_list)):
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle_list[i])
        use = pynvml.nvmlDeviceGetUtilizationRates(handle_list[i])
        brand = pynvml.nvmlDeviceGetName(handle_list[i]).decode("utf-8")
        device_temp = pynvml.nvmlDeviceGetTemperature(handle_list[i],0)
        ave_temp = ave_temp + device_temp
        if device_temp > max_temp:
            max_temp = device_temp
    ave_temp = ave_temp / gpu_nums
    return max_temp, ave_temp


if __name__ == "__main__":
    while True:
        max_temp, ave_temp=get_gpu_info()
        print ("MAX Temperature:", max_temp)
        print ('AVG Temperature:', ave_temp)
        if max_temp < 40:
            os.system('/root/host_fan_monitor/ipmicfg -fan 2')
            print ('FAN: Optimal')
        elif max_temp < 60:
            os.system('/root/host_fan_monitor/ipmicfg -fan 4')
            print ('FAN: Heavy IO')
        else :
            os.system('/root/host_fan_monitor/ipmicfg -fan 1')
            print ('FAN: Full')
        time.sleep(30)
