import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.Scanner;

public class Aluno {
    private String Matricula;
    private String Nome;
    private LocalDate DataNascimento;
    private char Sexo;

    public String getMatricula() {
        return Matricula;
    }

    public void setMatricula(String Matricula) {
        this.Matricula = Matricula;
    }

    public String getNome() {
        return Nome;
    }

    public void setNome(String Nome) {
        this.Nome = Nome;
    }

    public LocalDate getDataNascimento() {
        return DataNascimento;
    }

    public void setDataNascimento(String DataNascimento) {
        try {
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
            this.DataNascimento = LocalDate.parse(DataNascimento, formatter);
        } catch (java.time.format.DateTimeParseException e) {
            throw new IllegalArgumentException("Data de nascimento inválida. Use o formato dd/MM/yyyy.");
        }
    }

    public char getSexo() {
        return Sexo;
    }

    public void setSexo(char Sexo) {
        this.Sexo = Sexo;
    }

    public void lerDados() {
        Scanner scanner = new Scanner(System.in);

        Matricula = Utils.validarEntradaTexto("Digite a matrícula: ", scanner);
        Nome = Utils.validarEntradaTexto("Digite o nome: ", scanner);

        boolean dataValida = false;
        while (!dataValida) {
            try {
                String data = Utils.validarEntradaTexto("Digite a data de nascimento (dd/MM/yyyy): ", scanner);
                setDataNascimento(data);
                dataValida = true;
            } catch (IllegalArgumentException e) {
                System.out.println(e.getMessage());
            }
        }

        Sexo = Utils.validarEntradaTexto("Digite o sexo (M/F): ", scanner).toUpperCase().charAt(0);
    }

    @Override
    public String toString() {
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy");
        return "Matrícula: " + Matricula + ", Nome: " + Nome + 
               ", Data de Nascimento: " + DataNascimento.format(formatter) + 
               ", Sexo: " + Sexo;
    }
}
