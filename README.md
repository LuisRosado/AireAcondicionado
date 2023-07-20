# AireAcondicionado
Control basico de AC


El código que proporcionas es una simulación básica de un control de aire acondicionado. A continuación, te explico lo que hace cada parte del código:

--> Estado = random.randint(0, 1): Genera un número aleatorio 0 o 1 para representar el estado del aire acondicionado. 0 indica que está apagado, y 1 indica que está encendido.

--> Temperatura = random.randint(0, 45): Genera un número aleatorio entre 0 y 45 para representar la temperatura actual.

--> print('Estado: ', Estado, 'Temperatura: ', Temperatura): Muestra el estado del aire acondicionado y la temperatura actual en la pantalla.

--> El siguiente bloque de código utiliza condicionales if, elif, y else para simular las acciones del aire acondicionado según su estado y la temperatura.

Si el aire acondicionado está apagado (Estado == 0) y la temperatura es mayor que 25, el aire acondicionado se enciende (Estado = 1) y muestra "Encendiendo".
Si el aire acondicionado está apagado (Estado == 0) y la temperatura es menor o igual a 25, no hace nada y simplemente muestra un espacio vacío print('').
Si el aire acondicionado está encendido (Estado == 1) y la temperatura es mayor que 25, no hace nada y simplemente muestra un espacio vacío print('').
Si el aire acondicionado está encendido (Estado == 1) y la temperatura es menor o igual a 25, el aire acondicionado se apaga (Estado = 0) y muestra "Apagando".

En resumen, este código simula el comportamiento básico de un control de aire acondicionado que se enciende automáticamente si la temperatura es mayor a 25°C y se apaga si la temperatura baja a 25°C o menos. Cabe mencionar que este código solo realiza las acciones de encender o apagar el aire acondicionado, sin tener en cuenta otros ajustes o modos que un control de aire acondicionado real podría tener.
