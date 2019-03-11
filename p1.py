#import folder
import sys
gphuongtrinh_path= "gphuongtrinh"
sys.path.append(gphuongtrinh_path)
Game_path= "Game"
sys.path.append(Game_path)
geometry_path= "geometry"
sys.path.append(geometry_path)
encode_path= "encode"
sys.path.append(encode_path)

#import file
import tinhlaisuat
import Gptrinh1
import Guessnumber
import hinhhoc
import encode1
#start
i = 0
while i < 1:
    while True:
        try:
            print('\n\n------------------------------------------')
            print('|                  HOME                  |')
            print('------------------------------------------')
            print('CHỌN SỐ')
            x = int(input('1:TÍNH LÃI SUẤT \n2:GIẢI PHƯƠNG TRÌNH \n3:TRÒ CHƠI ĐOÁN SỐ\n4:HÌNH HỌC\n5:MÃ HÓA\n6:VẼ ĐƯỜNG ZICZAC\n7:SO SÁNH\n'))
            break
        except ValueError:
            print('nhập lại')

    if x == 1:
        tinhlaisuat.Tinhlai()
    elif x == 2:
        Gptrinh1.Gptrinh()
    elif x == 3:
        Guessnumber.Gn()

    elif x == 4:
        hinhhoc.Hh()
    elif x == 5:
        encode1.encode11()
    elif x == 6:
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
    elif x == 8:
        ds = []
        nl = []
        e = 'end'
        a = 0
        while True:
            a += 1
            s = input('nhập số: ')
            if s != e:
                ds.append(s)
                continue
            else:
                print(ds)
                for num in ds:
                    if num not in nl:
                        nl.append(num)

                for m in range(0, len(nl) - 1):
                    for n in range(m, len(nl)):
                        if nl[m] > nl[n]:
                            tempt = nl[m]
                            nl[m] = nl[n]
                            nl[n] = tempt
                print(''.join(str(e) for e in nl))
            w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
            if w == 1:

                i = 0
                break
            elif w == 2:

                continue
