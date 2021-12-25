class CorsHeaders:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.headers["Access-Control-Allow-Origin"] = ["https://cineacca.com", "https://storage.googleapis.com/cineacca_bucket"]
        response.headers["Access-Control-Allow-Methods"] = ["GET", "PUT", "DELETE", "OPTION"]
        response.headers["Cross-Origin-Resource-Policy"] = "cross-origin" 
        response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
        response.headers["Cross-Origin-Opener-Policy"] = "same-origin" 
        return response