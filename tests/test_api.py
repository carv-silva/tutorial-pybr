from fastapi.testclient import TestClient
from http import HTTPStatus
from api_pedidos.api import app
import pytest

@pytest.fixture
def cliente():
    return TestClient(app)


def test_integridade_status_200(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.status_code == HTTPStatus.OK


def test_verifica_integridade_retorno_json(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.headers["Content-Type"] == "application/json"
    #print(type(resposta))

def test_verifica_integridade_informacoes(cliente):
    resposta = cliente.get("/healthcheck")
    assert resposta.json() == {
        "status": "ok"
    }