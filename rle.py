import heapq
from collections import Counter

# --- Codificación Huffman ---
class NodoHuffman:
    def __init__(self, simbolo, frecuencia):
        self.simbolo = simbolo
        self.frecuencia = frecuencia
        self.izq = None
        self.der = None
    
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

def construir_arbol_huffman(texto):
    frecuencias = Counter(texto)
    heap = [NodoHuffman(simbolo, freq) for simbolo, freq in frecuencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        nuevo = NodoHuffman(None, n1.frecuencia + n2.frecuencia)
        nuevo.izq = n1
        nuevo.der = n2
        heapq.heappush(heap, nuevo)
    
    return heap[0]

def generar_codigos(arbol, codigo="", codigos={}):
    if arbol is None:
        return
    if arbol.simbolo is not None:
        codigos[arbol.simbolo] = codigo
    generar_codigos(arbol.izq, codigo + "0", codigos)
    generar_codigos(arbol.der, codigo + "1", codigos)
    return codigos

def comprimir_huffman(texto):
    arbol = construir_arbol_huffman(texto)
    codigos = generar_codigos(arbol)
    comprimido = ''.join(codigos[c] for c in texto)
    return comprimido, codigos

# --- Codificación RLE ---
def comprimir_rle(texto):
    if not texto:
        return ""
    comprimido = []
    count = 1
    for i in range(1, len(texto)):
        if texto[i] == texto[i-1]:
            count += 1
        else:
            comprimido.append((texto[i-1], count))
            count = 1
    comprimido.append((texto[-1], count))

    # Convertimos a binario real
    binario = ''.join(f"{ord(char):08b}{count:08b}" for char, count in comprimido)
    return binario

# --- Programa Principal ---
def main():
    print("=== Compresión de Texto (Huffman o RLE) ===")
    texto = input("Ingresa el mensaje a comprimir: ")
    metodo = input("Método (1=Huffman, 2=RLE): ").strip()

    original_bits = len(texto.encode('utf-8')) * 8  # bits reales

    if metodo == "1":
        comprimido, codigos = comprimir_huffman(texto)
        comprimido_bits = len(comprimido)
        print("\n--- Resultado Huffman ---")
        print("Códigos generados:", codigos)
        print("Datos comprimidos (binario):", comprimido)
    elif metodo == "2":
        comprimido = comprimir_rle(texto)
        comprimido_bits = len(comprimido)
        print("\n--- Resultado RLE ---")
        print("Datos comprimidos (binario):", comprimido)
    else:
        print("Método no válido.")
        return

    print("\n--- Estadísticas ---")
    print(f"Tamaño original: {original_bits} bits")
    print(f"Tamaño comprimido: {comprimido_bits} bits")
    print(f"Reducción: {100 - (comprimido_bits/original_bits)*100:.2f}%")

if __name__ == "__main__":
    main()