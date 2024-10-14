import re

# Definisci il percorso del tuo file di input e di output
input_file_path = 'tradotto_p1_RESTO_piurighe.txt'
output_file_path = 'scheletro_RESTO_piurighe.txt'

# Espressioni regolari per le righe da escludere e da cercare
exclude_pattern = re.compile(r'<it-IT>.*</it-IT>')        # Occorrenze su una sola riga
include_pattern = re.compile(r'<it-IT>([\s\S]*?)<\/it-IT>')  # Occorrenze su più righe

# Funzione per controllare se una riga deve essere esclusa
def should_exclude(line):
    return exclude_pattern.search(line)

# Leggi il contenuto del file
with open(input_file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Flag per sapere se ci troviamo all'interno di un blocco <it-IT> su più righe
inside_block = False

# Modifica il contenuto delle righe
for i in range(len(lines)):
    # Se la riga contiene il pattern su una singola riga, la saltiamo
    if should_exclude(lines[i]):
        continue

    # Cerca l'inizio di un blocco <it-IT>
    if '<it-IT>' in lines[i] and not '</it-IT>' in lines[i]:
        inside_block = True  # Inizia il blocco
        lines[i] = '-\n'  # Sostituisci l'inizio del blocco con '-'
    elif '</it-IT>' in lines[i] and inside_block:
        inside_block = False  # Fine del blocco
        lines[i] = '-\n'  # Sostituisci la fine del blocco con '-'
    elif inside_block:
        # Se siamo dentro il blocco, sostituiamo anche queste righe
        lines[i] = '-\n'

# Scrivi il risultato in un nuovo file
with open(output_file_path, 'w', encoding='utf-8') as file:
    file.writelines(lines)

print("Modifica completata! File salvato come:", output_file_path)

