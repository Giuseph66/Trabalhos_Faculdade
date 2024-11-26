import java.util.Scanner;

public class Utils {
    public static String validarEntradaTexto(String mensagem, Scanner scanner) {
        String entrada;
        do {
            System.out.print(mensagem);
            entrada = scanner.nextLine().trim();
            if (entrada.isEmpty()) {
                System.out.println("Erro: Entrada não pode ser vazia. Tente novamente.");
            }
        } while (entrada.isEmpty());
        return entrada;
    }
}
