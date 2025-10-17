Organização do repositório

Pasta structure:
- src/: código-fonte (scripts reorganizados)
- data/: arquivos de entrada (AFND, palavras de teste)
- out/: arquivos gerados (AFD convertido, resultados)
- diagrams/: arquivos .dot e imagens das automações

Como rodar

1) Gerar AFD a partir do AFND (Parte 1):
   python3 src/parte1.py
   (gera o arquivo em out/afd_saida.txt)

2) Converter e processar palavras (Parte 2):
   python3 src/parte2.py
   (gera out/afd_saida.txt e out/resultado_palavras.txt)

Observações
- Os scripts usam caminhos relativos esperando que você rode a partir do diretório raiz do projeto.
- Arquivos originais foram copiados para as novas pastas; se quiser, remova os duplicados manualmente.


# afnd-para-afd-conversor
### Parte 1: Converter um AFND (com movimentos vazios) em um AFD.
#### Alfabeto: {0,1}
#### Entrada: um arquivo com a tabela do AFND.
#### Formato do arquivo de entrada:
#### Linha 0: a sequência de estados separados por espaço. EX: A B C D E F
#### Linha 1: estado inicial
#### Linha 2: estados finais separados por espaço ( se houver mais de um estado final)
#### Linha 3 em diante: estado atual, espaço, caractere lido, espaço, próximo estado
#### Obs: respresentar a transição vazia por h.

#### Arquivo de entrada utilizado:
<img width="351" height="324" alt="image" src="https://github.com/user-attachments/assets/d1898f70-39ae-4029-ab3e-e2de305f47ff" />

## Resultado esperado:
#### Saída: um arquivo .txt (mesmo formato do arquivo de entrada) com a tabela do AFD
<img width="351" height="415" alt="image" src="https://github.com/user-attachments/assets/3930d5bd-a9c7-4ce6-b674-79a9f52fbb27" />

#### Usar o GraphViz para fazer a exibição do grafo do AFND e do AFD.
AFND:
<img width="691" height="232" alt="image" src="https://github.com/user-attachments/assets/4b07bbac-2991-4d75-a911-0a0915ea27ef" />


AFD:
<img width="917" height="384" alt="image" src="https://github.com/user-attachments/assets/f0ea9ccd-819e-4c6c-886a-92c44b6f3813" />

#### Usar o JFLAP e desenhar os dois autômatos: o de entrada e o de saída.

AFND:
<img width="648" height="415" alt="image" src="https://github.com/user-attachments/assets/e54cbb96-9835-4342-99dd-6b124c05bcab" />

AFD:
<img width="616" height="440" alt="image" src="https://github.com/user-attachments/assets/d60ea7ab-ea02-4883-8944-919b09f3a746" />

