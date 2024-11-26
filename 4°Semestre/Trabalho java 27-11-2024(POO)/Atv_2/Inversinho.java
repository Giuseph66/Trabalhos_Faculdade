import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Inversinho {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite uma frase: ");
        String frase = scanner.nextLine();

        String[] palavras = frase.split(" ");
        List<String> listaPalavras = new ArrayList<>();

        for (String palavra : palavras) {
            listaPalavras.add(palavra);
        }

        System.out.print("Frase invertida: \n");
        for (int i = listaPalavras.size() - 1; i >= 0; i--) {
            System.out.print(listaPalavras.get(i) + " ");
        }
        
        List<Character> listaCaracteres = new ArrayList<>();
        for (char c : frase.toCharArray()) {
            listaCaracteres.add(c);
        }

        System.out.print("\nOU ...\n");
        for (int i = listaCaracteres.size() - 1; i >= 0; i--) {
            System.out.print(listaCaracteres.get(i));
        }
    }
}
