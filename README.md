# TP2: programación dinámica.

### Para correr el TP

```
$ python3 ./tp2.py ./files/<archivo>
```

Tambien se puede generar un set de datos (explicado mas adelante) y ejecutar el trabajo con dicho set.

La salida contiene el número de enemigos eliminados y la secuencia de decisiones. Esta se encuentra en el archivo `/output/<archivo>`, luego de haber ejecutado el primer comando. 

### Para correr las pruebas (comparar la salida del algoritmo con el resultado esperado de los archivos de /files)

```
$ python3 ./tests.py
```

### En caso de querer generar nuevos sets de datos, ejecutar:

```
$ python3 ./utils/data_sets.py
```

Los tamaños de los sets y la cantidad de los mismos son parametrizables. La salida generada se encuentra en la carpeta `/sets`, y el nombre del archivo es `<size>.txt`.


### Para generar nuevos archivos con su salida esperada (algoritmo de fuerza bruta), ejecutar:

```
$ python3 ./utils/bt.py
```

El tamaño y la cantidad de sets generados tambien es parametrizable. La salida de los archivos se guarda en `/files`, y se agrega el resultado esperado en `/files/Resultados Esperados.txt`.


### En caso de querer ejecutar gráficos, se tienen que instalar las dependencias necesarias:

```
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
```