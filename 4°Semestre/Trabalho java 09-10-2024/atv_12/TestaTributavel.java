package atv_12;

public class TestaTributavel {
    public static void main(String[] args) {
        ContaCorrente cc = new ContaCorrente();
        cc.depositar(5000);
        System.out.println("Saldo Conta Corrente: R$ " + cc.obterSaldo());

        System.out.println("Tributos Conta Corrente: R$ " + cc.calculaTributos());

        ContaPoupanca cp = new ContaPoupanca();
        cp.depositar(500);
        System.out.println("Saldo Conta Poupança: R$ " + cp.obterSaldo());

        SeguroDeVida seguro = new SeguroDeVida();
        System.out.println("Tributos Seguro de Vida: R$ " + seguro.calculaTributos());
    }
}
