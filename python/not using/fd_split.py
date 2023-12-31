import random
import json


class SplitNumbers():
    def __init__(self, lst, fraction_amount, file_name):
        self.lst = lst
        self.original = lst[:]
        self.FRACTION_AMOUNT = fraction_amount
        self.FILE_NAME = file_name

        self.GEN_LST = [i for i in range(150, 2024, 2)]
        self.fraction_list = []
        self.index = 0
        self.done = True

    def splitter(self):
        with open(self.FILE_NAME, "r") as read_file:
            data = json.load(read_file)
            array = data[str(self.index)]
            valid_list = []
            if array != []:
                for lists in array:
                    valid = True
                    for items in lists:
                        if items in self.lst:
                            valid = False
                    if valid:
                        valid_list.append(lists)
                if valid_list != []:
                    next_lists = []
                    for valid in valid_list:
                        temp = []
                        for number in valid:
                            temp.append(len(data[str(number)]))
                        next_lists.append(sum(temp)/len(temp))

                    self.lst.remove(self.index)
                    for items_append in valid_list[
                      next_lists.index(max(next_lists))]:
                        self.lst.append(items_append)
                    self.lst.sort()
                    print()
                    print(self.lst, round(
                        sum([1/i for i in self.lst]), 14), len(self.lst))
                    self.done = False
                    print("split")

    def reloop_self(self):
        with open(self.FILE_NAME, "r") as read_file:
            data = json.load(read_file)
            # checking_list = [i for i in range(2, 2023)]
            # random.shuffle(checking_list)
            # for i in checking_list:
            i = random.randint(2, 2023)
            combos = data[str(i)]
            combos_in_lst = []
            for combo in combos:
                in_lst = True
                for number in combo:
                    if number not in self.lst:
                        in_lst = False
                if in_lst:
                    combos_in_lst.append(combo)
            if combos_in_lst != []:
                combo_lens = [len(i) for i in combos_in_lst]
                for combo in combos:
                    valid = True
                    for number in combo:
                        if number in self.lst:
                            valid = False
                    if valid and len(combo) >= min(combo_lens):
                        for number in combos_in_lst[
                                combo_lens.index(min(combo_lens))]:
                            self.lst.remove(number)
                        for number in combo:
                            self.lst.append(number)
                        self.lst.sort()
                        print(self.lst, round(sum(
                            [1/i for i in self.lst]), 14),
                            len(self.lst))
                        self.done = False
                        print("reloop")
                        return

    def main(self):
        print(self.lst, round(sum([1/i for i in self.lst]), 14), len(self.lst))
        best = []
        while True:
            self.done = True
            for self.index in self.lst:
                self.splitter()
            if self.done:
                best_len = []
                best.append(self.lst)
                for i in best:
                    best_len.append(len(i))
                print("Best list so far:")
                print(str(best[best_len.index(
                    max(best_len))]).replace(" ", ""),
                    len(best[best_len.index(max(best_len))]))
                self.reloop_self()


model_var = SplitNumbers([212,218,219,236,237,242,249,254,256,267,268,289,292,300,303,305,306,309,315,316,319,324,325,327,329,335,336,338,345,361,363,364,366,368,369,370,371,374,375,377,378,380,381,384,387,388,391,396,399,400,402,403,408,414,415,418,423,425,426,427,429,430,432,434,435,436,437,438,440,441,442,444,448,452,456,459,460,462,464,465,468,469,470,472,473,474,475,476,477,480,483,484,486,488,490,492,494,495,496,497,498,500,504,505,507,508,511,512,513,515,516,517,519,520,522,524,525,527,528,531,535,536,539,540,544,546,550,551,552,553,555,556,558,559,560,561,564,567,568,570,572,574,575,576,580,582,583,584,585,588,590,592,594,595,598,600,602,604,605,606,608,609,610,611,616,620,621,623,624,627,629,630,632,635,636,637,638,639,640,642,644,645,646,648,649,650,651,654,656,657,658,660,663,664,665,666,667,671,672,675,676,680,682,684,685,686,688,689,690,693,696,697,700,702,703,704,705,708,710,711,713,714,715,716,720,725,726,728,729,730,731,732,735,736,737,738,740,741,742,744,747,748,749,750,752,754,755,756,759,760,762,765,767,768,770,774,775,776,777,779,780,781,782,783,784,785,790,791,792,793,795,798,799,800,803,804,805,806,808,810,812,814,817,819,820,822,824,825,826,828,830,832,833,834,835,836,837,840,845,846,847,848,850,851,852,854,855,858,860,861,864,868,869,870,871,873,874,876,880,882,884,885,888,889,890,891,893,894,896,897,899,900,901,902,903,906,909,910,912,915,917,918,920,924,925,928,930,931,935,936,938,940,943,945,946,948,949,950,952,954,957,960,962,963,966,968,969,970,975,976,979,980,981,984,986,987,988,989,990,992,994,996,999,1000,1001,1003,1005,1007,1008,1010,1012,1014,1015,1020,1023,1025,1026,1029,1030,1032,1034,1035,1036,1040,1043,1044,1045,1050,1053,1054,1056,1057,1060,1062,1064,1065,1066,1067,1068,1071,1072,1073,1075,1078,1080,1081,1083,1085,1088,1089,1090,1092,1095,1098,1100,1102,1104,1105,1106,1107,1110,1111,1113,1116,1118,1120,1122,1125,1127,1128,1130,1131,1134,1136,1139,1140,1144,1147,1148,1150,1152,1155,1156,1159,1160,1161,1162,1164,1166,1168,1169,1170,1173,1175,1176,1177,1178,1180,1183,1185,1188,1189,1190,1196,1197,1200,1204,1206,1207,1209,1210,1212,1215,1216,1218,1219,1220,1221,1222,1224,1225,1230,1232,1235,1236,1239,1240,1242,1243,1248,1250,1251,1254,1256,1258,1260,1261,1265,1271,1272,1273,1274,1275,1276,1280,1281,1287,1288,1290,1292,1295,1296,1300,1302,1305,1308,1309,1310,1311,1312,1313,1314,1320,1323,1325,1326,1328,1330,1332,1333,1334,1335,1339,1340,1342,1344,1350,1352,1353,1356,1358,1360,1363,1364,1365,1368,1372,1375,1376,1377,1378,1380,1386,1392,1394,1395,1400,1403,1404,1406,1407,1408,1410,1413,1416,1417,1419,1420,1421,1422,1424,1425,1426,1428,1430,1431,1435,1440,1442,1443,1444,1449,1450,1452,1455,1456,1457,1458,1460,1462,1463,1464,1470,1472,1475,1476,1479,1480,1482,1484,1485,1488,1491,1494,1495,1496,1500,1504,1505,1508,1512,1513,1515,1517,1518,1519,1520,1521,1524,1525,1529,1530,1534,1536,1537,1539,1540,1545,1547,1548,1550,1551,1552,1554,1558,1560,1564,1566,1568,1572,1573,1575,1580,1581,1584,1586,1590,1591,1593,1595,1596,1598,1599,1600,1602,1605,1608,1610,1611,1612,1615,1616,1617,1620,1624,1625,1628,1632,1634,1638,1639,1640,1643,1644,1645,1647,1648,1649,1650,1652,1656,1661,1664,1665,1666,1668,1672,1674,1675,1677,1679,1680,1683,1690,1692,1694,1695,1696,1700,1701,1702,1703,1704,1705,1708,1710,1711,1715,1716,1717,1720,1722,1725,1728,1729,1730,1734,1736,1738,1739,1740,1746,1748,1749,1750,1751,1752,1755,1760,1763,1764,1767,1768,1769,1770,1771,1776,1778,1780,1781,1782,1785,1786,1788,1792,1794,1798,1800,1802,1804,1806,1809,1812,1813,1815,1817,1818,1820,1824,1827,1829,1830,1833,1836,1837,1840,1843,1845,1846,1848,1850,1854,1855,1856,1859,1860,1862,1863,1869,1870,1872,1875,1876,1880,1881,1885,1886,1887,1888,1890,1891,1892,1896,1898,1900,1903,1904,1905,1908,1909,1911,1914,1920,1924,1925,1926,1927,1932,1935,1936,1938,1940,1944,1947,1950,1952,1953,1955,1957,1958,1960,1961,1962,1963,1965,1968,1969,1972,1974,1975,1976,1978,1980,1984,1988,1989,1992,1995,1998,2000,2001,2002,2006,2009,2010,2013,2014,2015,2016,2021],
                  fraction_amount=2,
                  file_name="computed_numbers_testing.json")

model_var.main()
