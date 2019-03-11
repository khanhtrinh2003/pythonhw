import random
random.SystemRandom()
class Gn:
    def __init__(self):
        while True:
            try:
                x = int(input('\n0:Beginer\n1:Intermediate\n2:Advanced\n3:Expert\n4:Master\n5:Grandmaster\n'))
                break
            except ValueError:
                print('nhap lai')
        if x == 0:
            i = 0
            a = random.randint(1, 10)
            while True:
                i += 1
                while True:
                    try:
                        s = int(input('%d NHẬP 1 SỐ TỰ NHIÊN BẤT KÌ: '% i))
                        break
                    except ValueError:
                        print('Nhap lai')

                if s == a:
                    print('CHÚC MỪNG BẠN ĐÃ ĐOÁN ĐÚNG SỐ')
                    print('BẠN ĐƯỢC %d ĐIỂM\n\n' % (i))

                    w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
                    if w == 1:
                        i = 0
                        break
                    elif w == 2:
                        i = 0
                        continue
                    else:
                        print('KHÔNG CÓ SỐ NÀY')
                elif s > a:
                    print('SỐ ĐÓ BÉ HƠN %d'%s)
                else:
                    print('SỐ ĐÓ LỚN HƠN %d' % s)

        elif x == 1:
            i = 0
            a = random.randint(1, 100)

            while True:
                i += 1
                while True:
                    try:
                        s = int(input('%d NHẬP 1 SỐ TỰ NHIÊN BẤT KÌ: '% i))
                        break
                    except ValueError:
                        print('Nhap lai')

                if s == a:
                    print('CHÚC MỪNG BẠN ĐÃ ĐOÁN ĐÚNG SỐ')
                    print('BẠN ĐƯỢC %d ĐIỂM\n\n' % (i))

                    w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
                    if w == 1:
                        i = 0
                        break
                    elif w == 2:
                        i = 0
                        continue
                    else:
                        print('KHÔNG CÓ SỐ NÀY')
                elif s > a:
                    print('SỐ ĐÓ BÉ HƠN %d'%s)
                else:
                    print('SỐ ĐÓ LỚN HƠN %d' % s)

        elif x == 2:
            i = 0
            a = random.randint(1, 10000)
            while True:
                i += 1
                while True:
                    try:
                        s = int(input('%d NHẬP 1 SỐ TỰ NHIÊN BẤT KÌ: '% i))
                        break
                    except ValueError:
                        print('Nhap lai')

                if s == a:
                    print('CHÚC MỪNG BẠN ĐÃ ĐOÁN ĐÚNG SỐ')
                    print('BẠN ĐƯỢC %d ĐIỂM\n\n' % (i))

                    w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
                    if w == 1:
                        i = 0
                        break
                    elif w == 2:
                        i = 0
                        continue
                    else:
                        print('KHÔNG CÓ SỐ NÀY')
                elif s > a:
                    print('SỐ ĐÓ BÉ HƠN %d'%s)
                else:
                    print('SỐ ĐÓ LỚN HƠN %d' % s)

        elif x == 3:
            i = 0
            a = random.randint(1, 10000000)

            while True:
                i += 1
                while True:
                    try:
                        s = int(input('%d NHẬP 1 SỐ TỰ NHIÊN BẤT KÌ: '% i))
                        break
                    except ValueError:
                        print('Nhap lai')

                if s == a:
                    print('CHÚC MỪNG BẠN ĐÃ ĐOÁN ĐÚNG SỐ')
                    print('BẠN ĐƯỢC %d ĐIỂM\n\n' % (i))

                    w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
                    if w == 1:
                        i = 0
                        break
                    elif w == 2:
                        i = 0
                        continue
                    else:
                        print('KHÔNG CÓ SỐ NÀY')
                elif s > a:
                    print('SỐ ĐÓ BÉ HƠN %d'%s)
                else:
                    print('SỐ ĐÓ LỚN HƠN %d' % s)

        elif x == 4:
            i = 0
            a = random.randint(1, 100000000000)

            while True:
                i += 1
                while True:
                    try:
                        s = int(input('%d NHẬP 1 SỐ TỰ NHIÊN BẤT KÌ: '% i))
                        break
                    except ValueError:
                        print('Nhap lai')

                if s == a:
                    print('CHÚC MỪNG BẠN ĐÃ ĐOÁN ĐÚNG SỐ')
                    print('BẠN ĐƯỢC %d ĐIỂM\n\n' % (i))

                    w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
                    if w == 1:
                        i = 0
                        break
                    elif w == 2:
                        i = 0
                        continue
                    else:
                        print('KHÔNG CÓ SỐ NÀY')
                elif s > a:
                    print('SỐ ĐÓ BÉ HƠN %d'%s)
                else:
                    print('SỐ ĐÓ LỚN HƠN %d' % s)

        elif x == 5:
            i = 0
            a = random.randint(1, 10000000000000000)

            while True:
                i += 1
                while True:
                    try:
                        s = int(input('%d NHẬP 1 SỐ TỰ NHIÊN BẤT KÌ: ' % i))
                        break
                    except ValueError:
                        print('Nhap lai')

                if s == a:
                    print('CHÚC MỪNG BẠN ĐÃ ĐOÁN ĐÚNG SỐ')
                    print('BẠN ĐƯỢC %d ĐIỂM\n\n' % (i))

                    w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
                    if w == 1:
                        i = 0
                        break
                    elif w == 2:
                        i = 0
                        continue
                    else:
                        print('KHÔNG CÓ SỐ NÀY')
                elif s > a:
                    print('SỐ ĐÓ BÉ HƠN %d' % s)
                else:
                    print('SỐ ĐÓ LỚN HƠN %d' % s)