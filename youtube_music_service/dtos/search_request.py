class SearchRequest:
    def __init__(self, query):
        self.query = query

    @classmethod
    def from_dict(cls, data):
        return cls(
            query=data.get('query')
        )
