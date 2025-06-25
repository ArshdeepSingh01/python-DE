a=8
if a>10:
    print("No")
elif 10>a>7:
    print("Yes")
else:
    print("No no")

print("Arshdeep") if a==8 else print("Singh")

match a:
    case 8: print("Sher")
    case 2: print("Non Sher")
    case _: print("Haha")