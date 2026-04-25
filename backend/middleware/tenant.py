def get_org_from_request(request):
    return request.headers.get("X-ORG-ID")
