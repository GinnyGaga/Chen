a_list = [
    {"name": "c1","A":"starting","B":123,"C":"abc"},
    {"name": "c2", "A": "stopping", "B": 678, "C": "ghi"},
    {"name": "c3","A":"starting","B":345,"C":"def"}
]

b_list = []
for i in a_list:
    if i["A"] == "starting":
        b_list.append(i["name"])
print(b_list)


class VirtualM:
    def closeVM(self, type=3):
        # type=3表示关闭所有虚拟机
        pass

    def queryVM(self):
        pass


# 按经验，关闭一台虚拟机需要10秒
CLOSE_ONE_SPAND_SECOND = 10



# 判断虚拟机什么时候全部关闭成功
# 1、不断的循环查询虚拟机的运行状态，2、如果全部虚拟机的状态为已关闭，则停止查询，3、最多重试2次
retryTimes = 0 # 记录已经重试的次数
while True: # 不断循环
    allClosed = True  # 是否已经已关闭的表示，默认全部已关机
    rsp = VirtualM().queryVM() # 查询
    count = len(rsp) # 计算出虚拟机的总数
    for detail in rsp: # 遍历所有虚拟机的信息
        if detail["status"] != "close":  # 检查单台虚拟机的状态是否是已关闭
            allClose = False
            break # 只要有一个没关闭，都是没有完全关闭，跳出for循环

    if allClose == True:  # 当所有虚拟机已经关闭，跳出while循环
        break

    retryTimes += 1
    if retryTimes >= 2:
        raise Exception # 抛出一个重试2次虚拟机仍未关闭的错误
    import time
    time.sleep(count * CLOSE_ONE_SPAND_SECOND)  # 延迟n秒后重新检查



