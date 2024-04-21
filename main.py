results = []

def cky_parse(sentence, grammar):
    # Inicialización de la tabla
    n = len(sentence)
    table = [[set() for _ in range(n+1)] for _ in range(n)]
    
    # Paso de inicialización
    for i in range(1, n+1):
        for non_terminal, productions in grammar.items():
            if sentence[i-1] in productions:
                table[i-1][i].add(non_terminal)
    
    # Paso de completación
    for span in range(2, n+1):
        for begin in range(n-span+1):
            end = begin + span
            for split in range(begin+1, end):
                for non_terminal, productions in grammar.items():
                    for production in productions:
                        if len(production) == 2 and production[0] in table[begin][split] and production[1] in table[split][end]:
                            table[begin][end].add(non_terminal)
    
    # Paso de reconocimiento
    if 'S' in table[0][n]:
        return True, table
    else:
        return False, table

def read_grammar(k):
    G = {}
    for _ in range(k):
        l = input().split()
        G[l[0]] = []
        for i in range(1, len(l)):
            G[l[0]].append(l[i])
    return G

def main():
    cases = int(input())
    for _ in range(cases):
        nG, m = list(map(int, input().split()))
        grammar = read_grammar(nG)
        strings_to_test = [input() for _ in range(m)]

        for string in strings_to_test:
            parsed, _ = cky_parse(list(string), grammar)
            if parsed:
                results.append("yes")
                # print("yes")
            else:
                results.append("no")
                # print("no")

main()
for result in results:
	print(result)