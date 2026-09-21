from hospital_core.patients import normalize_document

def test_normalize_document():
    assert normalize_document(" 123-456 ") == "123456"
