# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import cmath

def quadratic_formula(a, b, c):
    # 計算判別式
    discriminant = b**2 - 4*a*c

    # 判斷解的情況
    if discriminant > 0:
        # 有兩個實根
        root1 = (-b + discriminant**0.5) / (2*a)
        root2 = (-b - discriminant**0.5) / (2*a)
        return root1, root2
    elif discriminant == 0:
        # 有一個重根
        root = -b / (2*a)
        return root, root
    else:
        # 有兩個虛根
        real_part = -b / (2*a)
        imaginary_part = cmath.sqrt(abs(discriminant)) / (2*a)
        root1 = complex(real_part, imaginary_part)
        root2 = complex(real_part, -imaginary_part)
        return root1, root2

# 輸入係數
a = float(input("請輸入a: "))
b = float(input("請輸入b: "))
c = float(input("請輸入c: "))

# 解方程式
roots = quadratic_formula(a, b, c)

# 輸出解
print("方程式的解為:", roots)
