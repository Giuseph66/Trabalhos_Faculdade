package atv_11;

public class TesteArea {
    public static void main(String[] args) {
        AreaCalculavel quadrado = new Quadrado(4);
        AreaCalculavel retangulo = new Retangulo(3, 5);
        AreaCalculavel circulo = new Circulo(2.5);

        System.out.println("Área do Quadrado: " + quadrado.calculaArea());
        System.out.println("Área do Retangulo: " + retangulo.calculaArea());
        System.out.println("Área do Circulo: " + circulo.calculaArea());
    }
}
