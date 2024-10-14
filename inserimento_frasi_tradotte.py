import re

# Definisci i nomi dei file di input e output
input_file = 'scheletro_RESTO_piurighe_serializzato.txt'        # File contenente i numeri
index_file = 'estratte_da_tradurre_solo_piu_righe_p2_senzatrattini.txt'        # File contenente le righe da sostituire
output_file = 'tradotto_RESTO_piurighe.txt'      # File dove scrivere il risultato

# Leggi le righe dal file di indice
with open(index_file, 'r', encoding='utf-8') as f:
    index_lines = f.readlines()

# Rimuovi eventuali spazi bianchi dalle righe
index_lines = [line.rstrip() for line in index_lines]

# Apri il file di input e leggi tutto il contenuto
with open(input_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Funzione per sostituire i numeri con le righe dall'indice
def replace_with_index(match):
    line_number = int(match.group(0))  # Ottieni il numero dalla regex
    if line_number - 1 < len(index_lines):
        # Restituisci la riga corrispondente con ritorno a capo
        return index_lines[line_number - 1].rstrip('\n') + '\n'  
    return match.group(0) + '\n'  # Restituisci il numero con ritorno a capo se non c'è una riga corrispondente

# Usa re.sub per sostituire i numeri con le righe dall'indice
new_content = re.sub(r'^\d+\r?\n', replace_with_index, content, flags=re.MULTILINE)

# Scrivi il nuovo contenuto nel file di output
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Sostituzioni completate.')
