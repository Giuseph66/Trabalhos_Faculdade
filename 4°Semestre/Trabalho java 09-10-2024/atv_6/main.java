package atv_6;

public class main {
    // Main para testar o programa
    public static void main(String[] args) {
        Carro carro = new Carro("ABC-1234"); // Criação do carro
        Pessoa pessoa = new Pessoa("João", carro); // Criação da pessoa associada ao carro

        // A pessoa interage com o carro
        pessoa.ligarCarro();
        pessoa.trocarMarcha(1);
        pessoa.acelerar();
        pessoa.frear();
        pessoa.desligarCarro();
    }
}
