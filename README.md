Criar uma calculadora capaz de realizar diversas operações matemáticas, com tratamento de erros e interação contínua com o usuário até que ele decida sair.

Como funciona
Laço infinito (while True)

Mantém o programa rodando até o usuário optar por sair.

Escolha do operador

O usuário digita qual operação quer fazer:

+ → soma

- → subtração

* → multiplicação

/ → divisão

** → potência

// → divisão inteira

% → cálculo de porcentagem

Entrada de valores

O programa solicita dois números.

Antes de prosseguir, ele verifica se são válidos usando .isdigit() (o que limita a números inteiros positivos, no seu código original).

Execução da operação

Dependendo do operador escolhido, o cálculo é feito.

O resultado é exibido formatado no terminal.

Repetição ou saída

Após cada cálculo, o usuário decide se quer continuar ou sair (s/n).

Tratamento de erros

Usa try/except para capturar erros e evitar que o programa quebre.

💡 Recursos utilizados
Estrutura de repetição while

Condições if/elif para escolher operações

Validação de entradas (isdigit())

Biblioteca math para cálculo de potência

F-strings para formatação de saída

Tratamento de exceções com try/except# calculadora
calculadora interativa diretamente no terminal
