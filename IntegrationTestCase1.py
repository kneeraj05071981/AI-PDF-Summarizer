"""Test the interaction between the PDF handler, GenAI model, and API endpoints."""
import requests

def test_generate_summary():
    files = {'file': open('test.pdf', 'rb')}
    response = requests.post('http://localhost:8000/summarize', files=files)
    assert response.status_code == 200
    assert 'summary' in response.json()
    assert len(response.json()['summary']) > 0
