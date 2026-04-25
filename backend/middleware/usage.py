from usage.tracker import track

def usage_middleware(request, call_next):
    org_id = request.headers.get("X-ORG-ID")
    if org_id:
        track(org_id, "request")

    return call_next(request)
