import math
class Hh:
    def __init__(self):
        while True:
            try:
                print('-----------------------------------------')
                print('|                HÌNH HỌC                |')
                print('-----------------------------------------')
                a = int(input('1:TAM GIÁC\n2:HÌNH VUÔNG\n3:HÌNH CHỮ NHẬT\n4:HÌNH TRÒN\n'))
                break
            except ValueError:
                print('nhap lai')
        if a == 1:
            i = 0
            while i < 1:
                z = int(input('1:CHU VI TAM GIÁC\n2:DIỆN TÍCH TAM GIÁC\n'))
                if z == 1:
                    m = float(input('NHẬP CẠNH 1: '))
                    n = float(input('NHẬP CẠNH 2: '))
                    k = float(input('NHẬP CẠNH 3: '))
                    if m <= 0 or n <= 0 or k <= 0:
                        print('CẠNH PHẢI LÀ SỐ DƯƠNG\n')
                        continue
                    else:
                        if m + n > k and m + k > n and n + k > m:
                            print('CHU VI TAM GIÁC LÀ: %f' % (m + n + k))
                            e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ TAM GIÁC\n'))
                            if e == 1:
                                break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                            elif e == 2:
                                continue  # NẾU e = 2 THÌ QUAY VỀ TAM GIÁC
                            else:
                                print('KHÔNG CÓ SỐ NÀY')

                        else:
                            print('ĐÂY KHÔNG PHẢI 3 CẠNH TAM GIÁC')

                elif z == 2:
                    m = float(input('NHẬP CẠNH 1: '))
                    n = float(input('NHẬP CẠNH 2: '))
                    k = float(input('NHẬP CẠNH 3: '))
                    if m <= 0 or n <= 0 or k <= 0:
                        print('CẠNH PHẢI LÀ SỐ DƯƠNG\n')
                        continue
                    else:
                        h = (m + n + k) / 2
                        if m + n > k and m + k > n and n + k > m:
                            print('DIỆN TÍCH TAM GIÁC LÀ: %f' % math.sqrt(h * (h - m) * (h - n) * (h - k)))
                            e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ TAM GIÁC\n'))
                            if e == 1:
                                break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                            elif e == 2:
                                continue  # NẾU e = 2 THÌ QUAY VỀ TAM GIÁC
                            else:
                                print('KHÔNG CÓ SỐ NÀY')

                        else:
                            print('ĐÂY KHÔNG PHẢI 3 CẠNH TAM GIÁC')
        elif a == 2:
            i = 0
            while i < 1:
                z = int(input('1:CHU VI HÌNH VUÔNG\n2:DIỆN TÍCH HÌNH VUÔNG\n'))
                if z == 1:
                    m = float(input('NHẬP CẠNH: '))
                    if m <= 0:
                        print('CẠNH PHẢI LÀ SỐ DƯƠNG\n')
                        continue
                    else:
                        print('CHU VI HÌNH VUÔNG LÀ: %f' % (m * 4))
                        e = int(input('\n1:QUAY VỀ BAN ĐẦU\n2:QUAY VỀ HÌNH VUÔNG\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ HÌNH VUÔNG
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
                elif z == 2:
                    m = float(input('NHẬP CẠNH: '))
                    if m <= 0:
                        print('CẠNH PHẢI LÀ SỐ DƯƠNG\n')
                        continue
                    else:
                        print('DIỆN TÍCH HÌNH VUÔNG LÀ: %f' % (m ** 2))
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ HÌNH VUÔNG\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ HÌNH VUÔNG
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
        elif a == 3:
            i = 0
            while i < 1:
                z = int(input('1:CHU VI HÌNH CHỮ NHẬT\n2:DIỆN TÍCH HÌNH CHỮ NHẬT\n'))
                if z == 1:
                    m = float(input('NHẬP CẠNH 1: '))
                    n = float(input('NHẬP CẠNH 2: '))
                    if m <= 0 or m <= 0:
                        print('CẠNH PHẢI LÀ SỐ DƯƠNG')
                        continue
                    else:
                        print('CHU VI HÌNH CHỮ NHÂT: %f' % (m + n) * 2)
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ TAM GIÁC\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ TAM GIÁC
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
                elif z == 2:
                    m = float(input('NHẬP CẠNH 1: '))
                    n = float(input('NHẬP CẠNH 2: '))
                    if m <= 0 or m <= 0:
                        print('CẠNH PHẢI LÀ SỐ DƯƠNG')
                        continue
                    else:
                        print('DIỆN TÍCH HÌNH CHỮ NHÂT: %f' % (m * n))
                        e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ TAM GIÁC\n'))
                        if e == 1:
                            break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                        elif e == 2:
                            continue  # NẾU e = 2 THÌ QUAY VỀ TAM GIÁC
                        else:
                            print('KHÔNG CÓ SỐ NÀY')
        elif a == 4:
            r = float(input('NHẬP BÁN KÍNH: '))
            if r <= 0:
                print('BÁN KÍNH PHẢI LÀ SỐ DƯƠNG!')

            else:
                s = int(input('1:CHU VI HÌNH TRÒN\n2:DIỆN TÍCH HÌNH TRÒN\n'))
                if s == 1:
                    print('CHU VI HÌNH TRÒN LÀ %f' % (math.pi * (r * 2)))
                elif s == 2:
                    print('DIỆN TÍCH HÌNH TRÒN LÀ %f' % (math.pi * (r ** 2)))
