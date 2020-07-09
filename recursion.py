'''
Realice un método recursivo que recibiendo una lista de números retorne el promedio 
de la multiplicación de sus miembros

ejem :  input [1,3,2,5,4,2]
        ouput [1*3*2*5*4*2]/ len(input)

'''

def multiplication(list):
    result = 0
    if list == []:
        result = 1
    else:
        result = list [0] * multiplication(list[1:])
    return result

# def multiplication2(list):
#     result = 0
#     array_mult = [ 0 for i in range(len(list))]
#     if list == []:
#         result = 1
#     else:
#         result = list[0] * multiplication2(list[1:])
#     array_mult 
#     return array_mult    

if __name__ == '__main__':
    list = [] 
    size = int(input('Defina longitud: '))
    for i in range(size):
        item = int(input('Ingrese valor: '))
        list.append(item)
    print(list)

    print(multiplication(list)/size)
    # print(multiplication2(list))
    
