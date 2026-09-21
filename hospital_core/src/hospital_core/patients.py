def normalize_document(document: str) -> str:
    value = document.strip().replace("-", "")
    if len(value) < 5:
        raise ValueError("Documento inválido")
    return value
