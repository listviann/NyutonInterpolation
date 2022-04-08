import sympy


# вариант 19

#      x=20
# -------------------------
# | X | 4  | 6  | 8  | 10 |
# |-----------------------|
# | Y | 11 | 27 | 50 | 83 |
# -------------------------

# 1^2 + 2^2 + 3^2 + ... (n - 1)^2 + n^2

# 1) составляем таблицу конечных разностей
# 2) Смотрим, заданная точка x_k ближе к началу исходной таблицы или к концу
# 3) Для точки X_k, близкой к началу таблицы: первая формула Ньютона:
# 4) Для точки x_k, близкой к концу таблицы: вторая формула Ньютона

# конечные разности
def create_finit_difference(y_arr):
    differences = []
    delta_fn_arr1 = []
    delta_fn_arr2 = []
    delta_fn_arr3 = []

    # [16, 23, 33]

    # ∆f_0 = 16
    # ∆f_1 = 23
    # ∆f_2 = 33
    for i in range(len(y_arr) - 1):
        delta_fn1 = y_arr[i + 1] - y_arr[i]
        delta_fn_arr1.append(delta_fn1)


    # [7, 10]

    # ∆2f_0 = 7
    # ∆2f_1 = 10
    for i in range(len(delta_fn_arr1) - 1):
        delta_fn2 = delta_fn_arr1[i + 1] - delta_fn_arr1[i]
        delta_fn_arr2.append(delta_fn2)

    # [3]

    # ∆3f_0 = 3
    for i in range(len(delta_fn_arr2) - 1):
        delta_fn3 = delta_fn_arr2[i + 1] - delta_fn_arr2[i]
        delta_fn_arr3.append(delta_fn3)

    differences.append(y_arr)
    differences.append(delta_fn_arr1)
    differences.append(delta_fn_arr2)
    differences.append(delta_fn_arr3)

    # print(delta_fn_arr1)
    # print(delta_fn_arr2)
    # print(delta_fn_arr3)

    #print(f"таблица {differences}")
    return differences


def factorial(_n):
    if _n == 0 or _n == 1:
        return 1

    res = 1
    for i in range(_n):
        res *= i + 1

    return res


def sum_factorial(x, k):
    res = x
    if x == 0:
        return 1
    for i in range(k):
        res *= x + i + 1

    return res


def second_nyuton_formula(x_arr, xk, y_arr):
    diffs = create_finit_difference(y_arr)
    print(diffs)
    h = abs(x_arr[1] - x_arr[0])
    #print(h)
    t = (xk - x_arr[-1]) / h
    #print(x_arr[-1])

    p = diffs[0][-1]
    for i in range(len(diffs) - 1):
        p += (sum_factorial(t, i) * diffs[i + 1][-1]) / factorial(i + 1)
    return p


x_dots = [4, 6, 8, 10]
y_dots = [11, 27, 50, 83]
x_k = 10

result = second_nyuton_formula(x_dots, x_k, y_dots)
print(f"результат: {result}")

#print(create_finit_difference(y_dots))
