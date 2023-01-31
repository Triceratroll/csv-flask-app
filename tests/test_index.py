from tests.conftest import client
from pathlib import Path

# get the resources folder in the tests folder
resources = Path(__file__).parent / "resources"

def test_request_example(client):
    response = client.get("/")
    assert b"<h1>Reporting Tool</h1>" in response.data 


def test_request_report_1(client):
    response = client.post("/upload_report_1", data={
        "files": [(resources / "products.csv").open("rb"),
                    (resources / "orders.csv").open("rb")]
        
    }, follow_redirects=True)
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the index page.
    assert response.request.path == "/download/order_prices.csv"
    assert response.status_code == 200

def test_request_report_2(client):
    response = client.post("/upload_report_2", data={
        "files": (resources / "orders.csv").open("rb"),
        
    }, follow_redirects=True)
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the index page.
    assert response.request.path == "/download/product_customers.csv"
    assert response.status_code == 200

def test_request_report_3(client):
    response = client.post("/upload_report_3", data={
        "files": [(resources / "orders.csv").open("rb"),
                   (resources / "products.csv").open("rb"),
                    (resources / "customers.csv").open("rb")]
        
    }, follow_redirects=True)
    # Check that there was one redirect response.
    assert len(response.history) == 1
    # Check that the second request was to the index page.
    assert response.request.path == "/download/customer_ranking.csv"
    assert response.status_code == 200