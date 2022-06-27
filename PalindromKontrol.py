girilenkarakter = input("Lütfen kontrol edilecek kelimeyi veya sayıyı giriniz: ")

if girilenkarakter == girilenkarakter[::-1]:
    print("Yazdığınız kelime/sayı palindromdur.")
else:
    print("Yazdığınız kelime/sayı palindrom değildir.")