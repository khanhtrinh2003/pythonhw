class bublesort:
    def __init__(self):
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
                print("kết quả")
                print(''.join(str(e) for e in nl))
            w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
            if w == 1:

                i = 0
                break
            elif w == 2:

                continue