package atv_6;

public class Pessoa {
    
    private String nome;
    private Carro meuCarro;

    public Pessoa(String nome, Carro carro) {
        this.nome = nome;
        this.meuCarro = carro;
    }

    public void ligarCarro() {
        meuCarro.ligar();
    }

    public void trocarMarcha(int marcha) {
        meuCarro.trocarMarcha(marcha);
    }

    public void acelerar() {
        meuCarro.acelerar();
    }

    public void frear() {
        meuCarro.frear();
    }

    public void desligarCarro() {
        meuCarro.desligar();
    }
}
