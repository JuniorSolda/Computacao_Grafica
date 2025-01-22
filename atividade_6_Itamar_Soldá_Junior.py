import numpy as np

def calcular_matriz_transformacao(transformacoes):
   
    # Matriz identidade inicial
    matriz_resultante = np.eye(3)
    
    for t in transformacoes:
        if t["tipo"] == "translacao":
            dx, dy = t.get("dx", 0), t.get("dy", 0)
            matriz_translacao = np.array([
                [1, 0, dx],
                [0, 1, dy],
                [0, 0, 1]
            ])
            matriz_resultante = matriz_resultante @ matriz_translacao
        
        elif t["tipo"] == "rotacao":
            angulo = np.radians(t.get("angulo", 0))  # Converte graus para radianos
            cos_a, sin_a = np.cos(angulo), np.sin(angulo)
            matriz_rotacao = np.array([
                [cos_a, -sin_a, 0],
                [sin_a,  cos_a, 0],
                [0,      0,     1]
            ])
            matriz_resultante = matriz_resultante @ matriz_rotacao
        
        elif t["tipo"] == "escala":
            sx, sy = t.get("sx", 1), t.get("sy", 1)
            matriz_escala = np.array([
                [sx, 0,  0],
                [0,  sy, 0],
                [0,  0,  1]
            ])
            matriz_resultante = matriz_resultante @ matriz_escala

    return matriz_resultante
# Definição da sequência de transformações
transformacoes = [
    {"tipo": "translacao", "dx": 3, "dy": 4},
    {"tipo": "rotacao", "angulo": 60},
    {"tipo": "escala", "sx": 2, "sy": 1}
]

# Calcula a matriz de transformação resultante
matriz_final = calcular_matriz_transformacao(transformacoes)
print("Matriz de Transformação Resultante:")
print(matriz_final)
