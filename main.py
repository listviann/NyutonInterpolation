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

    for pair in dots:
        y_arr.append(pair[1])

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

    # ∆3f_0
    for i in range(len(delta_fn_arr2) - 1):
        delta_fn3 = delta_fn_arr2[i + 1] - delta_fn_arr2[i]
        delta_fn_arr3.append(delta_fn3)

    differences.append(delta_fn_arr1)
    differences.append(delta_fn_arr2)
    differences.append(delta_fn_arr3)

    return differences


def sum_factorial(x, k):
    if x < 1:
        return 1
    result = 1
    for i in range(1, k + 1):
        result *= x + i
    return result


def factorial(_n):
    if _n < 1:
        return 1

    result = 1
    for i in range(1, _n + 1):
        result *= i

    return result


def second_nyuton_formula(x_arr, xk, diffs):
    h = x_arr[1] - x_arr[0]
    t = (xk - x_arr[-1]) / h

    p = diffs[0][-1]
    for i in range(len(diffs) - 1):
        p += (sum_factorial(t, i) * diffs[i + 1][-1]) / factorial(i)
    return p


dots = [[4, 11], [6, 27], [8, 50], [10, 83]]
x_dots = [4, 6, 8, 10]
y_dots = [11, 27, 58, 80]
x_k = 20

result = second_nyuton_formula(x_dots, x_k, create_finit_difference(y_dots))
print(f"результат: {result}")