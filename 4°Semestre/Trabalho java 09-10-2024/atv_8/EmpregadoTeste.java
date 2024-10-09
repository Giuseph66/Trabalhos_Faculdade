package atv_8;

public class EmpregadoTeste {
    public static void main(String[] args) {
        Empregado empregado1 = new Empregado("João", "Silva", 3000.00);
        Empregado empregado2 = new Empregado("Maria", "Oliveira", 4000.00);

        System.out.println("Salário anual de " + empregado1.getNome() + " " + empregado1.getSobrenome() + ": R$ " + empregado1.getSalarioAnual());
        System.out.println("Salário anual de " + empregado2.getNome() + " " + empregado2.getSobrenome() + ": R$ " + empregado2.getSalarioAnual());

        int aumento = 100;
        empregado1.darAumento(aumento);
        empregado2.darAumento(aumento);

        System.out.println("\nApós aumento de "+ aumento + "%:");
        System.out.println("Salário anual de " + empregado1.getNome() + " " + empregado1.getSobrenome() + ": R$ " + empregado1.getSalarioAnual());
        System.out.println("Salário anual de " + empregado2.getNome() + " " + empregado2.getSobrenome() + ": R$ " + empregado2.getSalarioAnual());
    }
}
