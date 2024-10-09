package atv_9;

public class ContaEspecial extends ContaBancaria {
    private double limite;

    public ContaEspecial(String nomeCliente, String numConta, double saldoInicial, double limite) {
        super(nomeCliente, numConta, saldoInicial);
        this.limite = limite;
    }

    @Override
    public boolean sacar(double valor) {
        if (valor > 0 && saldo + limite >= valor) {
            saldo -= valor;
            return true;
        } else {
            System.out.println("Saldo insuficiente, mesmo com limite.");
            return false;
        }
    }

    @Override
    public void mostrarDados() {
        super.mostrarDados();
        System.out.println("Limite: R$ " + limite);
    }
}
