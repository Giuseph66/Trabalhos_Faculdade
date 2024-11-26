import java.time.LocalDate;
import java.time.Period;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Turma {
    private List<Aluno> Alunos = new ArrayList<>();
    
    public void cadastrarAluno(Aluno aluno) {
        for (Aluno a : Alunos) {
            if (a.getMatricula().equals(aluno.getMatricula())) { // Use equals para comparar Strings
                System.out.println("Erro: Matrícula já cadastrada.");
                return; // Sai do método sem adicionar
            }
        }
        Alunos.add(aluno); // Adiciona somente se nenhuma matrícula duplicada foi encontrada
        System.out.println("Aluno cadastrado com sucesso!");
    }
    

    public void listarTodosAlunos() {
        for (Aluno aluno : Alunos) {
            System.out.println(aluno);
        }
    }

    public void listarAlunosPorSobrenome(String sobrenome) {
        for (Aluno aluno : Alunos) {
            if (aluno.getNome().contains(sobrenome)) {
                System.out.println(aluno);
            }
        }
    }

    public void listarAlunoMaisIdoso() {
        if (Alunos.isEmpty()) {
            System.out.println("Nenhum aluno cadastrado.");
            return;
        }
        Aluno maisIdoso = Alunos.get(0);
        for (Aluno aluno : Alunos) {
            if (aluno.getDataNascimento().isBefore(maisIdoso.getDataNascimento())) {
                maisIdoso = aluno;
            }
        }
        System.out.println("Aluno mais idoso: " + maisIdoso);
    }

    public void calcularMediaIdade() {
        if (Alunos.isEmpty()) {
            System.out.println("Nenhum aluno cadastrado.");
            return;
        }
        int somaIdades = 0;
        for (Aluno aluno : Alunos) {
            somaIdades += Period.between(aluno.getDataNascimento(), LocalDate.now()).getYears();
        }
        double media = (double) somaIdades / Alunos.size();
        System.out.println("Média de idade: " + media);
    }

    public void atualizarAluno(String matricula) {
        for (Aluno aluno : Alunos) {
            if (aluno.getMatricula().equals(matricula)) {
                System.out.println("Dados atuais do aluno: " + aluno);
                aluno.lerDados();
                System.out.println("Dados atualizados com sucesso!");
                return;
            }
        }
        System.out.println("Erro: Matrícula não encontrada.");
    }
    
    public void removerAluno(String matricula) {
        for (Aluno aluno : Alunos) {
            if (aluno.getMatricula().equals(matricula)) {
                Alunos.remove(aluno);
                System.out.println("Aluno removido com sucesso!");
                return;
            }
        }
        System.out.println("Erro: Matrícula não encontrada.");
    }
}