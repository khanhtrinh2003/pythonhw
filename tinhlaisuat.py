import math
class Tinhlai:
    def __init__(self):
        z = 0
        while z < 1:
            print('-----------------------------------------')
            print('|             TÍNH LÃI SUẤT             |')
            print('-----------------------------------            ------')
            a = int(input('\n1:TÍNH TIỀN NHẬN\n2:TÍNH TIỀN GỬI\n3:TÍNH THỜI GIAN NHẬN TIỀN\n4:QUAY VỀ \n'))

            if a == 4:
                break
            if a == 1:
                b = float(input('NHẬP SỐ TIỀN GỬI: '))
                c = float(input('NHẬP THỜI GIAN(NĂM): '))
                d = float(input('NHẬP SỐ PHẦN TRĂM: '))
                print('SÔ TIỀN NHẬN LÀ: %0.2f' % (b * math.pow((d + 1), c)))
                e = int(input('1: QUAY VỀ BAN ĐẦU\n2:TIẾP TỤC TÍNH LÃI SUẤT\n'))
                if e == 1:
                    break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                elif e == 2:
                    continue  # NẾU e = 2 THÌ QUAY VỀ TÍNH LÃI SUẤT
                else:
                    print('KHÔNG CÓ SỐ NÀY')

            if a == 2:
                b = float(input('NHẬP SỐ TIỀN NHẬN: '))
                c = float(input('NHẬP THỜI GIAN(NĂM): '))
                d = float(input('NHẬP SỐ PHẦN TRĂM: '))
                print('SÔ GỬI LÀ: %0.2f' % (b / math.pow((d + 1), c)))
                e = int(input('1: QUAY VỀ BAN ĐẦU\n2:QUAY VỀ TÍNH LÃI SUẤT\n'))
                if e == 1:
                    break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                elif e == 2:
                    continue  # NẾU e = 2 THÌ QUAY VỀ TÍNH LÃI SUẤT
                else:
                    print('KHÔNG CÓ SỐ NÀY')
            if a == 3:
                b = float(input('NHẬP SỐ TIỀN GỬI: '))
                c = float(input('NHẬP SỐ TIỀN NHẬN: '))
                d = float(input('NHẬP SỐ PHẦN TRĂM: '))
                print('THỜI GIAN LÀ: %0.2f NĂM' % math.log(c / b, d + 1))
                e = int(input('1: QUAY VỀ BAN ĐẦU\n2:TIẾP TỤC TÍNH LÃI SUẤT\n'))
                if e == 1:
                    break  # NẾU e = 1 THÌ QUAY VỀ BAN ĐẦU
                elif e == 2:
                    continue  # NẾU e = 2 THÌ QUAY VỀ TÍNH LÃI SUẤT
                else:
                    print('KHÔNG CÓ SỐ NÀY')