class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if body.get("env") == "prod" and body.get("approver") == body.get("requester"): failed.append("four_eyes")
    return {"passed": not failed, "failed": failed, "applied": False}
