#Aire Acondicionado

import random

Estado = random.randint(0, 1)
Temperatura = random.randint(0, 45)

print('Estado: ',Estado,'Temperatura: ',Temperatura)

if ((Estado == 0) & (Temperatura > 25)):
    Estado = 1
    print('Encendiendo')
elif((Estado == 0) & (Temperatura <= 25)):
    print('')
elif((Estado == 1) & (Temperatura > 25)):
    print('')
elif((Estado == 0) & (Temperatura <= 25)):
    Estado = 0
    print('Apagando')

