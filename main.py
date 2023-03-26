def list_comprehension_exercise_1():
    list_1 = [i for i in range(0, 11)]
    return list_1
print(list_comprehension_exercise_1())

def list_comprehension_exercise_2():
    list_2 = [i for i in range(0, 22) if i % 2 == 0 or i % 3 == 0]
    return list_2
print(list_comprehension_exercise_2())

def list_comprehension_exercise_3():
    list_3 = [i for i in range(-5, 32) if i % 2 != 0 and i % 5 != 0]
    return list_3
print(list_comprehension_exercise_3())

def list_comprehension_exercise_4():
    list_4 = [i**2 for i in range(0, 11)]
    return list_4
print(list_comprehension_exercise_4())

def list_comprehension_exercise_5(sentence:str):
    list_5 = [i for i in sentence if i.isupper()]
    return list_5
#isupper() que retorna True se todos caracteres forem maiúsculos, e False se não forem.
print(list_comprehension_exercise_5('O Rato Rui Gosta De QueiJo FresQuiNho'))

def list_comprehension_exercise_6(sentence:str):
    list_6 = [i for i in sentence.split() if len(i)>=4 and i[0]== "r"]
    return list_6
"""
split() divide uma string em uma lista de strings, usando um determinado delimitador.
len(i) verifica o tamanho do elemento no loop.
"""
print(list_comprehension_exercise_6('o rato rui roeu a roupa do rei de roma'))

