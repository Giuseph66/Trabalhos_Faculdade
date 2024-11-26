package atv_1;

public class Pessoa {
    private String nome;
    private int idade;
    private String profissao;

    public Pessoa(String nome, int idade, String profissao) {
        this.nome = nome;
        this.idade = idade;
        this.profissao = profissao;
    }

    public int calcularAnosBissextos() {
        int anoAtual = 2024; 
        int anoNascimento = anoAtual - idade;
        int anosBissextos = 0;

        for (int ano = anoNascimento; ano <= anoAtual; ano++) {
            if (isBissexto(ano)) {
                anosBissextos++;
            }
        }
        return anosBissextos;
    }

    private boolean isBissexto(int ano) {
        return (ano % 4 == 0 && ano % 100 != 0) || (ano % 400 == 0);
    }

    public void exibirInformacoes() {
        System.out.println("Nome: " + nome);
        System.out.println("Idade: " + idade + " anos");
        System.out.println("Profissão: " + profissao);
        System.out.println("Anos bissextos vividos: " + calcularAnosBissextos());
    }
}
