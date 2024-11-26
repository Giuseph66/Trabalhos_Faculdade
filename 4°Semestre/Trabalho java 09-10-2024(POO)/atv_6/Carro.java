package atv_6;

public class Carro {
    private String placa;
    private int marcha;

    public Carro(String placa) {
        this.placa = placa;
        this.marcha = 0; 
    }

    public void ligar() {
        System.out.println("Carro com placa " + placa + " ligado.");
    }

    public void trocarMarcha(int marcha) {
        this.marcha = marcha;
        System.out.println("Marcha trocada para " + marcha);
    }

    public void acelerar() {
        System.out.println("Carro acelerando na marcha " + marcha);
    }

    public void frear() {
        System.out.println("Carro freando.");
    }

    public void desligar() {
        System.out.println("Carro com placa " + placa + " desligado.");
    }
}

