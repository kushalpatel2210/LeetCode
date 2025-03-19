class Codec:
    def __init__(self):
        self.urlMap = {}
        self.id = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.urlMap[self.id] = longUrl
        shortUrl = f'http://tinyurl.com/{self.id}'
        self.id += 1
        return shortUrl
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        urlId = int(shortUrl.split('/')[-1])
        return self.urlMap[urlId]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))