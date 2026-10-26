# 📘 Atividade: Jogo da Forca

## 🎯 Objetivo

Desenvolva um jogo da Forca em Python para praticar manipulação de strings, estruturas de repetição, condicionais e seleção aleatória. Ao final, o programa deverá permitir que o jogador descubra uma palavra antes de esgotar as tentativas.

## 📝 Tarefas

### 🛠️ Preparar a partida e exibir o progresso

#### Descrição

Use a lista de palavras do código inicial para sortear a palavra secreta e mostrar ao jogador quais letras já foram descobertas.

#### Requisitos

O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida.
- Representar cada letra ainda não descoberta por `_` e atualizar a exibição após cada palpite correto.
- Solicitar um palpite de uma letra por vez.

### 🛠️ Controlar as tentativas e encerrar o jogo

#### Descrição

Implemente o fluxo das tentativas, atualizando o estado da partida até que o jogador descubra a palavra ou não tenha mais tentativas disponíveis.

#### Requisitos

O programa concluído deve:

- Reduzir o número de tentativas restantes quando o palpite não estiver na palavra.
- Continuar a partida enquanto houver letras a descobrir e tentativas disponíveis.
- Encerrar a partida quando a palavra for descoberta ou as tentativas incorretas se esgotarem.
- Exibir uma mensagem indicando vitória ou derrota; em caso de derrota, revelar a palavra secreta.
