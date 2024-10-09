package atv_10;
import java.util.InputMismatchException;
import java.util.Scanner;

public class ImpostoTeste {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        Contribuinte[] contribuintes = new Contribuinte[6];

        System.out.println("Cadastro de 3 Pessoas Físicas:");
        for (int i = 0; i < 3; i++) {
            System.out.print("Nome: ");
            String nome = scanner.nextLine();
            double rendaBruta = 0.0;
        
            boolean entradaValida = false;
            while (!entradaValida) {
                try {
                    System.out.print("Renda Bruta: R$ ");
                    rendaBruta = scanner.nextDouble();
                    entradaValida = true;
                } catch (InputMismatchException e) {
                    System.out.println("Entrada inválida! Por favor, insira um número.");
                    scanner.next(); 
                }
            }
            scanner.nextLine(); 
            contribuintes[i] = new PessoaFisica(nome, rendaBruta);
        }
        System.out.println("\nCadastro de 3 Pessoas Jurídicas:");
        for (int i = 3; i < 6; i++) {
            System.out.print("Nome: ");
            String nome = scanner.nextLine();
            double rendaBruta = 0.0;
            boolean entradaValida = false;
            while (!entradaValida) {
                try {
                    System.out.print("Renda Bruta: R$ ");
                    rendaBruta = scanner.nextDouble();
                    entradaValida = true;
                } catch (InputMismatchException e) {
                    System.out.println("Entrada inválida! Por favor, insira um número.");
                    scanner.next(); 
                }
            }
            scanner.nextLine();
            contribuintes[i] = new PessoaJuridica(nome, rendaBruta);
        }

        System.out.println("\nImpostos a serem pagos:");
        for (Contribuinte contribuinte : contribuintes) {
            contribuinte.exibirInfo();
            System.out.println("--------------------------");
        }

        scanner.close();
    }
}
