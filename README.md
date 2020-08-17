
# Desafio técnio para Data Science - Parafa, básico


## Contexto

Este desafio envolve um chat de suporte técnico de empresa de telecomunicações.

Neste chat, há um sistema de Natural Language Processing que classifica as mensagens do usuário em uma série de INTENÇÕES, para agilizar o atendimento.

Por exemplo, aqui temos algumas mensagens de usuário e a clasfificação de intenção esperada:

| Texto              |  Intenção            | 
| ------------------ | -------------------- |
| sim                | RESPOSTA VERDADEIRA  |
| eu quero           | RESPOSTA VERDADEIRA  |
| falar atendente    | TRANSFERE HUMANO     |
| sem sinal          | TECNICO SINAL        |


## O desafio

Neste desafio, você **já possui** um relatório das intenções que o sistema determinou, devendo somente responder as perguntas abaixo sobre este relatório.

O relatório é um arquivo .CSV com duas colunas:

- **Intenções Classificadas/Recebidas:** as intenções que o sistema determinou;
- **Intenções Reais/Esperadas:** as intenções corretas - ou seja, as que o sistema deveria ter determinado.

Cada exercício deve ser respondido criando um arquivo Python que terá o código pedido e imprimirá as respostas desejadas. Se desejar, inclua comentários explicando seu raciocínio ou dificuldades. Há um arquivo de exemplo como referência.

Desde que realize o pedido, você tem liberdade para implementar da forma que preferir.

A entrega deve ser feita através de um fork deste repositório no Github.

### 1. Quantas intenções são cobertas por este classificador - ou seja, quantas intenções únicas o classificador conhece? 

Use Python para determinar o que é pedido; e imprima o número de intenções únicas, seguido de uma lista com cada intenção única.

### 2. Qual a acurácia deste classificador?

Use Python para determinar a acurácia (accuracy) e a imprima.

### 3. Qual das intenções foi classificada com maior precisão? E qual foi classificada com menor precisão?

Use Python para determinar ambas, e as imprima nesta ordem.

### 4. Frequentemente, é possível melhorar um classificador agrupando as intenções menos assertivas em uma só. Tendo em mente as intenções determinadas vs. as desejadas, quais intenções você agruparia?

Por exemplo, se frequentemente as intenções FALTA SINAL e APARELHO QUEIMADO são confundidas, faz sentido as agrupar em uma só.

Use Python para determinar uma matriz de confusão, e baseado nela imprima as intenções que você considera boas candidatas para agrupamento.