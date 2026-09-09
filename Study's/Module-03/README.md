# Module-03 — Repetição (`for` e `while`)

Este módulo cobre **estruturas de repetição**: `while` e `for` com `range()`, incluindo acumuladores, contadores condicionais, loops aninhados e controle de fluxo com `break`/`continue`. Tudo combinado com o que já foi visto em variáveis, tipos, operadores e condicionais (`if`/`elif`/`else`) dos módulos anteriores.

Ainda **não** são abordados aqui: listas, tuplas, dicionários, métodos de string (`.split()`, `.replace()`, `.join()`, `.strip()`, slicing, indexação, `.upper()/.lower()`), funções (`def`), `match/case`.

Os arquivos seguem a convenção `NN-nome-descritivo.py`, com numeração sequencial e nome em inglês (kebab-case):

```
01-countdown.py
02-count-up.py
...
30-nested-multiplication-table.py
```

Comandos e conceitos novos são explicados com uma nota 💡 **apenas na primeira vez que aparecem** neste README.

Veja também os [desafios do Module-03](challenges/README.md) para exercícios de múltiplos passos que combinam tudo que foi aprendido aqui.

---

## Bloco 1 — `while` simples

## 01 — countdown

Peça ao usuário um número inteiro `start` e exiba uma contagem regressiva de `start` até `1`, um número por linha, usando `while`.

```python
counter = 3

while counter > 0:
    print(counter)
    counter -= 1

print("Fim!")
```

**Saída esperada (exemplo com `start = 5`):**
```
Digite o número inicial: 5
5
4
3
2
1
```

> 💡 **Comando novo:** `while <condição>:` — repete o bloco indentado enquanto a condição for verdadeira. É como um `if` que "volta" para testar a condição de novo a cada iteração.

> 💡 **Comando novo:** `-=` — operador de atribuição composta, equivalente a `start = start - 1`. Também existem `+=`, `*=`, `/=`, etc.

---

## 02 — count-up

Peça ao usuário um número inteiro `limit` e exiba uma contagem crescente de `1` até `limit`, um número por linha, usando `while`.

**Saída esperada (exemplo com `limit = 4`):**
```
Digite o limite: 4
1
2
3
4
```

---

## 03 — even-numbers-until-limit

Peça ao usuário um número inteiro `limit` e exiba todos os números pares de `0` até `limit` (inclusive), usando `while`.

**Saída esperada (exemplo com `limit = 10`):**
```
Digite o limite: 10
0
2
4
6
8
10
```

---

## 04 — multiples-of-three

Peça ao usuário um número inteiro `limit` e exiba todos os múltiplos de `3` entre `1` e `limit` (inclusive), usando `while`.

**Saída esperada (exemplo com `limit = 15`):**
```
Digite o limite: 15
3
6
9
12
15
```

---

## 05 — sum-until-negative

Peça ao usuário números inteiros repetidamente, um por vez, e some todos eles em uma variável `total`. O loop deve parar assim que o usuário digitar um número negativo. Ao final, exiba o `total` (sem contar o número negativo).

**Saída esperada (exemplo com entradas `5`, `3`, `2`, `-1`):**
```
Digite um número (negativo para parar): 5
Digite um número (negativo para parar): 3
Digite um número (negativo para parar): 2
Digite um número (negativo para parar): -1
Total: 10
```

---

## 06 — password-attempts

Defina uma variável `correct_password` com um valor fixo no código (ex.: `"python123"`). Peça ao usuário uma senha repetidamente usando `while`, até que ele acerte. Exiba `"Acesso liberado!"` quando a senha correta for digitada.

**Saída esperada (exemplo com tentativas erradas antes de acertar):**
```
Digite a senha: 123
Digite a senha: senha
Digite a senha: python123
Acesso liberado!
```

---

## Bloco 2 — `while` com acumulador e validação de input

## 07 — sum-of-n-numbers

Peça ao usuário quantos números ele quer somar (`amount`). Em seguida, peça cada número em um loop `while` e acumule a soma em `total`. Exiba o `total` ao final.

**Saída esperada (exemplo com `amount = 3` e valores `4`, `5`, `1`):**
```
Quantos números você vai somar? 3
Número 1: 4
Número 2: 5
Número 3: 1
Total: 10
```

> 💡 **Comando novo:** variável acumuladora — uma variável (ex.: `total = 0`) criada **antes** do loop e atualizada a cada iteração (`total += numero`), usada para guardar um resultado acumulado ao longo das repetições.

---

## 08 — average-of-n-numbers

Peça ao usuário quantos números ele vai informar (`amount`) e, em seguida, peça cada número em um loop, acumulando a soma. Ao final, calcule e exiba a média.

**Saída esperada (exemplo com `amount = 4` e valores `2`, `4`, `6`, `8`):**
```
Quantos números? 4
Número 1: 2
Número 2: 4
Número 3: 6
Número 4: 8
Média: 5.0
```

---

## 09 — positive-number-validation

Peça um número ao usuário repetidamente até que ele digite um valor maior que zero. Enquanto o número informado for inválido (menor ou igual a zero), exiba uma mensagem de erro e peça novamente.

**Saída esperada (exemplo com entradas `-3`, `0`, `7`):**
```
Digite um número positivo: -3
Valor inválido, tente novamente.
Digite um número positivo: 0
Valor inválido, tente novamente.
Digite um número positivo: 7
Número válido: 7
```

---

## 10 — menu-validation

Exiba um menu fixo com 3 opções (`1 - Cadastrar`, `2 - Consultar`, `3 - Sair`) e peça ao usuário para escolher uma opção. Enquanto a opção digitada não for `1`, `2` ou `3`, exiba `"Opção inválida."` e peça novamente. Ao final, exiba qual opção foi escolhida.

**Saída esperada (exemplo com entradas `5`, `2`):**
```
1 - Cadastrar
2 - Consultar
3 - Sair
Escolha uma opção: 5
Opção inválida.
Escolha uma opção: 2
Você escolheu: 2
```

---

## 11 — multiplication-accumulator

Peça ao usuário 5 números, um por vez, e calcule o produto (multiplicação) de todos eles usando um acumulador que começa em `1`.

**Saída esperada (exemplo com valores `2`, `3`, `1`, `4`, `2`):**
```
Número 1: 2
Número 2: 3
Número 3: 1
Número 4: 4
Número 5: 2
Produto total: 48
```

---

## 12 — even-odd-counter

Peça ao usuário quantos números ele vai informar (`amount`). Para cada número digitado, verifique se é par ou ímpar e conte quantos de cada tipo foram informados. Ao final, exiba as duas contagens.

**Saída esperada (exemplo com `amount = 4` e valores `2`, `5`, `8`, `7`):**
```
Quantos números? 4
Número 1: 2
Número 2: 5
Número 3: 8
Número 4: 7
Pares: 2
Ímpares: 2
```

---

## Bloco 3 — `for` com `range()`

## 13 — for-range-basic

Use um `for` com `range(5)` para exibir os números de `0` a `4`, um por linha.

```python
for letter_position in range(3):
    print("Volta número:", letter_position)
```

**Saída esperada:**
```
0
1
2
3
4
```

> 💡 **Comando novo:** `for <variável> in range(n):` — repete o bloco indentado `n` vezes, com a variável assumindo os valores `0, 1, 2, ..., n-1` a cada iteração.

> 💡 **Comando novo:** `range(n)` — gera uma sequência de números inteiros de `0` até `n-1`.

---

## 14 — for-range-start-end

Use `for` com `range(início, fim)` para exibir todos os números inteiros de `5` até `10` (inclusive).

**Saída esperada:**
```
5
6
7
8
9
10
```

> 💡 **Comando novo:** `range(início, fim)` — gera uma sequência de `início` até `fim - 1`. Por isso, para incluir o número `10`, é preciso usar `range(5, 11)`.

---

## 15 — for-range-step

Use `for` com `range(início, fim, passo)` para exibir os números pares de `0` até `20` (inclusive).

**Saída esperada:**
```
0
2
4
6
8
10
12
14
16
18
20
```

> 💡 **Comando novo:** `range(início, fim, passo)` — o terceiro argumento define de quanto em quanto a sequência avança. Pode ser negativo, para contar decrescente.

---

## 16 — countdown-with-for

Peça ao usuário um número `start` e use `for` com `range` e passo negativo para exibir uma contagem regressiva de `start` até `1`.

**Saída esperada (exemplo com `start = 5`):**
```
Digite o número inicial: 5
5
4
3
2
1
```

---

## 17 — multiplication-table

Peça ao usuário um número `number` e exiba a tabuada desse número, de `1` a `10`, usando `for`.

**Saída esperada (exemplo com `number = 7`):**
```
Digite um número: 7
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
```

---

## 18 — repeat-input-with-for

Peça ao usuário quantos nomes ele vai digitar (`amount`). Use `for` com `range(amount)` para pedir e exibir cada nome digitado, numerando as entradas.

**Saída esperada (exemplo com `amount = 3` e nomes `Ana`, `Bruno`, `Carla`):**
```
Quantos nomes? 3
Nome 1: Ana
Nome 2: Bruno
Nome 3: Carla
```

---

## Bloco 4 — Acumuladores e contadores condicionais (`for`/`while` + `if`)

## 19 — sum-even-numbers-for

Peça ao usuário um número `limit` e, usando `for` com `range`, some apenas os números pares entre `1` e `limit` (inclusive). Exiba a soma final.

**Saída esperada (exemplo com `limit = 10`):**
```
Digite o limite: 10
Soma dos pares: 30
```

---

## 20 — count-multiples-of-five

Peça ao usuário um número `limit` e conte, usando `for`, quantos múltiplos de `5` existem entre `1` e `limit` (inclusive).

**Saída esperada (exemplo com `limit = 23`):**
```
Digite o limite: 23
Múltiplos de 5 encontrados: 4
```

---

## 21 — highest-value-among-n

Peça ao usuário quantos números ele vai informar (`amount`) e, em seguida, cada número em um loop. Ao final, exiba o maior valor digitado, comparando os números conforme são informados (sem usar listas).

**Saída esperada (exemplo com `amount = 4` e valores `3`, `9`, `2`, `7`):**
```
Quantos números? 4
Número 1: 3
Número 2: 9
Número 3: 2
Número 4: 7
Maior valor: 9
```

---

## 22 — lowest-value-among-n

Igual ao exercício anterior, mas exibindo o **menor** valor digitado entre os `amount` números informados.

**Saída esperada (exemplo com `amount = 3` e valores `8`, `1`, `5`):**
```
Quantos números? 3
Número 1: 8
Número 2: 1
Número 3: 5
Menor valor: 1
```

---

## 23 — approved-students-counter

Peça ao usuário quantos alunos ele vai informar (`amount`) e, para cada aluno, peça a nota final (`grade`). Considere aprovado quem tirar nota maior ou igual a `7`. Ao final, exiba quantos alunos foram aprovados e quantos foram reprovados.

**Saída esperada (exemplo com `amount = 3` e notas `8`, `5`, `7`):**
```
Quantos alunos? 3
Nota do aluno 1: 8
Nota do aluno 2: 5
Nota do aluno 3: 7
Aprovados: 2
Reprovados: 1
```

---

## 24 — sum-and-average-with-validation

Peça ao usuário quantos números ele vai informar (`amount`). Para cada número, valide que ele seja maior que zero (repetindo a pergunta enquanto o valor for inválido, como no exercício 09), e acumule soma e contagem. Ao final, exiba a soma total e a média.

**Saída esperada (exemplo com `amount = 2` e valores `-1`, `4`, `6`):**
```
Quantos números? 2
Número 1: -1
Valor inválido, tente novamente.
Número 1: 4
Número 2: 6
Soma: 10
Média: 5.0
```

---

## Bloco 5 — Loops aninhados e `break`/`continue`

## 25 — nested-multiplication-table

Use dois `for` aninhados para exibir a tabuada de `1` a `5`, cada uma de `1` a `5`, separando cada tabuada com uma linha em branco.

```python
for outer in range(1, 3):
    for inner in range(1, 4):
        print(f"outer={outer}, inner={inner}")
    print()
```

**Saída esperada:**
```
1 x 1 = 1
1 x 2 = 2
1 x 3 = 3
1 x 4 = 4
1 x 5 = 5

2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10

3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15

4 x 1 = 4
4 x 2 = 8
4 x 3 = 12
4 x 4 = 16
4 x 5 = 20

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
```

> 💡 **Comando novo:** loop aninhado (**nested loop**) — um loop dentro de outro. Para cada iteração do loop externo, o loop interno é executado por completo.

---

## 26 — number-grid

Use dois `for` aninhados para exibir uma grade de números: para cada linha de `1` a `3`, exiba os números de `1` a `4` separados por espaço, na mesma linha.

```python
for number in range(1, 6):
    print(number, end=" ")

print()
print("Terminou a linha!")
```

**Saída esperada:**
```
1 2 3 4 
1 2 3 4 
1 2 3 4 
```

> 💡 **Comando novo:** `print(valor, end=" ")` — o argumento `end` define o que é impresso ao final do `print` no lugar da quebra de linha padrão. Aqui, usa espaço em vez de pular linha.

---

## 27 — stop-on-target-number

Peça ao usuário um número `target`. Em seguida, use `for` com `range(1, 21)` para exibir os números de `1` a `20`, mas pare o loop imediatamente (sem exibir os números seguintes) assim que o número exibido for igual a `target`.

```python
for number in range(1, 10):
    if number == 4:
        print("Achou o 4, parando o loop!")
        break
    print(number)
```

**Saída esperada (exemplo com `target = 6`):**
```
Digite o número alvo: 6
1
2
3
4
5
6
```

> 💡 **Comando novo:** `break` — encerra imediatamente o loop mais próximo (`for` ou `while`), pulando para a primeira linha depois dele.

---

## 28 — skip-multiples-of-three

Use `for` com `range(1, 21)` para exibir os números de `1` a `20`, **pulando** (sem exibir) os múltiplos de `3`.

```python
for number in range(1, 8):
    if number % 2 == 0:
        continue
    print(number)
```

**Saída esperada:**
```
1
2
4
5
7
8
10
11
13
14
16
17
19
20
```

> 💡 **Comando novo:** `continue` — interrompe a iteração atual do loop e passa direto para a próxima, sem executar o restante do bloco naquela volta.

---

## 29 — guess-the-number

Defina um número secreto fixo no código (`secret_number`). Peça ao usuário tentativas em um loop `while True`, exibindo `"Muito alto!"` ou `"Muito baixo!"` conforme o caso, e use `break` para encerrar o loop quando o usuário acertar, exibindo `"Você acertou!"`.

```python
attempts = 0

while True:
    attempts += 1
    print("Tentativa número:", attempts)

    if attempts == 3:
        print("Chega de tentativas!")
        break
```

**Saída esperada (exemplo com tentativas `50`, `30`, `42`):**
```
Tente adivinhar o número: 50
Muito alto!
Tente adivinhar o número: 30
Muito baixo!
Tente adivinhar o número: 42
Você acertou!
```

> 💡 **Comando novo:** `while True:` — cria um loop que repete indefinidamente, até ser interrompido por um `break` em algum ponto do bloco.

---

## 30 — full-purchase-loop-summary

Peça ao usuário quantos produtos ele vai comprar (`amount`). Use um loop para pedir o preço de cada produto, acumulando o total gasto. Se o usuário digitar um preço negativo em qualquer momento, exiba `"Preço inválido, compra cancelada."` e interrompa o loop imediatamente com `break`, sem exibir o total. Caso todos os preços sejam válidos, exiba o total gasto e a média de preço por produto ao final.

**Saída esperada (exemplo com `amount = 3` e preços `10`, `20`, `15`):**
```
Quantos produtos você vai comprar? 3
Preço do produto 1: 10
Preço do produto 2: 20
Preço do produto 3: 15
Total gasto: 45.0
Preço médio: 15.0
```

**Saída esperada (exemplo com `amount = 3` e preços `10`, `-5`):**
```
Quantos produtos você vai comprar? 3
Preço do produto 1: 10
Preço do produto 2: -5
Preço inválido, compra cancelada.
```

---

## Observações

- Todos os exercícios deste módulo usam apenas `while`, `for` com `range()`, `if`/`elif`/`else` e os comandos já vistos nos módulos anteriores — nada de listas, funções ou métodos de string.
- Os desafios do Module-03 estão em [`challenges/README.md`](challenges/README.md) e combinam os conceitos deste módulo em problemas de múltiplos passos.