package atv_4;

public class Triangulo {
        private double lado1;
        private double lado2;
        private double lado3;
    
        public Triangulo(double lado1, double lado2, double lado3) {
            this.lado1 = lado1;
            this.lado2 = lado2;
            this.lado3 = lado3;
        }
        public boolean isTrianguloValido() {
            return (lado1 + lado2 > lado3) && (lado1 + lado3 > lado2) && (lado2 + lado3 > lado1);
        }
    
        public double calcularArea() {
            if (isTrianguloValido()) {
                double SPerimetro = (lado1 + lado2 + lado3) / 2;
                return Math.sqrt(SPerimetro * (SPerimetro - lado1) * (SPerimetro - lado2) * (SPerimetro - lado3));
            } else {
                return 0;
            }
        }
        public void exibirInformacoes() {
            System.out.println("Lado 1: " + lado1);
            System.out.println("Lado 2: " + lado2);
            System.out.println("Lado 3: " + lado3);
            if (isTrianguloValido()) {
                System.out.println("Este é um triângulo válido.");
                System.out.println("Área: " + calcularArea());
            } else {
                System.out.println("Os lados fornecidos não formam um triângulo válido.");
            }
        }
}
