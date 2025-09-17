import numpy as np


def obtener_arreglo(range_t: tuple[int, int], range_b: tuple[int, int]):
    def fn (size: int):
        return np.column_stack((
            np.random.randint(range_b[0], range_b[1], size, dtype=np.int64),
            np.random.randint(range_t[0], range_t[1], size, dtype=np.int64)
        ))
    return fn


