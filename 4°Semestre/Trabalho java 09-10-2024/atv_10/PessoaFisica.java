package atv_10;

public class PessoaFisica extends Contribuinte {
    public PessoaFisica(String nome, double rendaBruta) {
        super(nome, rendaBruta);
    }
    @Override
    public double calcularImposto() {
        double imposto = 0;
        double deducao = 0;
        double aliquota = 0;

        if (rendaBruta <= 1400) {
            aliquota = 0;
            deducao = 0;
        } else if (rendaBruta <= 2100) {
            aliquota = 0.10;
            deducao = 100;
        } else if (rendaBruta <= 2800) {
            aliquota = 0.15;
            deducao = 270;
        } else if (rendaBruta <= 3600) {
            aliquota = 0.25;
            deducao = 500;
        } else {
            aliquota = 0.30;
            deducao = 700;
        }

        imposto = (rendaBruta * aliquota) - deducao;
        return imposto;
    }
}
