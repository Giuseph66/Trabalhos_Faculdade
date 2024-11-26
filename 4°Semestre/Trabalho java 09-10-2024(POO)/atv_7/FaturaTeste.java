package atv_7;

public class FaturaTeste {
    public static void main(String[] args) {
        Fatura fatura = new Fatura("001", "Teclado Mecânico", 5, 150.75);

        // Exibindo informações da fatura
        System.out.println("Número da Fatura: " + fatura.getNumero());
        System.out.println("Descrição: " + fatura.getDescricao());
        System.out.println("Quantidade: " + fatura.getQuantidade());
        System.out.println("Preço por item: R$ " + fatura.getPrecoPorItem());
        System.out.println("Total da Fatura: R$ " + fatura.getTotalFatura());

        Fatura faturaErrada = new Fatura("002", "Mouse", -3, -50.0);
        System.out.println("\nTestando com valores inválidos:");
        System.out.println("Número da Fatura: " + faturaErrada.getNumero());
        System.out.println("Descrição: " + faturaErrada.getDescricao());
        System.out.println("Quantidade: " + faturaErrada.getQuantidade());
        System.out.println("Preço por item: R$ " + faturaErrada.getPrecoPorItem());
        System.out.println("Total da Fatura: R$ " + faturaErrada.getTotalFatura());
    }
}
