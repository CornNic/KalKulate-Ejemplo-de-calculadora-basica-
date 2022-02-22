SUMA = 1
RESTA = 2
MULTIPLICACION = 3
DIVISION = 4
DIVISION_ENTERA = 5
MODULO = 6
POTENCIA = 7


print(f'''
                                    KALCULATE by CornNic
{SUMA}) SUMA
{RESTA}) RESTA
{MULTIPLICACION}) MULTIPLICACION
{DIVISION}) DIVISION
{DIVISION_ENTERA}) DIVISION ENTERA
{MODULO}) MODULO
{POTENCIA}) POTENCIA
 ''')

opc = int(input('Seleccione que operacion desea realizar : '))

if SUMA <= opc <= POTENCIA :
    opc_1 = float(input('Ingrese el primer numero : '))
    opc_2 = float(input('Ingrese el segundo numero : '))
    if opc == SUMA:
        print(f'{opc_1} + {opc_2} = {opc_1 + opc_2}')
    elif opc == RESTA:
        print(f'{opc_1} - {opc_2} = {opc_1 - opc_2}')
    elif opc == MULTIPLICACION:
        print(f'{opc_1} * {opc_2} = {opc_1 * opc_2}')
    elif opc == DIVISION :
        if opc_2 != 0:
            print(f'{opc_1} / {opc_2} = {opc_1 / opc_2}')
        else:
            print('Operacion no definida')
    elif opc == DIVISION_ENTERA :
        if opc_2 != 0:
            print(f'{opc_1} // {opc_2} = {opc_1 // opc_2}')
        else:
            print('Operacion no definida')
    elif opc == MODULO :
        if opc_2 != 0:
            print(f'{opc_1} % {opc_2} = {opc_1 % opc_2}')
        else:
            print('Operacion no definida')
    else:
        print(f'{opc_1} ** {opc_2} = {opc_1 ** opc_2}')
else:
    print('Syntax Error : No existe esa opcion')


print('Powered By CornNic')