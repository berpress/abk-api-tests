import cattr
from requests import Response


class Validator:
    def structure(self, response, type_response) -> Response:
        if type_response:
            try:
                response.data = cattr.structure(response.json(), type_response)
            except Exception as e:
                raise e
        return response
