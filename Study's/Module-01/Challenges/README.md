# Module-01 — Desafios

Desafios extras deste módulo, separados da [lista principal de exercícios](../README.md). Aqui você usa os mesmos comandos já vistos (`print()`, variáveis, tipos, operadores aritméticos, `input()`, booleanos), mas combinados de forma mais criativa e em problemas com mais de um passo.

**Ainda sem `if`/`else`, `for`/`while`, listas ou métodos de string** — os desafios são resolvidos só com o que o Module-01 já cobriu, mesmo que exijam mais raciocínio para montar.

Resolva cada um em seu próprio arquivo seguindo a convenção de nome:

```
NN-nome-descritivo.py
```

Nenhum comando novo aparece aqui — se precisar relembrar o que algum comando faz, veja o [README de exercícios](../README.md).

---

## 01 — change-due

Dado um valor de compra (`purchase_value`) e um valor pago em dinheiro (`amount_paid`), calcule e imprima o troco a devolver.

**Saída esperada (exemplo com purchase_value=35.50, amount_paid=50):**
```
14.5
```

---

## 02 — weighted-average

Dadas três notas e seus respectivos pesos (ex: nota 7 com peso 2, nota 8 com peso 3, nota 9 com peso 5), calcule a média ponderada.

```python
weighted_average = (n1 * w1 + n2 * w2 + n3 * w3) / (w1 + w2 + w3)
```

**Saída esperada (exemplo com as notas e pesos acima):**
```
8.3
```

---

## 03 — currency-converter

Peça ao usuário um valor em reais (como texto) e uma cotação do dólar (como texto), converta ambos para `float`, e imprima o valor convertido em dólares, arredondado para 2 casas decimais.

**Saída esperada (exemplo digitando 100 e 5.20):**
```
19.23
```

---

## 04 — time-in-seconds

Peça ao usuário horas, minutos e segundos (três `input()` separados) e imprima o total convertido em segundos.

**Saída esperada (exemplo digitando 1 hora, 30 minutos, 15 segundos):**
```
5415
```

---

## 05 — discount-calculator

Dado um valor de compra (`purchase_value`), calcule o valor com 15% de desconto aplicado, e imprima tanto o valor do desconto quanto o valor final — sem usar `if` para checar faixas, é sempre 15% fixo.

**Saída esperada (exemplo com purchase_value=200):**
```
Desconto: 30.0
Valor final: 170.0
```

---

## 06 — split-the-bill

Dado o valor total de uma conta (`total_bill`) e o número de pessoas (`number_of_people`), calcule quanto cada pessoa deve pagar, incluindo 10% de gorjeta no valor total antes de dividir.

**Saída esperada (exemplo com total_bill=120, number_of_people=4):**
```
33.0
```

---

## 07 — triple-comparison

Peça ao usuário três números (via `input()`, convertidos para `float`) e imprima três booleanos: se o primeiro é maior que o segundo, se o segundo é maior que o terceiro, e se os três são diferentes entre si (usando `and`).

**Saída esperada (exemplo digitando 10, 5, 3):**
```
True
True
True
```

---

## 08 — full-temperature-converter

Peça ao usuário uma temperatura em Fahrenheit e converta para Celsius **e** para Kelvin, imprimindo os dois resultados.

```python
celsius = (fahrenheit - 32) * 5/9
kelvin = celsius + 273.15
```

**Saída esperada (exemplo digitando 98.6):**
```
37.0
310.15
```

---

## 09 — compound-interest-single-period

Dado um valor principal (`principal`), uma taxa de juros (`rate`) e o número de períodos (`periods`), calcule o montante final usando juros compostos.

```python
amount = principal * (1 + rate) ** periods
```

**Saída esperada (exemplo com principal=1000, rate=0.10, periods=2):**
```
1210.0
```

---

## 10 — full-sales-report

Peça ao usuário o nome de um produto, a quantidade vendida e o preço unitário (três `input()`). Calcule o valor total da venda, aplique 8% de imposto sobre esse total, e imprima um mini relatório com: nome do produto, quantidade, preço unitário, subtotal, valor do imposto e total com imposto — tudo usando f-strings, cada informação em uma linha.

**Saída esperada (exemplo: nome="Mouse", quantidade=3, preço=45.00):**
```
Produto: Mouse
Quantidade: 3
Preço unitário: 45.0
Subtotal: 135.0
Imposto: 10.8
Total: 145.8
```

---

## Observações

- Os desafios podem exigir mais de uma fórmula ou passo intermediário — releia o enunciado com calma antes de começar.
- Nenhum comando novo é introduzido aqui; tudo já foi visto na [lista de exercícios](../README.md).
- Se travar em algum, revisar o exercício correspondente no módulo principal costuma destravar.