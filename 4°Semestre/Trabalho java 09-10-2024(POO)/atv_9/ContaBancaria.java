package atv_9;

public class ContaBancaria {
    private String nomeCliente;
    private String numConta;
    protected double saldo; 

    public ContaBancaria(String nomeCliente, String numConta, double saldoInicial) {
        this.nomeCliente = nomeCliente;
        this.numConta = numConta;
        this.saldo = saldoInicial;
    }

    public String getNomeCliente() {
        return nomeCliente;
    }

    public String getNumConta() {
        return numConta;
    }

    public double getSaldo() {
        return saldo;
    }

    public boolean sacar(double valor) {
        if (valor > 0 && saldo >= valor) {
            saldo -= valor;
            return true;
        } else {
            System.out.println("Saldo insuficiente para saque.");
            return false;
        }
    }

    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
        }
    }

    public void mostrarDados() {
        System.out.println("Nome do Cliente: " + nomeCliente);
        System.out.println("Número da Conta: " + numConta);
        System.out.println("Saldo: R$ " + saldo);
    }
}
