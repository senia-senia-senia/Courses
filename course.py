import os
import time
errurl = "output3.txt.txt"
inp = open('input.txt', 'r')
output = open('output.txt' , 'w')
trpstrf = open('TRPSTR.txt', 'r')
parametr = open('parametr.txt', 'a')
# Триплетный синтаксические знаки
trpBeg = "$"
trpEnd = ";"
trpAp = "'"
trpEq = "="
trpDot = "."
trpCol = ":"
trpSharp = "#"
# Коды ошибок
errNoerr = "0"
errProg = "1"
errBeg = "2"
errEnd = "3"
errAp = "4"
errEq = "5"
errDot = "6"
errCol = "7"
errSharp = "8"
# Точка начала программы. Главная функция Нужно чтобы название
# триплета было из двух букв, исправить
def main():
    a = []
    trpstr = trpstrf.readline()
    print(trpstr)
    func = inp.read()
    print(func)
    a = parseInp(func)
    if a[3] == 'trpSort':
        print('1')
        if a[1]!= '' and a[2]!= '' and a[0]!= '':
            print('Неверные параметры получены на входе', file = output)
        else:
            ishod = trpSort(trpstr) 
            print(ishod,file = output)
    elif a[3] == 'trpDelPref':
        if a[1]!= '' and a[2]!= '':
            print('Неверные параметры получены на входе', file = output)
        else:
            ishod = trpDelPref(trpstr,a[0])
            print(ishod,file = output)
    elif a[3] == 'trpGet':
        if a[0]!= '' and a[1]!='' and a[2]!='':
            ishod = trpGet(trpstr, a[0],a[1],a[2])
            print(ishod,file = output)
        else:
            print('Неверные параметры получены на входе', file = output)
    elif a[3] == 'trp_Get':
        print('4')
        if a[0]!= '' and a[1]!='' and a[2]!='':
            ishod = trp_Get(trpstr, a[0],a[1],a[2])
            print(ishod,file = output)
        else:
            print('Неверные параметры получены на входе', file = output)    
    elif a[3] == 'trpGetName':
        print('5')
        if a[1]!= '' and a[2]!= '' and a[0]!= '':
            print('Неверные параметры получены на входе', file = output)
        else:
            ishod = trpGetName(trpstr)
            print(ishod,file = output)
    elif a[3] == 'del_trp':
        print('6')
        if a[2]!= '':
            print('Неверные параметры получены на входе', file = output)
        else:
            ishod = del_trp(trpstr, a[0], a[1])
            print(ishod,file = output)
    elif a[3] == 'trpGoNext':
        print('7')
        if a[1]!= '' and a[2]!= '' and a[0]!= '':
            print('Неверные параметры получены на входе', file = output)
        else:
            ishod = trpGoNext(trpstr)
            print(ishod,file = output)
    elif a[3] == 'trpGoEnd':
        print('8')
        if a[1]!= '' and a[2]!= '' and a[0]!= '':
            print('Неверные параметры получены на входе', file = output)
        else:
            ishod = trpGoEnd(trpstr)
            print(ishod,file = output)
    elif a[3] == 'trpGoName':
        print('9')
        if a[1]!= '' and a[2]!= '' and a[0]!= '':
            print('Неверные параметры получены на входе', file = output)
        else:
            ishod = trpGoName(trpstr)
            print(ishod,file = output)
    elif a[3] == 'trp_GetFirst':
        print('10')
        if a[1]!= '' and a[2]!= '' and a[0]!= '':
            print('Неверные параметры получены на входе', file = output)
        else:
            ishod = trp_GetFirst(trpstr)
            print(ishod,file = output)
    else:
        print('11')
        tstr = []
        trstrt = []
        tstr = parseOne(func)
        trstrt = tstr[2]
        ishod = trpAdd(trpstr, tstr[0], tstr[1], trstrt[0], trstrt[1])
        print(ishod,file = output)


#1func
def trpAddStr(trpstr, pref, name, value, rem , isStr):#work it define
    val = value
    if isStr: val = trpAp + value + trpAp
    if rem != 'NULL':
        newtrp = trpBeg + pref + trpDot + name+rem + trpEq + val + trpEnd
    else :
        newtrp = trpBeg + pref + trpDot + name + trpEq + val + trpEnd
    return trpAddStrOld(trpstr, newtrp, True)

#2func
def trpAdd(trpstr, pref, name, value, isStr):
    return trpAddStr(trpstr, pref, name, value, "", isStr)
#3func
def trpAddInt(trpstr, pref, name, v):
    i = [trpstr, pref, name, v]
    return trpAdd(trpstr, pref, name, v, False)

#4func
def trpMerge(trpstr, strpsSecond):
    trpstr = parseAll(trpstr)
    trpsSecond = parseAll(strpsSecond)
    newtrps = {}
    for key in trpstr:
        if newtrps.get(key) == None:
            newtrps[key] = trpstr[key]
    for key in trpsSecond:
        if newtrps.get(key) == None:
            newtrps[key] = trpsSecond[key]
    return trpArrToStr(newtrps)

#5func
def trpSort(trpstr):
    trps = parseAll(trpstr)
    return trpArrToStr(trps)

#6func
def trpDelPref(trpstr, pdel_trpref):
    i = [trpstr, pdel_trpref]
    oldtrps = parseAll(trpstr)
    newtrps = {}
    for key in oldtrps:
        trp = oldtrps[key]
        (obj, par, (val, isStr)) = trp
        if obj != pdel_trpref:
            newtrps[key] = trp 
    return trpArrToStr(newtrps)

#7func
#CHek
def trpGet(trpstr, pref, name, value):
    trps = parseAll(trpstr)
    for key in trps:
        trp = trps[key]
        (obj, par, (val, isStr)) = trp
        if obj == pref and name == par:
            return (True, val, isStr)
    return (False, "", False)

#8func
#CHek
def trp_Get(trpstr, pref, name, value):
    (isGood, val, isStr) = trpGet(trpstr, pref, name, value)
    return (isGood, val)

#9func
def trpGetName(trpstr):
    (obj, par, val, rest) = parseOne(trpstr)
    return (obj + trpDot + par)

#10func
def del_trp(trpstr, pref, name):
    oldtrps = parseAll(trpstr)
    newtrps = {}
    for key in oldtrps:
        trp = oldtrps[key]
        (obj, par, (val, isStr)) = trp
        if not (obj == pref and name == par):
            newtrps[key] = trp
    return trpArrToStr(newtrps)

#11func
def trpGoNext(trpstr):
    (obj, par, val, rest) = parseOne(trpstr)
    return rest

#12func
def trpGoEnd(trpstr):
    restOld = trpstr
    (obj, par, val, rest) = parseOne(trpstr)
    while rest != "":
        restOld = rest
        (obj, par, val, rest) = parseOne(rest)
    return restOld

#13func
def trpGoName(trpstr):
    return trpGetName(trpstr)

#14func
def trp_GetFirst(trpstr):
    (obj, par, val, rest) = parseOne(trpstr)
    return (obj + trpDot + par, val)

#Вспомогательные функции
#Вспомогательные функции
#Вспомогательные функции
#Вспомогательные функции
#Вспомогательные функции
#Вспомогательные функции
#Вспомогательные функции

def trpAddStrOld(strps, snewtrp, replace):
    trps = parseAll(strps)
    newtrps = parseAll(snewtrp)
    for key in iter(newtrps):
        if trps.get(key) == None or replace:
            trps[key] = newtrps[key]
    return trpArrToStr(trps)

def trpDelExact(strps, strpdel):
    trps = parseAll(strps)
    (obj, par, val, rest) = parseOne(strpdel)
    deleted = True
    try:
        del trps[obj + trpDot + par]
    except Exception as e:
        deleted = False
    return (trpArrToStr(trps), deleted)

def trpDelByObj(strps, objdel):
    oldtrps = parseAll(strps)
    newtrps = {}
    for key in oldtrps:
        trp = oldtrps[key]
        (obj, par, (val, isStr)) = trp
        if obj != objdel:
            newtrps[key] = trp
    return trpArrToStr(newtrps)
def parseInp(s):
    if (':' in s) == True:
        obj = ""
        par = ""
        val = ""
        oper = ""
        # Проверка символа начала триплета
        testErr(s,0,trpBeg,errBeg)
        i = 1
        print("1")
        # Считывание первой части триплета и проверка наличия точки
        (obj, i) = readToControl(s,i)
        if (s.find('.')!= -1) and (s.find('.')<s.find(':')):
            testErr(s,i,trpDot,errDot)
            i+=1
            # Считывание второй части триплета
            (par, i) = readToControl(s,i)
            print(par)
            #i += 1
            print("2",i)
            if (s.find('=') != -1) and (s.find('=')<s.find(':')):
                #Проверка  наличия знака равенства
                testErr(s,i,trpEq,errEq)
                i += 1
                print("3")
                # Проверка наличия апострофа
                isStr = False
                if len(s) > i and s[i] == trpAp:
                    i += 1
                    isStr = True
                print("4")
                # Считывание третьей части триплета
                while len(s) > i and s[i] != trpAp and s[i] != trpEnd:
                    print("ap: " + s[i])
                    val += s[i]
                    i += 1
                # Если строка, то проверяем закрывающий апостроф
                if isStr:
                    testErr(s,i,trpAp,errAp)
                    i += 1
        #проверка наличия знака двоеточия
        testErr(s,i,trpCol,errCol)
        i += 1
        print("3")
        # Проверка наличия '#'
        if len(s) > i and s[i] == trpSharp:
            i += 1
        print("4")
        # Считывание третьей части триплета
        while len(s) > i and s[i] != trpSharp and s[i] != trpEnd:
            print("ap: " + s[i])
            oper += s[i]
            i += 1
        # Если строка, то проверяем закрывающий '#'
        testErr(s,i,trpSharp,errSharp)
        i += 1
        # Проверка знака завершения триплета
        testErr(s,i,trpEnd,errEnd)
        i += 1
        print("5")
    else:
        oper = 'trpAdd'
    return(obj,par,val,oper)

# Функция считывания триплета
def parseOne(s):
    obj = ""
    par = ""
    val = ""
    # Проверка символа начала триплета
    testErr(s,0,trpBeg,errBeg)
    i = 1
    print("1")
    # Считывание первой части триплета и проверка наличия точки
    (obj, i) = readToControl(s,i)
    testErr(s,i,trpDot,errDot)
    i += 1
    print("2")
    # Считывание второй части триплета и проверка наличия знака равенства
    (par, i) = readToControl(s,i)
    testErr(s,i,trpEq,errEq)
    i += 1
    print("3")
    # Проверка наличия апострофа
    isStr = False
    if len(s) > i and s[i] == trpAp:
        i += 1
        isStr = True
    print("4")
    # Считывание третьей части триплета
    while len(s) > i and s[i] != trpAp and s[i] != trpEnd:
        print("ap: " + s[i])
        val += s[i]
        i += 1
    # Если строка, то проверяем закрывающий апостроф
    if isStr:
        testErr(s,i,trpAp,errAp)
        i += 1
    # Проверка знака завершения триплета
    testErr(s,i,trpEnd,errEnd)
    i += 1
    print("5")
    return (obj, par, (val, isStr), s[i:])
def parseAll(text):
    if text == "":
        return {}
    trps = {}
    while text != "":
        (obj, par, val, text) = parseOne(text)
        trps[obj + trpDot + par] = (obj, par, val)
    return trps

def trpToStr(trp):
    (obj, par, (val, isStr)) = trp
    if isStr:
        val = trpAp + val + trpAp;
    return (trpBeg + obj + trpDot + par + trpEq + val + trpEnd) 

def trpArrToStr(trps):
    str = ""
    for key in trps:
        str+=trpToStr(trps[key])
    return str

def testErr(s, i, msg):
    if len(s) <= i:
        raiseErr(msg)
# Проверка вхождения индекса i в строку s. Проверка s[i] = test.
# Создание ошибки с сообщение msg, если первые два условия неверны     
def testErr(s, i, test, msg):
    print(str(i)+" "+str(test)+" "+msg)
    if len(s) <= i or test != s[i]:
        raiseErr(msg)
# Функция печати ошибки s в файл и вызова исключения   
def raiseErr(s):
    f = open(errurl, "w")
    f.write("$Q.ERRTRP="+s+";")
    f.close()
    raise Exception("raiseErr " + s)
# Проверяет, является ли символ c управляющим
def isControl(c):
    return c == trpBeg or c == trpDot or c == trpEq or c == trpEnd or c == trpSharp or c == trpCol
# Считывает подстроку строки s, начиная с позиции start и до появления управляющего символа
def readToControl(s,start):
    obj = ""
    i = start
    while len(s) > i and not isControl(s[i]):
        obj += s[i]
        i += 1
    return (obj, i)
def ChekOut(i):
    while a[i] == '':
        schet = shet + 1
        i+=1
    return('Данная функция предпологает ', schet,'аргументов')
    

def helpFunction(cmd = 0 ):
    if cmd == 0:
        print('''1.trpAddStr() --- Функция добавляет триплет в триплексную строку.''')
        print('''2.trpAdd() --- Функция работает как trpaddstr.''')   
        print('''3.trpAddInt() --- Функция добавляет триплет c целым значением в триплексную строку''')
        print('''4.trpMerge() --- Функция сливает две триплексных строки.''')
        print('''5.trpSort() --- Функция сортирует триплексную строку в лексикографическом порядке имен. ''')
        print('''6.trpDelPref() --- Функция удаляет все триплеты с заданным префиксом из триплексной строки.''')
        print('''7.trpGet() --- Функция ищет по префиксу объекта pref и имени name в строке trpstr значение  триплета и кладет его  в текстовую строку value, тип значение в type. Возвращает true, если значение есть, иначе false.''')
        print('''8.trp_Get() --- Тоже, но без type.''')
        print('''9.trpGetName() --- Функция возвращает имя первого триплета в триплексной строке.''')
        print('''10.del_trp() --- Функция удаляет  триплеты с заданным префиксом и именем  из триплексной строки. ''')
        print('''11.trpGoNext() --- Функция переводит указатель на следующий триплет в строке.''')
        print('''12.trpGoEnd() --- Функция переводит указатель на конец триплексной строчки.''')
        print('''13.trpGoName() --- Функция аналогична trpgetname''')
        print('''14.trp_GetFirst() --- Функция возвращает указатель на первый триплет (префикс) и берет его значение.''')
        print('''15.helpFunction() --- Функция возвращает подробную информацию о функциях, а также о каэждой из функций по отдельности.''')
        print('хочешь выйти из помошника по функциям?(Y/N)')
    elif cmd == 'trpAddStr':
        cmd = print('''Функция добавляет триплет в триплексную строку.
    Если триплет уже был, то заменяет значение.
    Возвращает обновленную триплексную строку.
    Параметры:
    trpstr -  строка триплетов;
    pref   -  префикс;
    name – имя;
    value – значение триплета;
    type – тип триплета;
    rem – примечание.
                ''')
    elif cmd == 'trpAdd':
        cmd = print('''Функция добавляет триплет в триплексную строку.
    Если триплет уже был, то заменяет значение.
    Возвращает обновленную триплексную строку.
    Параметры:
    trpstr -  строка триплетов;
    pref   -  префикс;
    name – имя;
    value – значение триплета;
    type – тип триплета.
    ''')
    elif cmd == 'trpAddInt' :
        cmd = print('''Функция добавляет триплет c целым значением в триплексную строку.
    Если триплет уже был, то заменяет значение.
    Возвращает обновленную триплексную строку.
    Параметры:
    trpstr -  строка триплетов,
    pref   -  префикс,
    name – имя,
    v –  значение. 
    ''')
    elif cmd == 'trpMerge' :
        cmd = print('''Функция сливает две триплексных строки.
    Возвращает результат слияния. 
    Параметры:
    trpstr -  основная строка триплетов,
    trpstradd - добавляемая строка триплетов.
    ''')
    elif cmd == 'trpSort' :
        cmd = print('''Функция сортирует триплексную строку в лексикографическом порядке имен.
    Возвращает от-сортированную триплексную строку.
    Параметры:
    trpstr -  строка триплетов
    ''')
    elif cmd == 'trpDelPref' :
        cmd = print('''Функция удаляет все триплеты с заданным префиксом из триплексной строки. 
    Параметры:
    trpstr -   строка триплетов,
    pref   -  префикс.
    ''')
    elif cmd == 'trpGet' :
        cmd = print('''Функция ищет по префиксу объекта pref и имени name в строке trpstr значение  триплета и кладет его  в текстовую строку value, тип значение в type.
    Возвращает true, если значение есть, иначе false.
    ''')
    elif cmd == 'trp_Get' :
        cmd = print('''Функция ищет по префиксу объекта pref и имени name в строке trpstr значение  триплета и кладет его  в текстовую строку value.
    Возвращает true, если значение есть, иначе false.
    ''')
    elif cmd == 'trpGetName' :
        cmd = print('''Функция возвращает имя первого триплета в триплексной строке.
    ''')
    elif cmd == 'del_trp' :
        cmd = print('''Функция удаляет  триплеты с заданным префиксом и именем  из триплексной строки. 
    Параметры:
    trpstr -   строка триплетов,
    pref   -  префикс,
    namei  -  имя
    ''')
    elif cmd == 'trpGoNext' :
        cmd = print('''Функция переводит указатель на следующий триплет в строке.
    Параметры:
    trpstr -   строка триплетов.
    ''')
    elif cmd == 'trpGoEnd' :
        cmd = print('''Функция переводит указатель на конец триплексной строчки.
    Параметры:
    trpstr -   строка триплетов.

    ''')
    elif cmd == 'trp_GetFirst' :
        cmd = print('''Функция возвращает указатель на первый триплет (префикс) и берет его значение.
    Параметры:
    trp -   строка триплетов (входной аргумент),
    fullprf   -  обозначение триплета (Пре-фикс.Имя) (выходной аргумент),
    value - значение триплета (выходной аргумент).
    ''')
    else:
        print('неверный аргумент')
    return(cmd)
    

try:
    main()
#Отлов ошибок
except Exception as e:
    error = True
    (arg,) = e.args
    if type(arg) == str:
        print("err: " + arg)
    else:
        print("err: err")
        print("err: " + str(type(arg)))
        print("err: " + str(e.args))
        raiseErr(errProg)

inp.close()
output.close()
trpstrf.close()
parametr.close()
