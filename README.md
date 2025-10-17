# 🧩 afnd-para-afd-conversor

## 📁 Organização do Repositório

### Estrutura de Pastas

```
├── src/         # Código-fonte
├── data/        # Arquivos de entrada (AFND e palavras de teste)
├── out/         # Arquivos gerados (AFD convertido e resultados do GraphViz para fazer a exibição do grafo do AFND e do AFD)
└── diagrams/    # Imagens geradas
```

---

## Como Rodar

### 1️⃣ Gerar AFD a partir do AFND (Parte 1)

```bash
python3 src/parte1.py
```

> 💡 Gera o arquivo: `out/afd_saida.txt`

---

### 2️⃣ Converter e Processar Palavras (Parte 2)

```bash
python3 src/parte2.py
```

> 💡 Gera os arquivos:
>
> * `out/afd_saida.txt`
> * `out/resultado_palavras.txt`

---

## ⚙️ Observações
* Os scripts utilizam **caminhos relativos**, então devem ser executados **a partir do diretório raiz** do projeto.
---

## 📚 Parte 1: Conversão de AFND → AFD

### Objetivo

Converter um **AFND (com movimentos vazios)** em um **AFD**.

* **Alfabeto:** `{0, 1}`
* **Entrada:** arquivo com a tabela do AFND

---

### 🗂️ Formato do Arquivo de Entrada

| Linha | Descrição                                                | Exemplo           |
| :---- | :------------------------------------------------------- | :---------------- |
| 0     | Sequência de estados separados por espaço                | `A B C D E F`     |
| 1     | Estado inicial                                           | `A`               |
| 2     | Estados finais separados por espaço                      | `E F`             |
| 3+    | Transições: estado atual, caractere lido, próximo estado | `A 0 B` / `A h C` |

> ℹ️ A **transição vazia** deve ser representada por **`h`**.

---

### 📄 Exemplo de Arquivo de Entrada

<img width="351" height="324" alt="image" src="https://github.com/user-attachments/assets/d1898f70-39ae-4029-ab3e-e2de305f47ff" />

---

## 🎯 Resultado Esperado

### 📤 Saída

Um arquivo `.txt` (mesmo formato do de entrada) contendo a **tabela do AFD**.

<img width="351" height="415" alt="image" src="https://github.com/user-attachments/assets/3930d5bd-a9c7-4ce6-b674-79a9f52fbb27" />

---

## 📊 Visualização dos Autômatos

### 🔹 AFND

<img width="691" height="232" alt="image" src="https://github.com/user-attachments/assets/4b07bbac-2991-4d75-a911-0a0915ea27ef" />

### 🔹 AFD

<img width="917" height="384" alt="image" src="https://github.com/user-attachments/assets/f0ea9ccd-819e-4c6c-886a-92c44b6f3813" />

---

## 🧮 Visualização no JFLAP

### 🔸 AFND

<img width="648" height="415" alt="image" src="https://github.com/user-attachments/assets/e54cbb96-9835-4342-99dd-6b124c05bcab" />

### 🔸 AFD

<img width="616" height="440" alt="image" src="https://github.com/user-attachments/assets/d60ea7ab-ea02-4883-8944-919b09f3a746" />

