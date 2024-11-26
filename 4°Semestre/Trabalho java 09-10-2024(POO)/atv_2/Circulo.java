package atv_2;

public class Circulo {
        private double raio;
    
        public Circulo(double raio) {
            this.raio = raio;
        }
    
        public double calcularArea() {
            return Math.PI * Math.pow(raio, 2);
        }
    
        public double calcularPerimetro() {
            return 2 * Math.PI * raio;
        }
        public void exibirInformacoes() {
            System.out.println("Raio: " + raio);
            System.out.println("Área: " + calcularArea());
            System.out.println("Perímetro: " + calcularPerimetro());
        }
    }