package atv_9;

public class Teste {
    public static void main(String[] args) {
        ContaPoupanca contaPoupanca = new ContaPoupanca("João Silva", "1234-5", 1000.00, 15);
        ContaEspecial contaEspecial = new ContaEspecial("Maria Oliveira", "6789-0", 500.00, 1000.00);

        System.out.println("Tenta sacar R$ 200 da conta poupança...");
        contaPoupanca.sacar(200);
        contaPoupanca.mostrarDados();

        System.out.println("\nTenta sacar R$ 600 da conta especial...");
        contaEspecial.sacar(600);
        contaEspecial.mostrarDados();

        System.out.println("\nTenta sacar R$ 1000 da conta especial (testando limite)...");
        contaEspecial.sacar(1000);
        contaEspecial.mostrarDados();

        System.out.println("\nDeposita R$ 500 na conta poupança...");
        contaPoupanca.depositar(500);
        contaPoupanca.mostrarDados();

        System.out.println("\nDeposita R$ 300 na conta especial...");
        contaEspecial.depositar(300);
        contaEspecial.mostrarDados();

        System.out.println("\nAplicando rendimento de 5% na conta poupança...");
        contaPoupanca.calcularNovoSaldo(5);
        contaPoupanca.mostrarDados();

        System.out.println("\nDados Finais:");
        contaPoupanca.mostrarDados();
        contaEspecial.mostrarDados();
    }
}
