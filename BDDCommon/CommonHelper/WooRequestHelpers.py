
from woocommerce import API
class WooRequestHelper():
    
    def __init__(self) -> None:
        
        self.wcapi = API(
            url="http://localhost:10004",
            consumer_key="ck_f1767b58c6e0c65aeab891a9a70fddef4db345fd",
            consumer_secret="cs_255ae9296b2d082df8bd9b5027dda7b32788ef09",
            version="wc/v3"
        )
    
    def assert_status_code(self):

        assert self.rs.status_code == self.expected_status_code, f"Bad status code. Endpoint {self.wc_endpoint}, params {self.params},\
            Actual status is {self.rs.status_code}, and expected status is {self.expected_status_code}"

    def get(self, wc_endpoint, params = None, expected_status_code=200):

        self.rs = self.wcapi.get(wc_endpoint, params = params,)
        self.wc_endpoint = wc_endpoint
        self.expected_status_code = expected_status_code
        self.params = params
        self.assert_status_code() 

    def post(self):
        pass

    def delete(self):
        pass

    def put(self):
        pass


if __name__ == '__main__':
    myobject = WooRequestHelper()
    myobject.get("products")