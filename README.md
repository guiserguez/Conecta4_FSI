# Conecta4
Primer trabajo de curso de Fundamentos de los Sistemas Inteligentes: Búsqueda con oponente

Descripción de la práctica

Para comenzar hemos implementado una heurística que devuelve valores aleatorios, como toma de contacto con la práctica.

A partir de ahí empezamos a hacer la heurística que se ha utilizado en la práctica, que en lo que se basa es, si el estado del board es de perdido devuelve “-infinito”, si es de ganado es “+infinito”, sino empezamos a evaluar a partir de los movimientos que se pueden realizar, para el jugador en concreto las diferentes rectas donde se puede hacer 4 en raya, sumando 1 si es hueco está vacío y 3 si es una ficha propia. Si las posiciones contadas antes de llegar a una ficha contraria son menores a 4, es decir que es imposible realizar 4 en raya, se devuelve la puntuación a ese estado como 0. 
Luego se evalúa para el contrario y se le resta al contador la heurística obtenida para el propio usuario, utilizando el mismo método que hemos utilizado previamente.

Luego introdujimos la variante de poder empezar la partida nosotros o la máquina, y elegir además el nivel de dificultad, que lo implementaremos cambiando la profundidad de la heurística del 1 al 4.

También implementamos el decorador memoize, para que cuando se recuerde una posición que se ha evaluado anteriormente no la evalúe de nuevo, sino que la obtenga del diccionario memo.

Queremos destacar que tuvimos problemas al realizar la heurística, ya que cuando encontraba una posición vacía, al hacer el board.get(posicion) nos devolvía “none”, para resolver el problema se evalua si es la ficha del jugador o del contrario, y si no es ninguna de las dos, pues lo tratamos como vacío.

Por último hemos implementado la opción de que dos heurísticas puedan competir entre ellas. En esta entrega lo hemos configurado de manera de que la heurística compita con sí misma.

El trabajo lo hemos repartido de la siguiente manera: Güise Lorenzo Rodríguez Aguiar desarrolló la opción de elegir la dificultad y que dos heurísticas compitan entre ellas y Álvaro Suárez Marrero refactorizó el código para facilitar su comprensión y lectura. De manera conjunta hemos desarrollado la heurística y el patrón de diseño “memoize”.
