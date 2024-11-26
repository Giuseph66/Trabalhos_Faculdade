import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class ContadorPalavrasUnicas {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite uma frase: ");
        String frase = scanner.nextLine();

        String[] palavras = frase.split("\\s+");

        Set<String> palavrasUnicas = new HashSet<>();

        for (String palavra : palavras) {
            palavra = palavra.toLowerCase().replaceAll("[^a-zá-úà-ùãõâêîôûç]", "");
            if (!palavra.isEmpty()) {
                palavrasUnicas.add(palavra);
            }
        }

        System.out.println("Número de palavras únicas: " + palavrasUnicas.size());
        
        System.out.println("Palavras únicas:");
        for (String palavra : palavrasUnicas) { 
            System.out.println(palavra); }
    }
}
