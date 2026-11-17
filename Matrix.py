print("Выберете необходимое:")
choose = int(input("1.Определитель матрицы \n"
                   "2.Транспонирование матрицы\n"
                   "3.Умножение матриц\n"
                   "4.Умножение матрицы на число\n"
                   "5.Поиск обратной матрицы\n"
                   "6.Решение квадратных матриц\n"))





# Определитель
def det(mat):
    n = len(mat)
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    deter = 0
    for i in range(n):
        minor = [row[:i] + row[i + 1:] for row in mat[1:]]
        deter += ((-1) ** i * mat[0][i] * det(minor))
    return deter





# Транспонирование
def trans(mat):
    retC = []
    for j in range(len(mat[0])):
        retR = []
        for i in range(len(mat)):
            retR.append(mat[i][j])
        retC.append(retR)
    return retC





# Умножение
def mylt(mat1, mat2):
    if len(mat1[0]) != len(mat2):
        return 0
    mat = [[0] * len(mat2[0]) for _ in range(len(mat1))]
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                mat[i][j] += (mat1[i][k] * mat2[k][j])
    return mat




# Умножение на число
def mylt_num(n,mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            mat[i][j] *= n
    return mat




# Обратная матрица
def rev(mat):
    d = det(mat)
    if d == 0:
        return "Матрица вырождена, и не имеет обратной"
    add = []
    for i in range(len(mat)):

        ct = []
        for j in range(len(mat)):
            minor = [row[:j] + row[j + 1:] for row in mat[:i] + mat[i + 1:]]
            ct.append(det(minor) * (-1) ** (i+j))
        add.append(ct)

    return mylt_num(1/d, trans(add))






if choose == 1:
    print("Введите квадратную матрицу:\n")
    firstRow = list(map(float, input().split()))
    otherRow = [list(map(float, input().split())) for _ in range(len(firstRow) - 1)]
    mat = [firstRow] + otherRow
    print(f'Определитель вашей матрицы: {det(mat)}')




if choose == 2:
    print("Введите матрицу:\n")
    mat = []
    while True:
        try:
            line = list(map(float, input().split()))
        except EOFError:
            break
        if not line:
            break
        mat.append(line)
    print("Транспонированная матрица: \n")
    for r in trans(mat):
        for c in r:
            print(c, end=' ')
        print()




if choose == 3:
    print("Введите 2 матрицы размерностью nXq и qXm")
    mat1 = []
    while True:
        try:
            line = list(map(float, input().split()))
        except EOFError:
            break
        if not line:
            break
        mat1.append(line)
    mat2 = []
    while True:
        try:
            line = list(map(float, input().split()))
        except EOFError:
            break
        if not line:
            break
        mat2.append(line)
    rez = mylt(mat1, mat2)
    if rez == 0:
        print('Такие матриц умножать нельзя!')
    else:
        print("Матрица-произведение: \n")
        for r in rez:
            for c in r:
                print(c, end=' ')
            print()




if choose == 4:
    mat = []
    n = float(input("Введите число: "))
    print("Введите матрицу: ")
    while True:
        try:
            line = list(map(float, input().split()))
        except EOFError:
            break
        if not line:
            break
        mat.append(line)
    print("Умноженая матрица: \n")
    for r in mylt_num(n,mat):
        for c in r:
            print(c, end=' ')
        print()


if choose == 5:
    print("Введите квадратную матрицу:\n")
    firstRow = list(map(float, input().split()))
    otherRow = [list(map(float, input().split())) for _ in range(len(firstRow) - 1)]
    mat = [firstRow] + otherRow
    if not isinstance(rev(mat), str):
        print(f'Обратная вашей матрицы:\n')
        for r in  rev(mat):
            for c in r:
                print(c, end=' ')
            print()
    else: print(rev(mat))



if choose == 6:

    print("Введите квадратную матрицу:\n")
    firstRow = list(map(float, input().split()))
    otherRow = [list(map(float, input().split())) for _ in range(len(firstRow) - 1)]
    mat = [firstRow] + otherRow
    mat_inv = rev(mat)
    if not isinstance(mat_inv, str):
        print("Введите свободные члены:\n")
        fr = []
        while True:
            try:
                line = list(map(float, input().split()))
            except EOFError:
                break
            if not line:
                break
            fr.append(line)
        if len(fr) != 1:
            print(f'Решение вашей матрицы: \n')
            for r in mylt(mat_inv,fr):
                for c in r:
                    print(c, end=' ')
                print()
        else:
            print(f'Решение вашей матрицы: \n')
            for r in mylt(mat_inv,trans(fr)):
                for c in r:
                    print(c, end=' ')
                print()
    else: print(mat_inv)