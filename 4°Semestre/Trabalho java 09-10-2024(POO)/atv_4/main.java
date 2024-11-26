package atv_4;

public class main {
    public static void main(String[] args) {
        Triangulo triangulo = new Triangulo(3, 4, 5);
        triangulo.exibirInformacoes();
        
        Triangulo trianguloerrado = new Triangulo(1, 2, 10);
        trianguloerrado.exibirInformacoes();
    }
}

