package atv_3;

public class main {
    public static void main(String[] args) {
        ContaBancaria conta = new ContaBancaria("12345-6", "João Silva", 1000.0);

        conta.exibirInformacoes();
        conta.depositar(500.0);
        conta.exibirInformacoes();
        conta.sacar(300.0);
        conta.exibirInformacoes();
        conta.sacar(1000.0); 
        conta.exibirInformacoes();
        conta.sacar(300.0); 
        conta.sacar(-300.0); 
    }
}
