class encode11:
    def __init__(self):
        m = 0
        while m < 1:
            key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u',
                   'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c',
                   'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k',
                   'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S',
                   'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A',
                   'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I',
                   'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M', ' ': ' ', '0': '!', '4': '@', '6': '#',
                   '8': '$', '1': '%', '3': '^', '5': '&', '7': '*', '9': '(', '2': ')', 'ă': 'a8',
                   'Ă': 'A8', 'â': 'a6', 'Â': 'A6', 'ê': 'e6', 'Ê': 'E6', 'ô': 'o6', 'Ô': 'O6', 'ư': 'u7',
                   'ơ': 'o7', 'Ư': 'U7', 'Ơ': 'O7', 'đ': 'd9', 'Đ': 'D9','a8': 'ă',
                   'A8': 'Ă', 'a6': 'â', 'A6': 'Â', 'e6': 'ê', 'E6': 'Ê', 'O6': 'Ô', 'o6': 'ô', 'u7': 'ư',
                   'o7': 'ơ', 'U7': 'Ư', 'O7': 'Ơ', 'd9': 'đ', 'D9': 'Đ',
                   }
            chuoi = input('NHẬP CÂU CẦN MÃ HÓA HOẶC GIẢI MÃ: ')

            password = []

            for i in range(len(chuoi)):
                x = key[chuoi[i]]
                password.append(x)

            print(''.join(str(e) for e in password))
            w = int(input('1: THOÁT RA\n2: TIẾP TỤC\n'))
            if w == 1:
                i = 0
                break
            elif w == 2:
                i = 0
                continue

