package atv_5;
import java.util.ArrayList;

public class Calculadora {
    private ArrayList<Double> numeros;

    public Calculadora() {
        numeros = new ArrayList<>();
    }

    public void adicionarNumero(double numero) {
        numeros.add(numero);
    }

    public double somar() {
        double soma = 0;
        for (double numero : numeros) {
            soma += numero;
        }
        return soma;
    }

    public double subtrair() {
        if (numeros.isEmpty()) return 0;
        double resultado = numeros.get(0);
        for (int i = 1; i < numeros.size(); i++) {
            resultado -= numeros.get(i);
        }
        return resultado;
    }

    public double multiplicar() {
        if (numeros.isEmpty()) return 0;
        double produto = 1;
        for (double numero : numeros) {
            produto *= numero;
        }
        return produto;
    }

    public double dividir() {
        if (numeros.isEmpty()) return 0;
        double resultado = numeros.get(0);
        for (int i = 1; i < numeros.size(); i++) {
            if (numeros.get(i) == 0) {
                System.out.println("Erro: Divisão por zero.");
                return 0;
            }
            resultado /= numeros.get(i);
        }
        return resultado;
    }
    public void exibirMenu() {
        System.out.println("Escolha a operação que deseja realizar:");
        System.out.println("1 - Soma");
        System.out.println("2 - Subtração");
        System.out.println("3 - Multiplicação");
        System.out.println("4 - Divisão");
        System.out.println("0 - Sair");
    }

    public void limparNumeros() {
        numeros.clear();
    }
}
