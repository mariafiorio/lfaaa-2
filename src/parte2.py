from collections import deque, defaultdict

class AFND:
    def __init__(self):
        self.estados = set()
        self.alfabeto = set()
        self.transicoes = defaultdict(lambda: defaultdict(set))
        self.estado_inicial = ''
        self.estados_finais = set()
    
    def fecho_epsilon(self, estados):
        fecho = set(estados)
        pilha = list(estados)
        while pilha:
            estado = pilha.pop()
            for prox_estado in self.transicoes[estado].get('\u03b5', set()):
                if prox_estado not in fecho:
                    fecho.add(prox_estado)
                    pilha.append(prox_estado)
        return frozenset(fecho)
    
    def transicao_afd(self, conjunto_estados, simbolo):
        destinos = set()
        for estado in conjunto_estados:
            destinos.update(self.transicoes[estado].get(simbolo, set()))
        return self.fecho_epsilon(destinos)

class AFD:
    def __init__(self):
        self.estados = set()
        self.alfabeto = set()
        self.transicoes = defaultdict(lambda: defaultdict(str))  # destino único
        self.estado_inicial = ''
        self.estados_finais = set()
    
    def processar_palavra(self, palavra):
        estado_atual = self.estado_inicial
        for simbolo in palavra:
            if simbolo not in self.alfabeto:
                return False  # símbolo fora do alfabeto
            if estado_atual in self.transicoes and simbolo in self.transicoes[estado_atual]:
                estado_atual = self.transicoes[estado_atual][simbolo]
            else:
                return False  # transição não definida (AFD parcial)
        return estado_atual in self.estados_finais

def ler_afnd_arquivo(nome_arquivo):
    afnd = AFND()
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()
    
    if len(linhas) < 3:
        raise ValueError("Arquivo de entrada inválido: precisa de ao menos 3 linhas (estados, inicial, finais).")
    
    # Linha 0: estados
    afnd.estados = set(linhas[0].strip().split())
    # Linha 1: estado inicial
    afnd.estado_inicial = linhas[1].strip()
    # Linha 2: estados finais (pode estar vazia)
    afnd.estados_finais = set(linhas[2].strip().split()) if linhas[2].strip() else set()
    
    if afnd.estado_inicial not in afnd.estados:
        raise ValueError(f"Estado inicial '{afnd.estado_inicial}' não está na lista de estados.")
    if not afnd.estados_finais.issubset(afnd.estados):
        desconhecidos = afnd.estados_finais - afnd.estados
        raise ValueError(f"Estados finais desconhecidos: {', '.join(sorted(desconhecidos))}")
    
    # Linhas 3+: transições
    for linha in linhas[3:]:
        linha = linha.strip()
        if not linha:
            continue
        partes = linha.split()
        if len(partes) != 3:
            raise ValueError(f"Linha de transição inválida: '{linha}' (esperado: 'origem simbolo destino')")
        estado_atual, simbolo, proximo_estado = partes
        if estado_atual not in afnd.estados:
            raise ValueError(f"Estado de origem desconhecido: '{estado_atual}'")
        if proximo_estado not in afnd.estados:
            raise ValueError(f"Estado de destino desconhecido: '{proximo_estado}'")
        
        # Normaliza ε: aceita 'h', 'H' e 'ε'
        if simbolo.lower() == 'h' or simbolo == '\u03b5':
            simbolo_norm = '\u03b5'
        else:
            if simbolo not in {'0', '1'}:
                raise ValueError(f"Símbolo inválido '{simbolo}'. O alfabeto permitido é {{0,1}} e ε (h/H).")
            simbolo_norm = simbolo
        
        afnd.transicoes[estado_atual][simbolo_norm].add(proximo_estado)
    
    # Alfabeto conforme o enunciado
    afnd.alfabeto = {'0', '1'}
    return afnd

def converter_afnd_para_afd(afnd):
    afd = AFD()
    afd.alfabeto = set(afnd.alfabeto)  # {'0','1'}
    
    # ε-fecho do estado inicial
    estado_inicial_afd = afnd.fecho_epsilon({afnd.estado_inicial})
    
    # Mapeamento: conjunto de estados -> nome Qk
    mapeamento_estados = {}
    estados_nao_processados = deque()
    contador_estados = 0
    
    # Cria Q0 para o conjunto inicial e define como estado inicial do AFD
    nome_estado_inicial = f"Q{contador_estados}"
    mapeamento_estados[estado_inicial_afd] = nome_estado_inicial
    afd.estados.add(nome_estado_inicial)
    afd.estado_inicial = nome_estado_inicial
    estados_nao_processados.append(estado_inicial_afd)
    contador_estados += 1
    
    # BFS sobre conjuntos
    while estados_nao_processados:
        conjunto_atual = estados_nao_processados.popleft()
        nome_atual = mapeamento_estados[conjunto_atual]
        
        # Marca final se intersecta finais do AFND
        if conjunto_atual & afnd.estados_finais:
            afd.estados_finais.add(nome_atual)
        
        # Para cada símbolo do alfabeto
        for simbolo in afd.alfabeto:
            proximo_conjunto = afnd.transicao_afd(conjunto_atual, simbolo)
            if proximo_conjunto:
                if proximo_conjunto not in mapeamento_estados:
                    nome_proximo = f"Q{contador_estados}"
                    mapeamento_estados[proximo_conjunto] = nome_proximo
                    afd.estados.add(nome_proximo)
                    estados_nao_processados.append(proximo_conjunto)
                    contador_estados += 1
                nome_proximo = mapeamento_estados[proximo_conjunto]
                afd.transicoes[nome_atual][simbolo] = nome_proximo
    
    return afd

def salvar_afd_arquivo(afd, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        f.write(' '.join(sorted(afd.estados)) + '\n')
        f.write(afd.estado_inicial + '\n')
        f.write(' '.join(sorted(afd.estados_finais)) + '\n')
        for estado in sorted(afd.estados):
            for simbolo in sorted(afd.alfabeto):
                if simbolo in afd.transicoes[estado]:
                    prox_estado = afd.transicoes[estado][simbolo]
                    f.write(f"{estado} {simbolo} {prox_estado}\n")

def ler_palavras_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as f:
        return [linha.strip() for linha in f.readlines()]

def processar_palavras_afd(afd, palavras, nome_arquivo_saida):
    with open(nome_arquivo_saida, 'w', encoding='utf-8') as f:
        for palavra in palavras:
            aceita = afd.processar_palavra(palavra)
            f.write(f"{palavra} {'aceito' if aceita else 'não aceito'}\n")

if __name__ == "__main__":
    import os
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    entrada = os.path.join(base_dir, 'data', 'entrada_trab_01.txt')
    palavras_file = os.path.join(base_dir, 'data', 'palavras_teste.txt')
    saida_afd = os.path.join(base_dir, 'out', 'afd_saida.txt')
    saida_resultado = os.path.join(base_dir, 'out', 'resultado_palavras.txt')

    # Parte 1: Converter AFND-ε para AFD
    afnd = ler_afnd_arquivo(entrada)
    afd = converter_afnd_para_afd(afnd)
    salvar_afd_arquivo(afd, saida_afd)
    
    # Parte 2: Processar palavras
    palavras = ler_palavras_arquivo(palavras_file)
    processar_palavras_afd(afd, palavras, saida_resultado)
