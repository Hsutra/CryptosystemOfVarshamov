import string
import itertools
import random
import math

def genvector(n, p):
    vector = list()
    vector.append(random.randint(1, 10))
    for i in range(n - 1):
        sum = 0
        for j in range(len(vector)):
            sum += vector[j] * (p - 1)
        vector.append(random.randint(sum + 1, sum + 10))
    return vector

def gensec(vector):
    sum = 0
    for i in vector:
        sum += i
    m = random.randint(sum + 1, sum + 10)#модуль(должен быть больше суммы элементов вектора)
    nlist = []
    for i in range(2, m):
        if (math.gcd(m, i) == 1):
            nlist.append(i)
    e = random.choice(nlist)#множитель(e,m) = 1
    seclist = [m, e]
    return seclist

def genopenvector(vector, m, e):
    vectorB = list()
    for i in range(len(vector)):
        vectorB.append(((vector[i] * e) % m))
    return vectorB

def genclosedvector(vectorB, m, e):
    u = 0
    for i in range(m - 1):
        if ((e * i) % m) == 1:
            u = i  # u = e^-1
            break
    vectorC = []
    for i in range(len(vectorB)):
        vectorC.append((vectorB[i] * u) % m)
    return vectorC
def gencodes(n, p, a): #n-длина кодового слова, p-разрядность, a-число(a <= n)
    num_system = []
    for i in range(p):
        num_system.append(i)
    Codes = []
    set = list(itertools.product(num_system, repeat=n))
    for i in set:
        sum = 0
        k = 1
        for j in i:
            sum += k * j
            k += 1
        if (sum % (n + 1) == a):
            Codes.append(i)
    Alphabet = list(" " + string.ascii_letters + string.digits + string.punctuation)
    CodeWords = {}
    random.shuffle(Codes)
    j = 0
    if (len(Codes) != 0):
        for i in Alphabet:
            CodeWords[i] = Codes[j]
            j += 1
    return CodeWords
print(string.punctuation)
def encrypt(plane_text, vectorA, CodeWords):
    shifr = []
    sum = 0
    for i in plane_text:
        for key, value in CodeWords.items():
            if (i == key):
                sum = 0
                k = 0
                for num in value:
                    sum += vectorA[k] * num
                    k += 1
        shifr.append(sum)
    return shifr

def decrypt(shifr_text, vectorB, CodeWords, m, e):
    str = str_to_int(shifr_text)
    txt = ""
    u = 0
    for i in range(m - 1):
        if ((e * i) % m) == 1:
            u = i  # u = e^-1
            break
    vectorC = []
    for i in range(len(vectorB)):
        vectorC.append((vectorB[i] * u) % m)
    for i in str:
        for key, value in CodeWords.items():
            sum = 0
            k = 0
            for num in value:
                sum += vectorC[k] * num
                k += 1
            if (sum == i):
                txt += key
                break
    return txt

def str_to_int(str):
    l = len(str)
    integ = []
    i = 0
    while i < l:
        s_int = ''
        a = str[i]
        while '0' <= a <= '9':
            s_int += a
            i += 1
            if i < l:
                a = str[i]
            else:
                break
        i += 1
        if s_int != '':
            integ.append(int(s_int))
    return integ
n = 6# n >= 3
p = 3
a = 0
CodeWords = gencodes(n, p, a)
VectorA = genvector(n, p) #элемент сверхрастущего вектора должен быть больше суммы всех предыдущих * р - 1
m, e = gensec(VectorA)
print("Модуль/Множитель: ", m, e)
VectorB = []
for i in range(len(VectorA)):
    VectorB.append(((VectorA[i] * e) % m))
print("Закрытый ключ:", VectorA)
print("Открытый ключ:", VectorB)
plane_text = "CODE RRW BAC AB"
shifr_text = str(encrypt(plane_text, VectorA, CodeWords))
print("Открытый текст: ", plane_text)
print("Шифр текст: ", shifr_text)
print("Расшифрованный текст: ", decrypt(shifr_text, VectorB, CodeWords, m, e))
