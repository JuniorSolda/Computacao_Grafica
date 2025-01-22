#Itamar Soldá Junior - 1992821

from pywavefront import Wavefront

class Vertex:
    def __init__(self, id, x, y, z):
        self.id = id
        self.x = x
        self.y = y
        self.z = z
        self.edges = []

class Edge:
    def __init__(self, id, vertex1, vertex2, face1=None, face2=None):
        self.id = id
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.face1 = face1
        self.face2 = face2

class Face:
    def __init__(self, id, vertices):
        self.id = id
        self.vertices = vertices
        self.edges = []


class WingedEdge:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.faces = []

    def add_vertex(self, x, y, z):
        vertex_id = len(self.vertices)
        vertex = Vertex(vertex_id, x, y, z)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self, vertex1, vertex2, face1=None, face2=None):
        edge_id = len(self.edges)
        edge = Edge(edge_id
        , vertex1, vertex2, face1, face2)
        self.edges.append(edge)
        vertex1.edges.append(edge)
        vertex2.edges.append(edge)
        return edge

    def add_face(self, vertices):
        face_id = len(self.faces)
        face = Face(face_id, vertices)
        self.faces.append(face)
        for i in range(len(vertices)):
            vertex1 = vertices[i]
            vertex2 = vertices[(i + 1) % len(vertices)]
            edge = self.find_edge(vertex1, vertex2)
            if edge:
                edge.face2 = face
            else:
                edge = self.add_edge(vertex1, vertex2, face)
            face.edges.append(edge)

    def find_edge(self, vertex1, vertex2):
        for edge in vertex1.edges:
            if edge.vertex1 == vertex1 and edge.vertex2 == vertex2:
                return edge
        return None

    def find_faces_shared_by_edge(self, edge_id):
        if 0 <= edge_id < len(self.edges):
            edge = self.edges[edge_id]
            return [face.id for face in [edge.face1, edge.face2] if face]  # Filtrar faces nulas
        else:
            return []

    def find_edges_shared_by_vertex(self, vertex_id):
        if 0 <= vertex_id < len(self.vertices):
            vertex = self.vertices[vertex_id]
            return vertex.edges
        else:
            return []

    def find_vertices_shared_by_face(self, face_id):
        if 0 <= face_id < len(self.faces):
            face = self.faces[face_id]
            return face.vertices
        else:
            return []

# Função para ler o arquivo .obj e construir a estrutura winged-edge
def build_winged_edge_structure(file_name):
    winged_edge = WingedEdge()
    current_vertices = []

    with open(file_name, 'r') as obj_file:
        for line in obj_file:
            parts = line.split()
            if not parts:
                continue

            if parts[0] == 'v':
                x, y, z = map(float, parts[1:4])
                vertex = winged_edge.add_vertex(x, y, z)
                current_vertices.append(vertex)
            elif parts[0] == 'f':
                vertex_indices = [int(v.split('//')[0]) - 1 for v in parts[1:]]
                face_vertices = [current_vertices[i] for i in vertex_indices]
                winged_edge.add_face(face_vertices)

    return winged_edge

def main():
    obj_file = "cube.obj"
    winged_edge = build_winged_edge_structure(obj_file)

    while True:
        print("\nMenu:")
        print("1. Consultar as faces que compartilham uma aresta")
        print("2. Consultar as arestas que compartilham um vértice")
        print("3. Consultar os vértices que compartilham uma face")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            edge_id = int(input("Informe o ID da aresta: "))
            shared_faces = winged_edge.find_faces_shared_by_edge(edge_id)
            print(f"Faces compartilhadas pela aresta {edge_id}: {shared_faces}")
            input("Pressione Enter para voltar ao menu...")

        elif choice == "2":
            vertex_id = int(input("Informe o ID do vértice: "))
            shared_edges = winged_edge.find_edges_shared_by_vertex(vertex_id)
            print(f"Arestas compartilhadas pelo vértice {vertex_id}: {[edge.id for edge in shared_edges]}")
            input("Pressione Enter para voltar ao menu...")

        elif choice == "3":
            face_id = int(input("Informe o ID da face: "))
            shared_vertices = winged_edge.find_vertices_shared_by_face(face_id)
            print(f"Vértices compartilhados pela face {face_id}: {[vertex.id for vertex in shared_vertices]}")
            input("Pressione Enter para voltar ao menu...")

        elif choice == "4":
            break

if __name__ == "__main__":
    main()
