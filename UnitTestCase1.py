import pytest
from your_microservice import pdf_handler

def test_pdf_handler_valid_pdf():
    pdf_content = b'%PDF-1.4 valid pdf content'
    result = pdf_handler.extract_text(pdf_content)
    assert isinstance(result, str)
    assert len(result) > 0

def test_pdf_handler_invalid_file():
    with pytest.raises(ValueError):
        pdf_handler.extract_text(b'invalid content')
