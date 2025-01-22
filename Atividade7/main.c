#include <GL/glut.h>

// Função para renderizar o triângulo
void display(void) {
    glClear(GL_COLOR_BUFFER_BIT); // Limpa a tela

    glBegin(GL_TRIANGLES);  // Inicia o desenho do triângulo
        glColor3f(1.0, 0.0, 0.0);  // Define a cor do triângulo (vermelho)
        glVertex2f(-0.5, -0.5); // Vértice inferior esquerdo
        glVertex2f( 0.5, -0.5); // Vértice inferior direito
        glVertex2f( 0.0,  0.5); // Vértice superior
    glEnd();

    glFlush(); // Exibe o conteúdo na janela
}

// Função principal
int main(int argc, char** argv) {
    glutInit(&argc, argv);               // Inicializa o GLUT
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);  // Define o modo de exibição
    glutInitWindowSize(500, 500);         // Define o tamanho da janela
    glutCreateWindow("Triângulo com OpenGL");      // Cria a janela

    glutDisplayFunc(display);             // Define a função de renderização
    glutMainLoop();                       // Inicia o loop de renderização
    return 0;
}

