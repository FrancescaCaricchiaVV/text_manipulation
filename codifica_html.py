import re
import html

# Funzione per codificare i caratteri speciali in HTML
def encode_html_special_chars(text):
    # Codifica il testo normalmente
    escaped_text = html.escape(text)
    # Ritorna le virgolette doppie alla loro forma originale, se codificate
    return escaped_text.replace("&quot;", '"').replace("&#x27;", "'")

# Funzione per codificare solo le porzioni racchiuse dai tag <en>...</en>, anche se su più righe
def encode_in_tags(content, tag="en"):
    # Espressione regolare per trovare i contenuti all'interno dei tag <en>...</en>, includendo i nuovi caratteri di riga
    pattern = re.compile(f'<{tag}>(.*?)</{tag}>', re.DOTALL)
    
    # Funzione per sostituire i contenuti tra i tag con la versione codificata
    def replace_with_encoded(match):
        encoded_content = encode_html_special_chars(match.group(1))
        return f'<{tag}>{encoded_content}</{tag}>'
    
    # Sostituisce tutte le occorrenze nel testo
    return re.sub(pattern, replace_with_encoded, content)

# Assegnazione diretta dei nomi dei file di input e output
input_file = "Web Policy ITA.txt"
output_file = "Web Policy ITA.xml"

# Leggere il file di input
with open(input_file, "r", encoding="utf-8") as file:
    content = file.read()

# Codificare le porzioni tra i tag <en>, comprese quelle su più righe
encoded_content = encode_in_tags(content)

# Scrivere il risultato in un file di output
with open(output_file, "w", encoding="utf-8") as file:
    file.write(encoded_content)

print("Codifica completata!")
