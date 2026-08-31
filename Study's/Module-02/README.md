# Module-02 — Condicionais (if/else)

Este módulo cobre estruturas condicionais em Python: `if`, `if/else`, `if/elif/else`, condições compostas com `and`/`or` dentro de condicionais, e `if` aninhado. O objetivo é aprender a tomar decisões no código com base em condições, usando os comandos e operadores já vistos no Module-01 (variáveis, tipos, operadores aritméticos e de comparação, `input()`, `and`/`or`).

Este módulo **não** aborda: `for`/`while` (loops), listas/arrays, métodos de string (`.split()`, `.replace()`, `.join()`, `.strip()`, slicing, indexação, `.upper()/.lower()`, `len()`), funções (`def`), dicionários.

Os arquivos seguem a convenção `NN-nome-descritivo.py`, por exemplo:

```
15-grade-classification.py
```

Comandos novos são explicados apenas na primeira vez que aparecem neste README (nota 💡). Se precisar rever a explicação de algo, procure a primeira ocorrência do exercício correspondente.

Veja também os [desafios deste módulo](challenges/README.md).

---

## 01 — positive-check

Peça um número ao usuário e informe se ele é positivo.

```python
# apenas se o número for positivo, a mensagem é exibida
```

**Saída esperada (com entrada 7):**
```
O número é positivo.
```

> 💡 **Comando novo:** `if condição:` — executa o bloco indentado abaixo somente se a condição for verdadeira. Se for falsa, o bloco é simplesmente ignorado e o programa segue adiante.

---

## 02 — even-check

Peça um número e informe se ele é par (use o operador `%`).

**Saída esperada (com entrada 10):**
```
O número é par.
```

---

## 03 — adult-check

Peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais).

**Saída esperada (com entrada 20):**
```
Você é maior de idade.
```

---

## 04 — password-length-check

Peça uma senha (como texto) e avise se ela tem pelo menos 8 caracteres. Use `len()` para descobrir o tamanho da string.

**Saída esperada (com entrada "abc123"):**
```
Senha muito curta.
```

> 💡 **Nota:** `len()` já é permitido, pois mede o *tamanho* de uma string (uma contagem, não um método de manipulação de texto como `.upper()`). Ele retorna um `int` com a quantidade de caracteres.

---

## 05 — discount-eligibility

Peça o valor de uma compra e informe se ela é elegível para desconto (valor maior que R$100).

**Saída esperada (com entrada 150):**
```
Compra elegível para desconto.
```

---

## 06 — temperature-alert

Peça a temperatura atual e exiba um alerta apenas se ela for maior que 35 (graus Celsius).

**Saída esperada (com entrada 38):**
```
Alerta: temperatura muito alta!
```

---

## 07 — odd-or-even

Peça um número e informe se ele é par ou ímpar.

**Saída esperada (com entrada 7):**
```
O número é ímpar.
```

> 💡 **Comando novo:** `if condição: ... else: ...` — se a condição do `if` for falsa, o bloco do `else` é executado no lugar. Um dos dois blocos sempre roda.

---

## 08 — greater-of-two

Peça dois números e informe qual é o maior. Considere o caso de serem iguais também.

**Saída esperada (com entrada 5 e 5):**
```
Os números são iguais.
```

---

## 09 — pass-or-fail

Peça a média final de um aluno e informe se ele foi aprovado (média >= 6) ou reprovado.

**Saída esperada (com entrada 7.5):**
```
Aprovado.
```

---

## 10 — sign-check-nested

Peça um número e informe se ele é positivo, negativo ou zero — usando `if/else` aninhado (sem `elif` ainda, só pra comparar com a versão que vem depois).

```python
# dica de estrutura:
# if número == 0:
#     ...
# else:
#     if número > 0:
#         ...
#     else:
#         ...
```

**Saída esperada (com entrada -3):**
```
O número é negativo.
```

---

## 11 — voting-eligibility

Peça a idade e informe se a pessoa pode votar (16+), sendo obrigatório dos 18 aos 69, e facultativo entre 16-17 ou 70+. Por enquanto, apenas diferencie "pode votar" (16+) de "não pode votar" (<16) — sem detalhar a obrigatoriedade ainda (isso vem depois com `elif`).

**Saída esperada (com entrada 16):**
```
Pode votar.
```

---

## 12 — ticket-price

Peça a idade e informe se o ingresso é "Meia-entrada" (menor de 12 ou 60+) ou "Inteira".

**Saída esperada (com entrada 65):**
```
Meia-entrada.
```

---

## 13 — number-parity-message

Peça um número inteiro e exiba uma frase completa dizendo se ele é par ou ímpar, incluindo o próprio número na mensagem (use f-string).

**Saída esperada (com entrada 4):**
```
O número 4 é par.
```

---

## 14 — balance-status

Peça o saldo de uma conta bancária e informe se está "Positivo" ou "Negativo" (considere zero como "Positivo").

**Saída esperada (com entrada -50):**
```
Saldo Negativo.
```

---

## 15 — grade-classification

Peça a nota de um aluno (0 a 10) e classifique em conceito: A (>=9), B (>=7), C (>=5), D (<5).

```python
# dica de estrutura:
# if nota >= 9:
#     ...
# elif nota >= 7:
#     ...
# elif nota >= 5:
#     ...
# else:
#     ...
```

**Saída esperada (com entrada 8):**
```
Conceito: B
```

> 💡 **Comando novo:** `elif condição:` — abreviação de "else if". Permite encadear várias condições em sequência; Python testa cada uma na ordem e executa apenas o primeiro bloco cuja condição for verdadeira, ignorando os demais.

---

## 16 — bmi-category

Peça peso (kg) e altura (m), calcule o IMC (`peso / altura ** 2`) e classifique: Abaixo do peso (<18.5), Normal (18.5–24.9), Sobrepeso (25–29.9), Obesidade (>=30).

**Saída esperada (com entrada 70 e 1.75):**
```
IMC: 22.86
Classificação: Normal
```

---

## 17 — age-group

Peça a idade e classifique em: Criança (0–11), Adolescente (12–17), Adulto (18–59), Idoso (60+).

**Saída esperada (com entrada 15):**
```
Faixa etária: Adolescente
```

---

## 18 — weekday-number

Peça um número de 1 a 7 e exiba o nome do dia da semana correspondente (1 = Domingo). Se o número for inválido, exiba uma mensagem de erro.

**Saída esperada (com entrada 3):**
```
Terça-feira
```

---

## 19 — season-by-month

Peça o número do mês (1–12) e informe a estação do ano (considere o hemisfério sul: Verão = Dez/Jan/Fev, Outono = Mar/Abr/Mai, Inverno = Jun/Jul/Ago, Primavera = Set/Out/Nov).

**Saída esperada (com entrada 7):**
```
Inverno
```

---

## 20 — shipping-cost

Peça o peso de um pacote (kg) e calcule o frete: até 1kg = R$10, até 5kg = R$25, até 10kg = R$45, acima de 10kg = R$70.

**Saída esperada (com entrada 3):**
```
Frete: R$25.00
```

---

## 21 — triangle-classification-by-sides

Peça os três lados de um triângulo e classifique: Equilátero (todos iguais), Isósceles (dois iguais), Escaleno (todos diferentes). Não se preocupe em validar se os lados formam um triângulo válido.

**Saída esperada (com entrada 5, 5 e 8):**
```
Triângulo Isósceles.
```

---

## 22 — tax-bracket

Peça o salário e calcule a alíquota de imposto: até 2000 = isento, até 4000 = 10%, até 8000 = 20%, acima de 8000 = 27%.

**Saída esperada (com entrada 5000):**
```
Alíquota: 20%
```

---

## 23 — grade-with-attendance

Peça a média final e a frequência (%). Se a frequência for menor que 75, o aluno está reprovado por falta, independente da nota. Caso contrário, aplique a mesma lógica de aprovação por nota (>= 6 aprovado).

**Saída esperada (com entrada média 8 e frequência 60):**
```
Reprovado por falta.
```

> 💡 **Nota:** isso já antecipa o próximo bloco (condições compostas), mas resolvido só com `if/elif/else` em sequência — mostra por que às vezes um `and` deixa o código mais enxuto.

---

## 24 — day-period

Peça uma hora (0–23) e informe o período do dia: Madrugada (0–5), Manhã (6–11), Tarde (12–17), Noite (18–23).

**Saída esperada (com entrada 14):**
```
Boa tarde!
```

---

## 25 — leap-year

Peça um ano e informe se é bissexto. Regra: divisível por 4 E (não divisível por 100 OU divisível por 400).

```python
# dica: combine and/or numa única condição
```

**Saída esperada (com entrada 2000):**
```
2000 é bissexto.
```

> 💡 **Nota:** `and`/`or` já foram vistos no Module-01 como operadores lógicos; aqui eles passam a ser usados *dentro* da condição de um `if`, o que é o padrão mais comum de uso deles.

---

## 26 — login-check

Peça usuário e senha, compare com valores fixos no código (ex: usuário esperado `"admin"`, senha esperada `"1234"`). Informe se o login foi bem-sucedido — só é bem-sucedido se AMBOS estiverem corretos.

**Saída esperada (com entrada usuário "admin" e senha "0000"):**
```
Login inválido.
```

---

## 27 — number-range-check

Peça um número e informe se ele está entre 10 e 20 (inclusive) usando uma única condição com `and`.

**Saída esperada (com entrada 15):**
```
O número está no intervalo.
```

---

## 28 — discount-with-conditions

Peça o valor da compra e se o cliente é membro do clube de fidelidade (responda "sim" ou "não" como string). O desconto de 15% só se aplica se o valor for maior que R$200 E o cliente for membro.

**Saída esperada (com entrada 300 e "sim"):**
```
Desconto aplicado! Valor final: R$255.00
```

---

## 29 — event-eligibility

Peça a idade e se a pessoa está acompanhada de um responsável ("sim"/"não"). A entrada é permitida se a idade for >= 18, OU se for menor de 18 mas estiver acompanhada.

**Saída esperada (com entrada 15 e "sim"):**
```
Entrada permitida.
```

---

## 30 — triangle-validity

Peça os três lados de um triângulo e informe se eles formam um triângulo válido. Regra: a soma de quaisquer dois lados deve ser maior que o terceiro (as três condições precisam ser verdadeiras ao mesmo tempo).

**Saída esperada (com entrada 3, 4 e 5):**
```
Os lados formam um triângulo válido.
```

---

## 31 — grade-and-behavior

Peça a média de um aluno e, dentro da lógica de aprovação, adicione uma verificação extra: se a média for exatamente 6 ou 7 (a chamada "zona de recuperação"), pergunte também o comportamento ("bom"/"ruim") para decidir aprovação — usando `if` aninhado dentro do `elif`.

**Saída esperada (com entrada média 6 e comportamento "bom"):**
```
Aprovado (zona de recuperação, comportamento bom).
```

> 💡 **Nota:** aqui um `if` aparece *dentro* do bloco de outro `if`/`elif` — isso é chamado de aninhamento (nested if). Cada nível de aninhamento tem sua própria indentação.

---

## 32 — discount-with-extra-tier

Peça o valor da compra e classifique o desconto por faixas de valor (0%, 5%, 10%, 15%). Dentro da faixa de 15% (valor > R$500), adicione uma checagem aninhada: se o valor for maior que R$1000, o desconto sobe pra 20%.

**Saída esperada (com entrada 1200):**
```
Desconto: 20%
Valor final: R$960.00
```

---

## 33 — triangle-type-and-validity

Combine os dois exercícios anteriores de triângulo: primeiro verifique (com `if` aninhado) se os lados formam um triângulo válido; só se for válido, classifique em Equilátero/Isósceles/Escaleno.

**Saída esperada (com entrada 1, 2 e 10):**
```
Esses lados não formam um triângulo válido.
```

---

## 34 — loan-approval

Peça renda mensal e valor do empréstimo solicitado. Primeiro verifique se a renda é suficiente (renda >= valor / 10); se for, verifique aninhadamente se o cliente já tem outro empréstimo em aberto ("sim"/"não") — se tiver, é preciso aprovação manual; se não tiver, é aprovado automaticamente.

**Saída esperada (com entrada renda 3000, valor 20000 e outro empréstimo "não"):**
```
Empréstimo aprovado automaticamente.
```

---

## 35 — full-purchase-summary

Exercício final do módulo, combinando tudo: peça o valor da compra, se o cliente é membro ("sim"/"não") e a forma de pagamento ("pix" ou "cartão"). Aplique nessa ordem: desconto de membro (10%, aninhado dentro da checagem de valor > R$100), depois desconto extra de pagamento à vista via Pix (mais 5% sobre o valor já com desconto). Exiba o valor final.

**Saída esperada (com entrada 300, membro "sim", pagamento "pix"):**
```
Valor final: R$256.50
```

---

## Observações

- A ordem dos exercícios segue: `if` simples → `if/else` → `if/elif/else` → condições compostas (`and`/`or`) → `if` aninhado.
- Este módulo não usa `for`/`while`, listas, nem métodos de string — isso fica para módulos futuros.
- Veja os [desafios deste módulo](challenges/README.md) para exercícios que combinam esses conceitos de forma mais livre.
