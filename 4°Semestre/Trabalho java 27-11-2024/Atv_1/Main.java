import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Turma turma = new Turma();
        Scanner scanner = new Scanner(System.in);
        int opcao = -1;

        do {
            System.out.println("\nMenu:");
            System.out.println("1. Cadastrar aluno");
            System.out.println("2. Listar todos os alunos");
            System.out.println("3. Listar alunos por sobrenome");
            System.out.println("4. Listar aluno mais velho");
            System.out.println("5. Calcular média de idade");
            System.out.println("6. Atualizar aluno");
            System.out.println("7. Remover aluno");
            System.out.println("0. Sair");

            // Validação da entrada
            boolean entradaValida = false;
            while (!entradaValida) {
                try {
                    System.out.print("Escolha uma opção: ");
                    opcao = scanner.nextInt();
                    scanner.nextLine(); // Consumir a quebra de linha
                    entradaValida = true;
                } catch (java.util.InputMismatchException e) {
                    System.out.println("Erro: Entrada inválida. Digite um número.");
                    scanner.nextLine(); // Limpar entrada inválida
                }
            }

            switch (opcao) {
                case 1:
                    Aluno aluno = new Aluno();
                    aluno.lerDados();
                    turma.cadastrarAluno(aluno);
                    break;
                case 2:
                    turma.listarTodosAlunos();
                    break;
                case 3:
                    System.out.print("Digite o sobrenome: ");
                    String sobrenome = scanner.nextLine();
                    turma.listarAlunosPorSobrenome(sobrenome);
                    break;
                case 4:
                    turma.listarAlunoMaisIdoso();
                    break;
                case 5:
                    turma.calcularMediaIdade();
                    break;
                case 6:
                    System.out.print("Digite a matrícula do aluno a ser atualizado: ");
                    String matriculaAtualizar = scanner.nextLine();
                    turma.atualizarAluno(matriculaAtualizar);
                    break;
                case 7:
                    System.out.print("Digite a matrícula do aluno a ser removido: ");
                    String matriculaRemover = scanner.nextLine();
                    turma.removerAluno(matriculaRemover);
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida. Escolha uma opção válida.");
            }
        } while (opcao != 0);

        scanner.close();
    }
}
