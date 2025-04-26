num = int(input("Bir sayı giriniz = "))

while True:
    def faktoriyel(num):
        if num == 0 or num == 1:
            return 1
        else:
            return num * faktoriyel(num - 1)

    print(f"Faktöriyel: {faktoriyel(num)}")
