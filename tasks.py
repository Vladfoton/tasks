import copy
import turtle


# type 2

def type2():
    print('x y z w')
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not ((x == (not (y))) <= ((x and w) == (z and (not (w))))):
                        print(x, y, z, w)


# type5

def type5():
    def fff(n):
        nb = bin(n)[2:]
        count1 = nb.count('1')
        count0 = nb.count('0')
        if count1 > count0:
            nb += '1'
        else:
            nb += '0'
        return nb

    print(int(fff(13), 2))
    for n in range(1, 100):
        if int(fff(n), 2) > 100:
            print(int(fff(n), 2))
            break


# type 6

def type6():
    import turtle
    n = 20
    turtle.left(90)

    for _ in range(5):
        turtle.forward(9 * n)
        turtle.right(120)

    turtle.up()

    turtle.goto(0, 0)
    for x in range(-n, 15 * n, n):
        for y in range(0, 15 * n, n):
            turtle.goto(x, y)
            turtle.dot(5)
    turtle.done()


# type8

def type8():
    from itertools import product

    s = 'аоу'

    dd = product(s, repeat=5)
    dd = sorted(list(dd))
    print(*dd)
    for i, c in enumerate(dd, start=1):
        print(i, c)


# type12

def type12():
    s = '1' * 82
    while (('11111' in s) or ('888' in s)):
        print(s, len(s))
        if '11111' in s:
            s = s.replace('11111', '88', 1)
        elif '888' in s:
            s = s.replace('888', '8', 1)

    print(s)


# type 14
def type14():
    n = 36 ** 7 + 6 ** 19 - 18

    def convert_to(num, base):
        ss = ''
        while num > 0:
            ss += str(num % base)
            num = num // base
        return ss[::-1]

    print(convert_to(n, 6))
    print(convert_to(n, 6).count('0'))


# type15
def type15():
    for a in range(1000):
        flag = True
        for x in range(1000):
            if not (((x % 3 == 0) <= (not (x % 5 == 0))) or (x + a >= 90)):
                flag = False
                break
        if flag:
            print(a)
            break


def type16():
    def f(n):
        if n <= 2:
            return 1
        else:
            return (f(n - 2) * (n - 1))

    print(f(7))


def type17():
    with open('17.txt', 'r') as f:
        num_data = [i[:-1] for i in f.readlines()]
        print(num_data)
        count = 0
        maxsum = 0
        filtered_num = [int(i) for i in num_data if (len(i) == 3 and i[-1] == '5')]
        delitel = min(filtered_num)
        print(f'{delitel=}')
        result = []
        for i in range(len(num_data) - 1):
            if (((len(num_data[i]) == 4) or (len(num_data[i + 1]) == 4)) and (
                    len(num_data[i]) + len(num_data[i + 1]) != 8)):
                summq = int(num_data[i]) ** 2 + int(num_data[i + 1]) ** 2
                if summq % delitel == 0:
                    count += 1
                    maxsum = max(maxsum, summq)

        print(f'{count=}  {maxsum=}')


def type23():
    def f(start, end):
        print(start, end)
        if start == end:
            print('find')
            return 1
        elif start > end:
            return 0
        else:
            return f(start + 2, end) + f(start * 2, end)

    print(f(1, 4) * f(4, 8))


def type24():
    with open('1_24.txt', 'r') as f:
        minlen = 10000000000000000000000000
        str_data = f.readline()
        str_data = str_data.replace('TT', "*")
        print(str_data)
        print(str_data.count('*'))
        for start in range(0, len(str_data) - 1):
            countsimbols = 0
            count_tt = 0
            for c in range(start, len(str_data)):
                if str_data[c] == "*":
                    count_tt += 1
                countsimbols += 1
                if count_tt == 150:
                    minlen = min(minlen, countsimbols + 150)
                    print(f'{start=} Current_len = {minlen}')
                    countsimbols = 0
                    count_tt = 0

        print(minlen)


def type25():
    def delit(n):
        count = 0
        delit_list = []
        for i in range(2, int(n / 2), 2):
            if n % i == 0:
                count += 1
                delit_list.append(i)
            if count > 3:
                return False
        if count == 3:
            print(f'{n=}, {delit_list=}')
            return True
        else:
            return False

    rez = []
    for n in range(101000000, 102000000, 2):
        if delit(n):
            rez.append(n)
            print(rez)
    print(sorted(rez))


def type26():
    with open('26.txt', 'r') as f:
        rez = {}
        list_data = [i[:-1] for i in f.readlines()]
        nums, summa = map(int, list_data.pop(0).split())
        print(nums, summa)
        for string in list_data:
            cost, type_izd = string.split()
            if type_izd in rez:
                rez[type_izd].append(int(cost))
            else:
                rez[type_izd] = [int(cost)]
        for key in rez:
            print(sorted(rez[key]))
        count_a = 0
        count_summa = 0
        for aa in sorted(rez['A']):
            if count_summa + int(aa) <= summa:
                count_a += 1
                count_summa += int(aa)
            else:
                break
        for bb in sorted(rez['B']):
            if count_summa + int(bb) <= summa:
                count_summa += int(bb)
            else:
                print(f'{count_a=}  delta = {summa - count_summa}')


def type27(filename):
    def count_odd_even(datalist) -> int:
        # считаем количество четных и нечетных
        # если четных больше возвращаем 0 иначе 1
        # если равны то 2
        count_1 = 0
        count_0 = 0
        for i in datalist:
            if i % 2:
                count_1 += 1
            else:
                count_0 += 1
        if count_0 == count_1:
            return 2
        if count_1 > count_0:
            return 1
        else:
            return 0

    with open(filename, 'r') as f:
        string_data = f.readlines()
        len_list = int(string_data.pop(0))
        print(len_list)
        list_min = []
        list_max = []

        for data in string_data:
            list_min.append(min(map(int, data.split())))
            list_max.append(max(map(int, data.split())))
        listmin = sorted(list_min, reverse=True)
        listmax = sorted(list_max, reverse=True)
        rezult = copy.deepcopy(listmax)




def newyear_chalenge1():
    string = 'ЗЖ АЮДЮЖФВ, АДЗВ Б ЗРЮЖХ ЖЮ ДЧЪБЛ ЙЗЯЭЮКЛЫЗ'
    alphabeet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'

    for i in range(33):
        str1 = ''
        for char in string:
            str1 += chr(ord(char) + i)
        print(f'{i=} : {str1}')


def newyear_chalenge4():
    rezult = []
    num = 1
    for i in range(1, 101):
        rezult.append((num, num + 1, num + 2))
        num += 3
    print(rezult)
    print(sum(rezult[99]))


def newyear_chalenge5():
    from collections import deque
    dd = deque('beegeek')
    print(dd)
    dd.append('b')
    print(dd)
    dd.popleft()
    print(dd)
    dd.popleft()
    dd.popleft()
    print(dd)
    dd.append('e')
    dd.append('e')
    dd.append('g')
    dd.popleft()
    dd.append('k')
    dd.popleft()
    dd.popleft()
    dd.append('!')
    print(dd)


class BreakLoops(Exception):
    pass
def newyear_chalenge10():
    try:
        for a in range(27, 201):
            print(f'{a=}')
            for b in range(a+1, 201):
                for c in range(b+1, 201):
                    for d in range(c+1, 201):
                        for e in range(d+1, 201):
                            if ((a ** 5 + b ** 5 + c ** 5 + d ** 5) == e ** 5):
                                print(a, b, c, d, e)
                                raise BreakLoops
    except BreakLoops:
        pass

if __name__ == '__main__':
    data = [4,
            8,
            15,
            16,
            3,
            14,
            15,
            192,
            168,
            1992,
            37,
            256,
            98,
            101,
            273,
            7787,
            918,
            39,
            1098,
            222,
            69]
    print(len(data))


