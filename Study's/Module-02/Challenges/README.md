# Module-02 — Desafios

Estes são problemas de mais de um passo, combinando de forma mais livre e criativa os comandos já vistos no módulo (`if`, `else`, `elif`, condições compostas com `and`/`or`, `if` aninhado). Nenhum comando novo é introduzido aqui — apenas recombinações do que já foi aprendido.

Veja a [lista principal de exercícios](../README.md).

---

## 01 — change-due

Dado um valor de compra (`purchase_value`) e um valor pago em dinheiro (`amount_paid`), calcule e imprima o troco a devolver.

**Saída esperada (exemplo com `purchase_value=35.50`, `amount_paid=50`):**
```
14.5
```

---

## 02 — password-strength

Dada uma senha (`password`), classifique sua força: "Fraca" (menos de 6 caracteres), "Média" (entre 6 e 10 caracteres), "Forte" (mais de 10 caracteres). Se a senha tiver menos de 4 caracteres, ignore as outras faixas e classifique direto como "Muito fraca".

**Saída esperada (exemplo com `password="abc123456789"`):**
```
Força da senha: Forte
```

---

## 03 — movie-ticket-price

Dada a idade (`age`) e o dia da semana (`weekday`, como texto, ex: "quarta"), calcule o preço do ingresso: R$20 normalmente, com desconto de 50% para menores de 12 ou maiores de 60, e desconto adicional de R$5 se for quarta-feira (os descontos podem se acumular).

**Saída esperada (exemplo com `age=65`, `weekday="quarta"`):**
```
Preço do ingresso: R$5.00
```

---

## 04 — bmi-and-age-report

Dados peso (`weight`), altura (`height`) e idade (`age`), calcule o IMC e gere um relatório combinando a classificação do IMC com a faixa etária da pessoa em uma única frase.

**Saída esperada (exemplo com `weight=68`, `height=1.70`, `age=30`):**
```
Adulto com IMC 23.53 (Normal).
```

---

## 05 — restaurant-bill-split

Dado o valor total da conta (`total_bill`), o número de pessoas (`num_people`) e se o serviço foi "bom" ou "ruim" (`service_quality`), calcule o valor por pessoa incluindo 10% de gorjeta se o serviço foi bom, ou sem gorjeta se foi ruim.

**Saída esperada (exemplo com `total_bill=200`, `num_people=4`, `service_quality="bom"`):**
```
Valor por pessoa: R$55.00
```

---

## 06 — shipping-and-tax

Dado o valor de um produto (`product_value`) e o estado de destino (`state`, como texto), calcule o valor final somando frete (grátis acima de R$300, senão R$20) e um imposto extra de 5% apenas se o estado for "SP".

**Saída esperada (exemplo com `product_value=250`, `state="SP"`):**
```
Valor final: R$282.50
```

---

## 07 — triangle-full-check

Dados três lados (`side_a`, `side_b`, `side_c`), verifique primeiro se formam um triângulo válido; se formarem, classifique o tipo (Equilátero, Isósceles ou Escaleno); se não formarem, informe qual combinação de lados violou a regra do triângulo.

**Saída esperada (exemplo com `side_a=4`, `side_b=4`, `side_c=4`):**
```
Triângulo Equilátero.
```

---

## 08 — loan-simulation

Dados renda mensal (`monthly_income`), valor solicitado (`loan_amount`) e se o cliente é "novo" ou "antigo" (`client_type`), decida a aprovação: clientes antigos precisam de renda >= valor/15; clientes novos precisam de renda >= valor/8 (critério mais rigoroso).

**Saída esperada (exemplo com `monthly_income=2000`, `loan_amount=20000`, `client_type="antigo"`):**
```
Empréstimo aprovado.
```

---

## 09 — grade-final-report

Dadas três notas (`grade1`, `grade2`, `grade3`) e a frequência (`attendance`), calcule a média das notas, aplique a regra de reprovação por falta (frequência < 75%) com prioridade sobre a nota, e classifique o resultado final em conceito (A/B/C/D) apenas se aprovado.

**Saída esperada (exemplo com `grade1=8`, `grade2=9`, `grade3=7`, `attendance=90`):**
```
Média: 8.0
Conceito: A
```

---

## 10 — smart-discount-cart

Dado o valor total do carrinho (`cart_total`), se o cliente é membro (`is_member`, "sim"/"não") e a forma de pagamento (`payment_method`, "pix" ou "cartão"), calcule o valor final aplicando em sequência: desconto de 10% para membros com carrinho acima de R$150, e desconto adicional de 5% para pagamento via Pix — mas o desconto do Pix só se aplica se o valor já tiver algum desconto de membro aplicado.

**Saída esperada (exemplo com `cart_total=400`, `is_member="sim"`, `payment_method="pix"`):**
```
Valor final: R$342.00
```

---

## Observações

- Os desafios seguem a mesma lógica dos exercícios principais, mas combinam mais de uma condição ou etapa de cálculo em um único problema.
- Nenhuma sintaxe nova aparece aqui — tudo usa `if`/`elif`/`else`, `and`/`or` e `if` aninhado, já vistos na [lista principal de exercícios](../README.md).