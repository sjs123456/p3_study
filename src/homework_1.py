"""
author : sjs

设计一个三级菜单，通过命令可以进行选择

结构：
-省
    -市
        -县
"""
provinceNum = {
    "1": "安徽",
    "2": "江西"
}
cityNum = {
    "101": "安庆",
    "102": "合肥",
    "201": "九江",
    "202": "合肥",
}

provinceInfo = {
    "安徽": {
        "合肥": {
            "1": "肥东",
            "2": "市区",
            "3": "肥西"
        },
        "安庆": {
            "1": "宿松",
            "2": "太湖",
            "3": "千山"
        }

    },
    "江西": {
        "九江": {
            "1": "石墨",
            "2": "爱迪生",
            "3": "阿打算"
        },
        "南昌": {
            "1": "阿达是",
            "2": "安飞",
            "3": "打上"
        },
    }
}

exit_flag = False
currentPage = 0


print("-----------请输入对应编码选择地区------------")

for i in provinceNum.keys():
    # 打印出一级目录
    print((i+".")+"\t"+provinceNum[i])

while True:
    if exit_flag:  # 退出标识符
        break
    areaNo1 = input(">>>:")
    if areaNo1 == "quit":
        break
    else:
        # 如果输入字符为
        cityList = list(provinceInfo[provinceNum[areaNo1]].keys())
        for i in range(1, len(cityList) + 1):
            print((str(i) + ".") + "\t" + cityList[i-1])
        currentPage += 1
        while True:
            areaNo2 = input(">>>:")
            if areaNo2 == "back":
                if currentPage == 1:
                    for i in provinceNum.keys():
                        print((i + ".") + "\t" + provinceNum[i])
                    break
                if currentPage == 2:
                    cityList = list(provinceInfo[provinceNum[areaNo1]].keys())
                    for i in range(1, len(cityList) + 1):
                        print((str(i) + ".") + "\t" + cityList[i - 1])
                currentPage -= 1
            elif areaNo2 == "quit":
                exit_flag = True
                break
            else:
                countyList = list(provinceInfo[provinceNum[areaNo1]][cityList[int(areaNo2)-1]].values())
                for i in range(1, len(countyList) + 1):
                    print((str(i) + ".") + "\t" + countyList[i - 1])
                currentPage += 1