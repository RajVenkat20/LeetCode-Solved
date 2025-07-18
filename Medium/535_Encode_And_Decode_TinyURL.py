class Codec:
    def __init__(self):
        self.map = {}

    def encode(self, longUrl: str) -> str:
        code = hash(longUrl)
        self.map[code] = longUrl
        return f"http://tinyurl.com/{code}"
        

    def decode(self, shortUrl: str) -> str:
        code = int(shortUrl.replace("http://tinyurl.com/", ""))
        return self.map[code]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))