# Module-01 — Fundamentos

Lista de exercícios deste módulo: `print()`, variáveis, tipos de dados, operadores aritméticos, `input()` e booleanos.

**Ainda não abordado neste módulo:** `if`/`else`, `for`/`while`, listas/arrays, métodos de string (`split`, `replace`, etc). Isso vem depois — todo exercício aqui é resolvível só com print, variáveis, matemática e conversão básica de tipo.

Resolva cada um em seu próprio arquivo seguindo a convenção de nome:

```
NN-nome-descritivo.py
```

Cada exercício é resolvível com o que já foi introduzido até ali. Comandos novos são explicados **na primeira vez que aparecem** — depois disso, já é esperado que você os conheça. Se um comando não estiver explicado onde você está, role para cima — ele foi introduzido antes.

Os desafios deste módulo (problemas extras, separados desta lista) ficam em [`challenges/`](./challenges/).

---

## 01 — hello

Imprima `"Hello, world!"` no console.

```python
print("Hello, world!")
```

**Saída esperada:**
```
Hello, world!
```

> 💡 **Comando novo:** `print()` — exibe texto (ou qualquer valor) no console. Tudo que estiver dentro dos parênteses é mostrado.

---

## 02 — hello-name

Guarde seu nome em uma variável e imprima uma saudação usando ela, tipo `"Hello, John!"`.

**Saída esperada (exemplo com nome "John"):**
```
Hello, John!
```

> 💡 **Conceito novo:** variáveis — um nome que guarda um valor, criado com `nome = valor`. Não é preciso declarar o tipo; o Python identifica sozinho.

---

## 03 — multi-print

Imprima três linhas diferentes de texto usando três chamadas separadas de `print()`.

**Saída esperada (exemplo):**
```
Primeira linha
Segunda linha
Terceira linha
```

---

## 04 — string-concat

Crie duas variáveis de texto (primeiro nome, sobrenome) e imprima elas combinadas em um nome completo usando `+`.

**Saída esperada (exemplo):**
```
John Doe
```

> 💡 **Conceito novo:** concatenação de strings — juntar textos com `+`. Os dois lados precisam ser strings, senão o Python gera um erro.

---

## 05 — f-string-intro

Repita o exercício 04, mas usando f-string em vez de `+`.

```python
name = "John"
print(f"Hello, {name}!")
```

**Saída esperada:**
```
Hello, John!
```

> 💡 **Sintaxe nova:** f-strings — `f"Hello, {name}"`. Tudo dentro de `{}` é avaliado e inserido no texto. Mais limpo que concatenação.

---

## 06 — int-vs-float

Crie uma variável inteira e uma variável float, imprima as duas junto com o tipo delas usando `type()`.

**Saída esperada (exemplo):**
```
10 <class 'int'>
3.5 <class 'float'>
```

> 💡 **Comando novo:** `type()` — retorna o tipo de dado de um valor (`int`, `float`, `str`, `bool`, etc).

---

## 07 — basic-math

Crie duas variáveis numéricas e imprima o resultado da soma, subtração, multiplicação e divisão delas.

**Saída esperada (exemplo com 10 e 3):**
```
13
7
30
3.3333333333333335
```

---

## 08 — division-types

Divida dois números inteiros usando `/` e depois usando `//`. Imprima os dois resultados e explique a diferença em um comentário.

**Saída esperada (exemplo com 7 e 2):**
```
3.5
3
```

> 💡 **Operador novo:** `//` — divisão inteira (floor division), descarta a parte decimal. `7 / 2` é `3.5`, `7 // 2` é `3`.

---

## 09 — modulo-intro

Imprima o resto da divisão de dois números.

**Saída esperada (exemplo com 7 e 2):**
```
1
```

> 💡 **Operador novo:** `%` (módulo) — retorna o resto de uma divisão. `7 % 2` é `1`.

---

## 10 — total-pay

Dadas as variáveis `hours_worked` e `hourly_rate`, calcule e imprima o pagamento total.

**Saída esperada (exemplo com 8 horas e R$25/hora):**
```
200.0
```

---

## 11 — input-basics

Peça o nome do usuário usando `input()` e imprima uma saudação com ele.

**Saída esperada (exemplo, digitando "Maria"):**
```
Hello, Maria!
```

> 💡 **Comando novo:** `input()` — pausa a execução e espera o usuário digitar algo, sempre retorna um `str`.

---

## 12 — input-number

Peça dois números ao usuário (como texto) e imprima a soma deles. Cuidado — `input()` sempre retorna texto.

**Saída esperada (exemplo digitando 4 e 6):**
```
10
```

> 💡 **Comando novo:** `int()` — converte um valor para número inteiro. Necessário porque `input()` retorna uma string, não um número. Também existe `float()` para decimais.

---

## 13 — celsius-to-fahrenheit

Peça ao usuário uma temperatura em Celsius e converta para Fahrenheit.

```python
F = C * 9/5 + 32
```

**Saída esperada (exemplo com 100°C):**
```
212.0
```

---

## 14 — boolean-intro

Crie duas variáveis booleanas e imprima elas, junto com o resultado de combiná-las com `and` e `or`.

**Saída esperada (exemplo com True e False):**
```
True
False
False
True
```

> 💡 **Tipo novo:** `bool` — `True` ou `False`. `and` / `or` combinam expressões booleanas.

---

## 15 — comparisons

Crie duas variáveis numéricas e imprima o resultado de compará-las com `==`, `!=`, `>`, `<`.

**Saída esperada (exemplo com 5 e 8):**
```
False
True
False
True
```

---

## 16 — rectangle-area

Dadas as variáveis `width` e `height`, calcule e imprima a área de um retângulo.

**Saída esperada (exemplo com width=4, height=5):**
```
20
```

---

## 17 — circle-area

Dada a variável `radius`, calcule e imprima a área de um círculo. Use `3.14159` como valor de pi (sem imports ainda).

```python
area = 3.14159 * radius * radius
```

**Saída esperada (exemplo com radius=3):**
```
28.27431
```

---

## 18 — average-of-three

Crie três variáveis numéricas e imprima a média delas.

**Saída esperada (exemplo com 4, 8, 6):**
```
6.0
```

---

## 19 — input-float

Peça ao usuário o preço de um produto (como texto) e imprima ele convertido para `float`, junto com o `type()`.

**Saída esperada (exemplo digitando 19.90):**
```
19.9 <class 'float'>
```

---

## 20 — temperature-range

Dadas duas variáveis de temperatura (`today` e `yesterday`), imprima o resultado de comparar se hoje está mais quente usando `>`, sem usar `if` — apenas imprima o booleano direto.

**Saída esperada (exemplo com today=25, yesterday=22):**
```
True
```

---

## 21 — is-adult

Peça a idade do usuário (convertida para `int`) e imprima o resultado de compará-la com `18` usando `>=` — só o booleano, sem `if` ainda.

**Saída esperada (exemplo digitando 20):**
```
True
```

---

## 22 — string-vs-number

Crie uma variável guardando `"5"` (como texto) e outra guardando `5` (como número). Imprima as duas, depois imprima o resultado de comparar elas com `==`. Explique em um comentário por que o resultado é esse.

**Saída esperada:**
```
5
5
False
```

---

## 23 — combined-conversion

Peça ao usuário dois números como texto, converta os dois para `float`, e imprima a soma, a diferença e o produto deles.

**Saída esperada (exemplo digitando 10 e 4):**
```
14.0
6.0
40.0
```

---

## 24 — multiple-assignment

Atribua três variáveis em uma única linha e imprima elas.

```python
a, b, c = 1, 2, 3
```

**Saída esperada:**
```
1
2
3
```

---

## 25 — simple-interest

Dadas as variáveis `principal`, `rate` e `time`, calcule o juro simples.

```python
interest = principal * rate * time
```

**Saída esperada (exemplo com principal=1000, rate=0.05, time=2):**
```
100.0
```

---

## 26 — round-numbers

Peça um float e imprima ele arredondado para 2 casas decimais.

**Saída esperada (exemplo digitando 3.14159):**
```
3.14
```

> 💡 **Comando novo:** `round(valor, casas)` — arredonda um número para a quantidade de casas decimais informada.

---

## 27 — abs-value

Peça um número e imprima o valor absoluto dele.

**Saída esperada (exemplo digitando -7):**
```
7
```

> 💡 **Comando novo:** `abs()` — retorna o valor absoluto (não-negativo) de um número.

---

## 28 — const-naming

Crie três variáveis que representem constantes (ex: `PI`, `MAX_USERS`) seguindo a convenção de nomenclatura do Python para constantes, e imprima elas.

**Saída esperada (exemplo):**
```
3.14159
100
```

> 💡 **Convenção nova:** Python não tem constantes de verdade, mas por convenção nomes que nunca devem mudar são escritos em `ALL_CAPS` (maiúsculas).

---

## 29 — comment-practice

Pegue qualquer exercício anterior e adicione um comentário `#` acima de cada linha explicando o que ela faz.

> 💡 **Sintaxe nova:** `#` inicia um comentário — ignorado pelo Python, usado para explicar o código para humanos.

---

## 30 — mini-receipt

Dadas as variáveis `item_name`, `item_price` e `quantity`, imprima um pequeno recibo formatado mostrando o item, quantidade, preço unitário e total (preço × quantidade), usando f-string.

**Saída esperada (exemplo: item="Caderno", price=5.50, quantity=3):**
```
Item: Caderno
Quantidade: 3
Preço unitário: 5.5
Total: 16.5
```

---

## 31 — bmi-calculator

Peça peso (kg) e altura (m) ao usuário, calcule o IMC, e imprima o resultado arredondado para 1 casa decimal.

```python
bmi = weight / height ** 2
```

**Saída esperada (exemplo com weight=70, height=1.75):**
```
22.9
```

> 💡 **Operador novo:** `**` — exponenciação (potência). `height ** 2` significa altura ao quadrado.

---

## 32 — variable-type-juggling

Crie uma variável guardando um número como texto (ex: `"42"`), converta para `int`, faça uma conta com ela, depois converta o resultado de volta para `str` e imprima concatenado com texto.

**Saída esperada (exemplo com "42" e +8):**
```
O resultado é 50
```

> 💡 **Comando novo:** `str()` — converte um valor para string. Útil para concatenar números com texto usando `+`.

---

## Observações

- Resolva os exercícios em ordem — os seguintes assumem que você já domina os comandos introduzidos antes.
- Nenhum `if`/`else`, `for`/`while`, listas ou métodos de string aqui — isso vem em outro módulo assim que for abordado em aula ou aqui.
- Os desafios deste módulo (problemas extras, fora desta lista principal) ficam em [`challenges/`](./challenges/).