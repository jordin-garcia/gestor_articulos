from hash import Hash


class Nodo:
    def __init__(self, clave, valor):
        self.clave = clave
        self.valor = valor
        self.siguiente = None


class TablaHashEncadenamiento:
    def __init__(self, tamaño=101):
        self.valor_hash = Hash()
        self.tamaño = tamaño
        self.tabla = [None] * tamaño

    def _hash(self, clave):
        hash_int = int(clave, 16)
        return hash_int % self.tamaño

    def insertar(self, clave, valor):
        indice = self._hash(clave)
        nodo = self.tabla[indice]

        if nodo is None:
            self.tabla[indice] = Nodo(clave, valor)
            return

        # Recorremos la lista para ver si existe la clave
        prev = None
        while nodo:
            if nodo.clave == clave:
                nodo.valor = valor  # actualiza si existe
                return
            prev = nodo
            nodo = nodo.siguiente

        # Inserta al final de la lista
        prev.siguiente = Nodo(clave, valor)

    def buscar(self, clave):
        indice = self._hash(clave)
        nodo = self.tabla[indice]

        while nodo:
            if nodo.clave == clave:
                return nodo.valor
            nodo = nodo.siguiente
        return None

    def eliminar(self, clave):
        indice = self._hash(clave)
        nodo = self.tabla[indice]
        prev = None

        while nodo:
            if nodo.clave == clave:
                if prev:
                    prev.siguiente = nodo.siguiente
                else:
                    self.tabla[indice] = nodo.siguiente
                return True
            prev = nodo
            nodo = nodo.siguiente
        return False

    def todos_valores(self):
        valores = []
        for i in range(self.tamaño):
            actual = self.tabla[i]
            while actual:
                valores.append(actual.valor)
                actual = actual.siguiente
        return valores

    def existe(self, clave):
        return self.buscar(clave) is not None
