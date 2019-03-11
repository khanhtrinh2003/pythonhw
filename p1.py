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
line_path= "line"
sys.path.append(line_path)
compare_path= "compare"
sys.path.append(compare_path)
#import file
import tinhlaisuat
import Gptrinh1
import Guessnumber
import hinhhoc
import encode1
import ziczac
import compare1
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
        ziczac.ziczac1()
    elif x == 8:
        compare1.bublesort()

