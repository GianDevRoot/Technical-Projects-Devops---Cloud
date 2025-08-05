from app import app

def test_homepage():
    """
    Verifica que la ruta raíz devuelva el texto esperado.
    """
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"Hola Mundo" in response.data
