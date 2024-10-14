import re

# Definisci i nomi dei file di input e output
input_file = 'scheletro_RESTO_piurighe.txt'
output_file = 'scheletro_RESTO_piurighe_serializzato.txt'

# Apri il file di input e leggi tutto il contenuto
with open(input_file, 'r', encoding='utf-8') as file:
    content = file.read()
    #print(repr(content))  # Debug: stampa il contenuto

# Conta il numero di occorrenze di '-\r\n'
occurrences = len(re.findall(r'-\n', content))
print(f'Occorrenze trovate di "-\n": {occurrences}')

# Funzione per sostituire righe che terminano con '-\r\n' con numeri incrementali
def replace_with_numbers(match):
    global counter
    replacement = str(counter) + '\n'  # Mantieni \r\n dopo il numero
    counter += 1
    return replacement

# Inizializza il contatore
counter = 1

# Usa re.sub per sostituire le righe che terminano con '-\r\n' con numeri incrementali
new_content = re.sub(r'-\n', replace_with_numbers, content)

# Scrivi il nuovo contenuto nel file di output
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(new_content)

print(f'Sostituite {counter - 1} occorrenze.')
