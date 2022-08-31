from multiprocessing.sharedctypes import Value


print("assalmualaikum wr wb")

while True:
    try:
        angkaganjilgenap = (int(input("Masukan Angka Ya : ")))
        if angkaganjilgenap <= 0:
            print('harus dari angka 1 ya')
            continue
        else:
            if angkaganjilgenap % 2:
                print("angka ganjil")
            else:
                print("angka genap")
    except ValueError:
        print("maaf inputan salah atau kosong")
        continue
    else:
        break
