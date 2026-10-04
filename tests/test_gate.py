from fastapi.testclient import TestClient
from cconfig.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'env': 'prod', 'requester': 'ada', 'approver': 'grace'}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'env': 'prod', 'requester': 'ada', 'approver': 'ada'}).json()
    assert bad["passed"] is False
    assert "four_eyes" in bad["failed"]
