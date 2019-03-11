import sys
bac1_path= "gphuongtrinh/bac1"
sys.path.append(bac1_path)

import ptrinh
import math
class Gptrinh:
    def __init__(self):
        z = 0
        while z < 1:
            while True:
                try:
                    print('-----------------------------------------')
                    print('|           GIẢI PHƯƠNG TRÌNH            |')
                    print('-----------------------------------------')
                    q = int(input('1: ax + b = 0 \n2: ax^2 + bx + c = 0\n3:TỔNG SỐ TỰ NHIÊN BÂT KÌ\n4:GIAI THỪA\n5:ax + by = c\n  a\'x + b\'y = c\'\n\n'))
                    break
                except ValueError:
                    print('nhap lai')
            if q == 1:
                ptrinh.PTbac().pt1()
            elif q == 2:
                print('-----------------------------------------')
                print('|         PHƯƠNG TRÌNH BẬC 2            |')
                print('-----------------------------------------')
                a = float(input('nhập hệ số a: '))
                if a == 0:
                    a = float(input('nhập hệ số b: '))
                    b = float(input('nhập hệ số c: '))
                    if a == 0:
                        print('PHƯƠNG TRÌNH VÔ NGHIỆM')
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
                    else:
                        print('x = %f' % (b / a))
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
                else:
                    b = float(input('nhập hệ số b: '))
                    c = float(input('nhập hệ số c: '))

                    delta = math.pow(b, 2) - 4 * a * c
                    if delta < 0:
                        print('phương trình vô nghiệm')
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
                    if delta == 0:
                        print('X1 = X2 = %f' % (-b / 2 * a))
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
                    if delta > 0:

                        print(
                            'X1 = %f \nX2 = %f' % (
                                ((-b - math.sqrt(delta)) / (2 * a)), (-b + math.sqrt(delta) / (2 * a))))
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                        else:
                            print('KHÔNG CÓ SỐ NÀY')

            elif q == 3:
                a = int(input('NHẬP SỐ ĐẦU TIÊN: '))
                b = int(input('NHẬP SỐ CUỐI CÙNG: '))
                i = 0
                m = 0
                s = 0
                n = 0
                while i < (a - 1):
                    i += 1
                    m += i
                while n < b:
                    n += 1
                    s += n
                print('TỔNG TỪ %d ĐẾN %d LÀ: %d' % (a, b, (s - m)))
                e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                if e == 1:
                    break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                elif e == 2:
                    continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                else:
                    print('KHÔNG CÓ SỐ NÀY')
            elif q == 4:
                a = int(input('NHẬP SỐ ĐẦU TIÊN: '))
                b = int(input('NHẬP SỐ CUỐI CÙNG: '))
                i = 0
                m = 1
                s = 1
                n = 0
                while i < (a - 1):
                    i += 1
                    m *= i
                while n < b:
                    n += 1
                    s *= n
                print('TỔNG TỪ %d ĐẾN %d LÀ: %d' % (a, b, (s / m)))
                e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                if e == 1:
                    break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                elif e == 2:
                    continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                else:
                    print('KHÔNG CÓ SỐ NÀY')
            elif q == 5:
                i = 0
                while i < 1:
                    A1 = int(input('NHẬP a = '))
                    B1 = int(input('NHẬP b = '))
                    C1 = int(input('NHẬP c = '))
                    A2 = int(input('NHẬP a\' = '))
                    B2 = int(input('NHẬP b\' = '))
                    C2 = int(input('NHẬP c\' = '))
                    D = A1 * B2 - A2 * B1
                    Dx = C1 * B2 - C2 * B1
                    Dy = A1 * C2 - A2 * C1
                    if D == 0:
                        if Dx == 0 and Dy == 0:
                            print('INFINITE SOL')
                            e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                            if e == 1:
                                break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                            elif e == 2:
                                continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                            else:
                                print('KHÔNG CÓ SỐ NÀY')
                        if (((Dx == 0) and (Dy != 0)) or (((Dx != 0) and (Dy == 0)))):
                            print('NO SOLUTION')
                            e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                            if e == 1:
                                break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                            elif e == 2:
                                continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                            else:
                                print('KHÔNG CÓ SỐ NÀY')
                    else:
                        print('------------------------')
                        print('     X= %f         ' % (Dx / D))
                        print('     Y= %f         ' % (Dy / D))
                        print('------------------------')
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ GIẢI PHƯƠNG TRÌNH\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ GIẢI PHƯƠNG TRÌNH
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
