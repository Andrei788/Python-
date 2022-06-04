S = float(input("введите сумму вклада: "))
time = int(1)
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
for i in per_cent:
    p = S / 100.0 * per_cent[i]
    print(int(p), per_cent.get(i))
    print(int(S), per_cent.values())

maxi = round(max(per_cent.values()) / 100 * S)
bank = max(per_cent, key=per_cent.get)
print(bank,maxi)