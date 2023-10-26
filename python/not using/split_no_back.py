import random
from datetime import datetime


class SplitNumbers():
    def __init__(self, lst, file_name):
        self.lst = lst
        self.original = lst[:]
        self.FILE_NAME = file_name

        self.cached_numbers = {}
        self.fraction_list = []
        self.counter = 0
        self.index = 0
        self.done = True

    def reader(self):
        with open(self.FILE_NAME, "r") as reader:
            data = reader.readlines()
            for line in data:
                number, number_list = line.strip().split(":")
                number = int(number)
                number_list = list(map(int, number_list.split(" ")))

                if number in self.cached_numbers:
                    self.cached_numbers[number].append(number_list)
                else:
                    self.cached_numbers[number] = [number_list]
        self.cached_numbers = dict(sorted(self.cached_numbers.items()))

    def splitter(self):
        array = self.cached_numbers.get(self.index, [])
        if not len(array):
            return

        def is_valid(lst):
            return all(item not in self.lst for item in lst)

        valid_list = [lst for lst in array if is_valid(lst)]
        if not len(valid_list):
            return

        next_lists = [sum(len(self.cached_numbers.get(number, []))
                          for number in valid) / len(valid)
                      for valid in valid_list]

        max_next_list = valid_list[next_lists.index(max(next_lists))]
        self.lst.remove(self.index)
        self.lst.extend(max_next_list)
        self.lst.sort()

        # if len(self.lst) > 890:
        print(self.counter, round(sum([1/i for i in self.lst])),
              len(self.lst), datetime.utcnow())
        self.counter = 0

    def reloop_self(self):
        while True:
            i = random.randint(2, 2023)
            combos = self.cached_numbers.get(i, [])
            if not combos:
                continue

            def in_list(c):
                return all(number in self.lst for number in c)

            def not_in_list(c):
                return all(number not in self.lst for number in c)
            combos_in_list = list(filter(in_list, combos))
            if not len(combos_in_list):
                continue

            valid_combos = list(filter(lambda c: not_in_list(c), combos))

            if not len(valid_combos):
                continue

            min_list_combo = min(combos_in_list, key=len)
            max_valid_combo = max(valid_combos, key=len)

            if len(max_valid_combo) >= len(min_list_combo):
                pre_list = [number for number in self.lst[:] if number not in min_list_combo]
                pre_list.extend(max_valid_combo)
                pre_list.sort()
                self.lst = pre_list[:]
                self.done = False
                return

    def main(self):
        print("At:", datetime.utcnow())
        print(round(sum([1/i for i in self.lst]), 14), len(self.lst))
        self.reader()
        print("split_tom.py starting…")

        best_list = []
        while True:
            if len(best_list) < len(self.lst):
                best_list = self.lst[:]
                print(str(best_list).replace(" ", ""),
                      round(sum([1/i for i in best_list]), 14))
                print("Best list len", len(best_list))
                if len(self.lst) > 899:
                    with open("lists.csv", "a") as writer:
                        writer.writelines(f"{str(len(self.lst))}, "
                                          f"{str(datetime.utcnow())}, "
                                          f"{str(self.lst)}\n")
            for self.index in self.lst:
                self.splitter()

            if self.done:
                # if self.counter > 300:
                    # if len(self.lst) > 800:
                    #     with open("lists.csv", "a") as writer:
                    #         writer.writelines(f"{str(len(self.lst))}, "
                    #                             f"{str(datetime.utcnow())}, "
                    #                             f"{str(self.lst)}\n")
                    # if len(best_list) < len(self.lst):
                    #     best_list = self.lst

                    # print("Most recent list:")
                    # print(str(self.lst).replace(" ", ""),
                    #       round(sum([1/i for i in self.lst]), 14))
                    # print("Recent list len", len(self.lst))

                    # print()

                    # print("Best list so far:")
                    # print(str(best_list).replace(" ", ""),
                    #       round(sum([1/i for i in best_list]), 14))
                    # print("Best list len", len(best_list))

                    # print("At:", datetime.utcnow())

                    # print("\nRestarting list…")
                    # self.lst = self.original[:]
                    # self.counter = 0
                # else:

                self.reloop_self()
                self.done = True
                self.counter += 1


model_var = SplitNumbers([206, 213, 243, 249, 254, 256, 262, 278, 282, 301, 305, 309, 330, 338, 342, 354, 363, 364, 365, 366, 369, 371, 374, 377, 378, 380, 381, 384, 385, 387, 388, 390, 391, 392, 395, 396, 399, 402, 403, 405, 406, 410, 414, 416, 418, 420, 423, 425, 426, 429, 430, 432, 434, 435, 436, 438, 440, 441, 442, 444, 445, 448, 450, 451, 455, 456, 459, 460, 462, 464, 465, 470, 472, 473, 474, 476, 477, 480, 481, 483, 484, 485, 486, 488, 490, 492, 495, 496, 497, 500, 504, 507, 508, 510, 511, 512, 513, 515, 516, 518, 519, 520, 522, 524, 525, 527, 528, 531, 532, 533, 534, 536, 539, 540, 544, 546, 548, 549, 550, 551, 552, 555, 556, 558, 559, 560, 561, 564, 567, 568, 570, 572, 574, 575, 576, 578, 580, 581, 582, 584, 585, 588, 590, 592, 594, 595, 598, 600, 603, 604, 606, 608, 609, 610, 611, 612, 615, 616, 618, 620, 621, 623, 624, 627, 630, 636, 637, 638, 639, 640, 642, 644, 645, 646, 648, 650, 651, 654, 655, 656, 658, 660, 663, 664, 665, 666, 667, 670, 671, 672, 675, 676, 679, 680, 682, 684, 685, 686, 688, 690, 693, 696, 697, 700, 702, 703, 704, 705, 707, 708, 710, 711, 712, 713, 714, 715, 716, 720, 722, 725, 726, 728, 729, 730, 731, 732, 735, 736, 737, 738, 740, 741, 742, 744, 747, 748, 749, 752, 754, 755, 756, 759, 760, 762, 765, 767, 768, 770, 774, 775, 776, 777, 779, 780, 781, 782, 783, 784, 785, 786, 790, 792, 793, 795, 798, 799, 800, 803, 804, 805, 806, 808, 810, 812, 814, 816, 817, 819, 820, 824, 825, 828, 832, 833, 834, 835, 836, 837, 840, 845, 846, 847, 848, 850, 851, 852, 854, 855, 858, 860, 861, 864, 868, 869, 870, 871, 872, 873, 874, 875, 876, 880, 882, 884, 885, 888, 889, 890, 891, 893, 894, 896, 897, 899, 900, 901, 902, 903, 906, 909, 910, 912, 913, 915, 917, 918, 920, 923, 924, 925, 927, 928, 930, 931, 935, 936, 938, 940, 943, 944, 945, 946, 948, 949, 950, 952, 954, 957, 959, 960, 962, 963, 966, 969, 970, 972, 975, 976, 979, 980, 981, 984, 986, 987, 988, 989, 990, 992, 994, 996, 999, 1000, 1001, 1003, 1005, 1007, 1008, 1012, 1014, 1015, 1017, 1020, 1022, 1023, 1025, 1026, 1029, 1030, 1032, 1034, 1035, 1036, 1037, 1040, 1043, 1044, 1045, 1048, 1050, 1053, 1054, 1056, 1057, 1060, 1062, 1064, 1066, 1067, 1068, 1070, 1071, 1073, 1075, 1079, 1080, 1081, 1085, 1088, 1089, 1090, 1092, 1095, 1100, 1102, 1104, 1105, 1107, 1110, 1111, 1112, 1113, 1116, 1118, 1120, 1121, 1122, 1125, 1127, 1128, 1130, 1131, 1134, 1136, 1139, 1140, 1143, 1144, 1147, 1148, 1150, 1152, 1155, 1157, 1159, 1160, 1161, 1162, 1164, 1168, 1169, 1170, 1173, 1175, 1176, 1177, 1178, 1180, 1183, 1184, 1185, 1188, 1189, 1190, 1196, 1197, 1200, 1204, 1206, 1207, 1209, 1210, 1212, 1216, 1218, 1219, 1220, 1221, 1222, 1224, 1225, 1230, 1232, 1235, 1236, 1239, 1240, 1242, 1243, 1245, 1246, 1247, 1248, 1250, 1251, 1254, 1256, 1258, 1260, 1261, 1264, 1265, 1269, 1271, 1272, 1273, 1274, 1275, 1276, 1280, 1281, 1284, 1287, 1288, 1290, 1292, 1295, 1296, 1298, 1300, 1302, 1305, 1308, 1309, 1310, 1311, 1312, 1313, 1314, 1316, 1320, 1323, 1325, 1326, 1328, 1330, 1332, 1333, 1334, 1335, 1337, 1339, 1340, 1342, 1344, 1350, 1352, 1353, 1356, 1357, 1360, 1363, 1364, 1365, 1368, 1370, 1372, 1375, 1376, 1377, 1378, 1380, 1386, 1387, 1390, 1392, 1394, 1395, 1397, 1400, 1403, 1404, 1406, 1407, 1408, 1410, 1411, 1413, 1414, 1416, 1417, 1419, 1420, 1421, 1422, 1424, 1425, 1426, 1428, 1430, 1431, 1435, 1440, 1441, 1442, 1443, 1444, 1449, 1450, 1452, 1455, 1456, 1457, 1458, 1460, 1462, 1463, 1464, 1469, 1470, 1472, 1474, 1475, 1476, 1479, 1480, 1482, 1484, 1485, 1488, 1491, 1494, 1495, 1496, 1498, 1500, 1501, 1504, 1505, 1508, 1512, 1515, 1517, 1518, 1519, 1520, 1521, 1524, 1525, 1526, 1528, 1529, 1530, 1533, 1534, 1536, 1537, 1539, 1540, 1541, 1545, 1547, 1548, 1550, 1551, 1552, 1554, 1558, 1560, 1562, 1564, 1566, 1568, 1572, 1573, 1575, 1580, 1581, 1582, 1584, 1586, 1590, 1591, 1593, 1595, 1596, 1598, 1599, 1600, 1602, 1605, 1606, 1608, 1610, 1611, 1612, 1615, 1616, 1617, 1620, 1624, 1625, 1628, 1632, 1633, 1634, 1635, 1638, 1639, 1640, 1643, 1644, 1645, 1647, 1649, 1650, 1651, 1652, 1653, 1656, 1659, 1660, 1661, 1664, 1665, 1666, 1668, 1672, 1674, 1675, 1677, 1679, 1680, 1683, 1690, 1692, 1694, 1696, 1700, 1701, 1702, 1704, 1705, 1708, 1710, 1711, 1712, 1715, 1716, 1717, 1719, 1720, 1722, 1725, 1728, 1729, 1730, 1734, 1736, 1738, 1739, 1740, 1742, 1743, 1746, 1748, 1749, 1750, 1751, 1752, 1755, 1760, 1763, 1764, 1767, 1768, 1769, 1770, 1771, 1776, 1778, 1780, 1781, 1782, 1785, 1786, 1788, 1792, 1794, 1798, 1800, 1802, 1804, 1805, 1806, 1807, 1809, 1812, 1813, 1815, 1818, 1819, 1820, 1824, 1825, 1826, 1827, 1829, 1830, 1833, 1836, 1837, 1840, 1845, 1846, 1848, 1850, 1853, 1854, 1855, 1856, 1859, 1860, 1862, 1863, 1869, 1870, 1872, 1875, 1876, 1880, 1881, 1885, 1886, 1887, 1888, 1890, 1891, 1892, 1896, 1898, 1900, 1903, 1904, 1905, 1908, 1911, 1914, 1917, 1919, 1920, 1924, 1925, 1926, 1927, 1932, 1935, 1936, 1938, 1940, 1943, 1944, 1947, 1950, 1952, 1953, 1955, 1957, 1958, 1960, 1961, 1962, 1963, 1968, 1969, 1971, 1972, 1974, 1975, 1976, 1978, 1980, 1984, 1988, 1989, 1992, 1995, 1998, 2000, 2001, 2002, 2006, 2009, 2010, 2013, 2014, 2015, 2016, 2020, 2021, 2023],
                         file_name="data.tom")

model_var.main()
