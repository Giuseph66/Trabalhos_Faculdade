package atv_10;

public abstract class Contribuinte {
    protected String nome;
    protected double rendaBruta;

    public Contribuinte(String nome, double rendaBruta) {
        this.nome = nome;
        this.rendaBruta = rendaBruta;
    }

    public abstract double calcularImposto();

    public void exibirInfo() {
        System.out.println("Nome: " + nome);
        System.out.println("Renda Bruta: R$ " + rendaBruta);
        System.out.println("Imposto a pagar: R$ " + calcularImposto());
    }
}
