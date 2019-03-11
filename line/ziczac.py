class ziczac1:
    def __init__(self):
        j = 0
        while j < 1:
            n = int(input("NHẬP SÔ ĐƯỜNG ZICZAC: "))
            m = int(input("NHẬP SỐ ĐIỂM TRÊN MỖI ĐƯỜNG "))
            hang = 0
            for i in range(0, m):
                for j in range(0, n * (m - 1) + 1):
                    if j % (2 * (m - 1)) == m - 1 - hang or j % (2 * (m - 1)) == m - 1 + hang:
                        print('*', end="")
                    else:
                        print(" ", end="")
                print("")
                hang = hang + 1
            w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
            if w == 1:
                i = 0
                break
            elif w == 2:
                j = 0
                continue