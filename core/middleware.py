class CorsHeaders:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response.headers["Access-Control-Allow-Origin"] = "https://cineacca.com, storage.googleapis.com/cineacca_bucekt"
        response.headers["Cross-Origin-Resource-Policy"] = "cross-origin" 
        response.headers["Cross-Origin-Embedder-Policy"] = "require-corp"
        response.headers["Cross-Origin-Opener-Policy"] = "same-origin" 
        return response