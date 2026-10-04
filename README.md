# Customer Configuration Management Portal

Level: 16 — FDE / Customer Engineering

Skills: Python, four-eyes on prod config

Pass when env is not prod or approver != requester.

```bash
pip install -r requirements.txt
pytest -q
```

This is a local laptop proof. It does not call a hosted model and it does not apply production changes.
