a=int(input("введите цену"))
if a<100:
    print("скидки нема")
else:
    a=a-a*0.1
    print("скидка есть")
print(a)