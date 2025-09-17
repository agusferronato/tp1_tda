# TP1 Teoria De Algoritmos

### Para correr el programa

```
$ python3 ./tp1.py ./files/<nombre_archivo>.txt
```

Por ejemplo:

```
$ python3 ./tp1.py ./files/10.txt
```

Salida esperada:

```
Batallas en orden (bi, ti) 
[(97, 100), (86, 100), (82, 100), (68, 100), (68, 100), (61, 100), (58, 100), (53, 100), (47, 100), (35, 100)]

Coeficiente obtenido
309600
```

### Para comparar la salida del algoritmo con las de la catedra, ejecutar:

```
$ python3 ./tests.py -c
```

### Para comparar la salida del algoritmo con las del algoritmo de backtracking, ejecutar:

```
$ python3 ./tests.py -a
```

### En caso de querer ejecutar graficos y otras funcionalidades:

1) Inicializar entorno virtual

```
$ python3 -m venv .venv
$ source .venv/bin/activate
```

2) Descargar dependencias

```
$ pip install -r requirements.txt
```
