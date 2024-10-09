package atv_5;
import java.util.Scanner;

public class main {
    public static void main(String[] args) {
        Calculadora calculadora = new Calculadora();
        Scanner scanner = new Scanner(System.in);
        boolean continuar = true;

        while (continuar) {
            System.out.println("\nInsira os números (digite 's' para encerrar a inserção e realizar a operação):");
            while (true) {
                String entrada = scanner.next();
                if (entrada.equalsIgnoreCase("s")) {
                    break;
                }
                try {
                    double numero = Double.parseDouble(entrada);
                    calculadora.adicionarNumero(numero);
                } catch (NumberFormatException e) {
                    System.out.println("Entrada inválida, tente novamente.");
                }
            }

            calculadora.exibirMenu();
            int opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    System.out.println("Resultado da soma: " + calculadora.somar());
                    break;
                case 2:
                    System.out.println("Resultado da subtração: " + calculadora.subtrair());
                    break;
                case 3:
                    System.out.println("Resultado da multiplicação: " + calculadora.multiplicar());
                    break;
                case 4:
                    System.out.println("Resultado da divisão: " + calculadora.dividir());
                    break;
                case 0:
                    continuar = false;
                    System.out.println("Encerrando o programa.");
                    break;
                default:
                    System.out.println("Opção inválida, tente novamente.");
            }

            calculadora.limparNumeros();
        }
        scanner.close();
    }
}
