import re

def extract_number(text: str) -> float:
    # Extrai um número de um texto
    # Suportando formatos como:
    # R$ 123,45
    # R$ 123.45
    # R$ 1.234,56

    if not isinstance(text, str):
        raise ValueError("Texto inválido para extração númerica.")
    
    cleaned = text.strip()
    cleaned = cleaned.replace("R$", "").replace("U$", "").replace("€", "").strip

    match = re.search(r"[-+]?\d[\d\.,]*", cleaned)
    if not match:
        raise ValueError(f"Nenhum número encontrado no texto: {text}")
    
    number_text = match.group(0)

    if "," in number_text and "." in number_text:
        number_text = number_text.replace(".", "").replace(",", ",")
    elif "," in number_text:
        number_text = number_text.replace(",", ".")

    return float(number_text)