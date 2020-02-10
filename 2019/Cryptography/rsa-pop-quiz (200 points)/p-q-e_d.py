from Crypto.Util.number import inverse

q = int(input("q="))
p = int(input("p="))
e = int(input("e="))

phi = (p - 1) * (q - 1)

d = inverse(e, phi)

print("d=\33[35m",d,"\33[0m")
