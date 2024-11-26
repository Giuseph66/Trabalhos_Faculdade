package atv_3;

public class ContaBancaria {
        private String numeroConta;
        private String nomeTitular;
        private double saldo;
    
        public ContaBancaria(String numeroConta, String nomeTitular, double saldo) {
            this.numeroConta = numeroConta;
            this.nomeTitular = nomeTitular;
            this.saldo = saldo;
        }
        public void depositar(double valor) {
            if (valor > 0) {
                saldo += valor;
                System.out.println("Depósito de R$ " + valor + " realizado com sucesso.");
            } else {
                System.out.println("O valor do depósito deve ser positivo.");
            }
        }
        public void sacar(double valor) {
            if (valor > 0 && valor <= saldo) {
                saldo -= valor;
                System.out.println("Saque de R$ " + valor + " realizado com sucesso.");
            } else if (valor > saldo) {
                System.out.println("Saldo insuficiente para realizar o saque.");
            } else {
                System.out.println("O valor do saque deve ser positivo.");
            }
        }
        public void exibirInformacoes() {
            System.out.println("Número da conta: " + numeroConta);
            System.out.println("Titular: " + nomeTitular);
            System.out.println("Saldo: R$ " + saldo);
        }
    }
