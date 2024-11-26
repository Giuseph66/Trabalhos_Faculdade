import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class Conta_ocorrencia {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite uma frase: ");
        String frase = scanner.nextLine();

        String[] palavras = frase.split("\\s+");

        Map<String, Integer> contadorPalavras = new HashMap<>();

        for (String palavra : palavras) {
            palavra = palavra.toLowerCase().replaceAll("[^a-zá-úà-ùãõâêîôûç]", "");
            if (!palavra.isEmpty()) {
                contadorPalavras.put(palavra, contadorPalavras.getOrDefault(palavra, 0) + 1);
            }
        }
        System.out.println("Ocorrências de cada palavra:");
        for (Map.Entry<String, Integer> entrada : contadorPalavras.entrySet()) {
            System.out.println(entrada.getKey() + ": " + entrada.getValue());
        }
    }
}
