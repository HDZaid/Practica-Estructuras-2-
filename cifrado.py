# --- Hashing FNV-1 (32 bits) ---

def fnv1_32_hash(text):
    # Parámetros estándar del algoritmo FNV-1 (32 bits)
    FNV_prime = 16777619
    offset_basis = 2166136261

    hash_value = offset_basis
    for char in text:
        hash_value = hash_value * FNV_prime
        hash_value = hash_value ^ ord(char)
        hash_value = hash_value & 0xffffffff  # mantener en 32 bits
    return hash_value


def main():
    print("=== HASHING FNV-1 ===")
    mensaje = input("Ingrese un mensaje de texto: ")

    hash_result = fnv1_32_hash(mensaje)
    print(f"\nHash FNV-1 (32 bits): {hash_result}")
    print(f"En formato hexadecimal: {hash_result:08x}")


if __name__ == "__main__":
    main()