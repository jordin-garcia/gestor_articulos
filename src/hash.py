class Hash:
    def calcular_hash_fnv1(self, contenido):
        # Calcula el hash FNV-1 de un contenido dado

        # Constantes FNV-1 para 32 bits
        FNV_OFFSET_BASIS = 2166136261
        FNV_PRIME = 16777619

        # Inicializar hash con offset basis
        valor_hash = FNV_OFFSET_BASIS

        # Convertir contenido a bytes si es string
        if isinstance(contenido, str):
            contenido = contenido.encode("utf-8")

        # Procesar cada byte
        for byte in contenido:
            valor_hash = valor_hash * FNV_PRIME
            valor_hash = valor_hash ^ byte

            # Mantener en 32 bits
            valor_hash = valor_hash & 0xFFFFFFFF

        # Convertir a hexadecimal y retornar 8 carácteres
        return format(valor_hash, "08x")
