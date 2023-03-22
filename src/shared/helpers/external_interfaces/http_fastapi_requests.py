import json
from .http_models import HttpRequest, HttpResponse


class FastAPIHttpRequest(HttpRequest):
    body: any
    headers: dict
    query_params: dict
    
    def __init__(self, data: dict = None) -> None:

        super().__init__(
            body=data.get("headers", None),
            headers=data.get("query_params", None),
            query_params=data.get("body", None)
        )


class FastAPIHttpResponse(HttpResponse):
    status_code: int = 200
    body: any = {"message": "No response"}
    headers: dict = {"Content-Type": "application/json"}

    def __init__(self, body: any = None, status_code: int = None, headers: dict = None) -> None:
    
        _body = body or FastAPIHttpResponse.body
        _headers = headers or FastAPIHttpResponse.headers
        _status_code = status_code or FastAPIHttpResponse.status_code

        super().__init__(body=_body, headers=_headers, status_code=_status_code)
        
    def to_dict(self) -> dict:
        return {
            "status_code": self.status_code,
            "body": json.dumps(self.body),
            "headers": self.headers,
        }