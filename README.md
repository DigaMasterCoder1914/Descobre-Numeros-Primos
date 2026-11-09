🔢 Verificador de Números Primos em PythonScript em Python desenvolvido para identificar se um determinado número inteiro positivo é primo (divisível apenas por 1 e por ele mesmo). O programa permite testar múltiplos números em sequência através de um loop interativo no terminal e contabiliza quantos números primos foram encontrados ao final da execução.🛠️ FuncionalidadesValidação de Entrada: Garante a leitura de números inteiros maiores ou iguais a 1.Checagem por Paridade: Separa a lógica de verificação entre números pares (onde apenas o número 2 é primo) e ímpares.Teste de Divisibilidade: Avalia se números ímpares possuem divisores inteiros no intervalo entre 3 e a metade do próprio número.Modo Interativo: Permite testar vários números consecutivos e exibe o total acumulado de números primos identificados ao encerrar.📐 Estrutura de FunçõesFunçãoDescriçãopergunta_Numero()Garante a leitura de um número inteiro $\ge 1$ através do input().E_Par()Retorna True se o número for par e False caso seja ímpar.Verifica_Primo_Par()Trata o caso de números pares (retorna True apenas para o número 2).verifica_Primo_Impar()Trata o número 1 (False) e testa se o número ímpar possui divisores no intervalo de 3 até $N // 2$.Imprime_Mensagem()Formata e imprime se o número é ou não primo no console.Fluxo()Orquestra a execução da verificação para uma única entrada e retorna o status.Main()Controla a repetição do programa, contabiliza os primos encontrados e exibe a contagem final.💻 Exemplo de Execução no TerminalPlaintextDigite um número para verififcar se ele é primo 
7
O número 7 é um número primo
Deseja Continuar a verificar primos?
Digite sim para continuar a rodar o programa 
sim
Digite um número para verififcar se ele é primo 
9
O número 9 Não é um número primo
Deseja Continuar a verificar primos?
Digite sim para continuar a rodar o programa 
nao
Voce achou 1 Números Primos 
🚀 Como ExecutarPré-requisitosPython 3.x instalado no ambiente.ExecuçãoSalve o código em um arquivo .py (exemplo: verificador_primos.py).Abra o terminal na pasta onde o arquivo foi salvo e execute:Bashpython verificador_primos.py
