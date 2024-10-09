package atv_9;

public class ContaPoupanca extends ContaBancaria {
    private int diaRendimento;

    public ContaPoupanca(String nomeCliente, String numConta, double saldoInicial, int diaRendimento) {
        super(nomeCliente, numConta, saldoInicial);
        this.diaRendimento = diaRendimento;
    }

    public void calcularNovoSaldo(double taxaRendimento) {
        if (taxaRendimento > 0) {
            saldo += saldo * (taxaRendimento / 100);
        }
    }

    @Override
    public void mostrarDados() {
        super.mostrarDados();
        System.out.println("Dia de Rendimento: " + diaRendimento);
    }
}

