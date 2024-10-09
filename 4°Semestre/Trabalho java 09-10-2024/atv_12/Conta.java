package atv_12;

public abstract class Conta {
    protected double saldo;

    public void depositar(double valor) {
        saldo += valor;
    }

    public boolean sacar(double valor) {
        if (saldo >= valor) {
            saldo -= valor;
            return true;
        } else {
            System.out.println("Saldo insuficiente.");
            return false;
        }
    }
    public double obterSaldo() {
        return saldo;
    }
}

