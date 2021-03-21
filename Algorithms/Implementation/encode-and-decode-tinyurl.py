# question link: https://leetcode.com/problems/encode-and-decode-tinyurl/

class Codec:
    def __init__(self):
        self.map = {}
        self.reverse_map = {}
        self.cnt = 0
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.reverse_map[self.cnt] = longUrl
        self.cnt += 1
        
        return 'http://tinyurl.com/' + str(self.cnt - 1)

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        url = shortUrl.split('/')[-1]
        idx = int(url)
        
        return self.reverse_map[idx]
