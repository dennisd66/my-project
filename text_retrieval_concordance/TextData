from collections import namedtuple, defaultdict

class TextData:
    WordData = namedtuple('WordData', ['word', 'index', 'metadata'])

    def __init__(self, tokens, metadata_list):
        self.data = []
        self.concordance_index = defaultdict(list)
        for idx, token in enumerate(tokens):
            metadata = metadata_list[idx] if idx < len(metadata_list) else {}
            word_data = TextData.WordData(token, idx, metadata)
            self.data.append(word_data)
            self.concordance_index[token.lower()].append(word_data)

    def search(self, query):
        return [wd for wd in self.data if wd.word == query]

    def filter_search_results(self, results, criteria):
        filtered_results = []

        for word_data in results:
            match = True

            for key, value in criteria.items():
                if key not in word_data.metadata or word_data.metadata[key] != value:
                    match = False
                    break

            if match:
                filtered_results.append(word_data)

        return filtered_results

    def present_concordance(self):
        sorted_index = sorted(self.concordance_index.items(), key=lambda x: x[0])
        for word, word_data_list in sorted_index:
            print(f"{word}:")
            for wd in word_data_list:
                print(f"  - Index: {wd.index}, Metadata: {wd.metadata}")


# Here's an example of how to use the TextData class:
#   tokens = ['this', 'is', 'an', 'example', 'text', 'for', 'tokenization', 'let', 's', 'see', 'how', 'it', 'works']
#   metadata_list = [
#       {"sentence_number": 1}, {"sentence_number": 1}, {"sentence_number": 1},
#       {"sentence_number": 1}, {"sentence_number": 1}, {"sentence_number": 1},
#       {"sentence_number": 1}, {"sentence_number": 2}, {"sentence_number": 2},
#       {"sentence_number": 2}, {"sentence_number": 2}, {"sentence_number": 2},
#       {"sentence_number": 2}
#   ]
#   text_data = TextData(tokens, metadata_list)
#
# Search for a word
#   query = "example"
#   search_results = text_data.search(query)
#   print(f"Search results for '{query}': {search_results}")
#
# Filter search results based on metadata
#   criteria = {"sentence_number": 2}
#   filtered_results = text_data.filter_search_results(search_results, criteria)
#   print(f"Filtered results based on criteria {criteria}: {filtered_results}")