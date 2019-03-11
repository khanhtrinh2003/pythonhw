import math

class PTbac:
    def pt1():
        print('-----------------------------------------')
        print('|         PHƯƠNG TRÌNH BẬC 1            |')
        print('-----------------------------------------')
        a = float(input('nhập hệ số a: '))
        b = float(input('nhập hệ số b: '))
        if a == 0:
            print('PHƯƠNG TRÌNH VÔ NGHIỆM')

        else:
            print('x = %f' % (b / a))
