

a=10
b=7


if a>b:
    r=("a bigger than b")
else:
    r=("a smaller than b")
print(f"일반 if문:{r}")

r="a bigger than b"if a>b else"a smaller than b"
print(f"상황 연사자:{r}")



if True:
    if True:
        if True:
            if True:
                b=12
                if True:
                    x=10

print(x+b)