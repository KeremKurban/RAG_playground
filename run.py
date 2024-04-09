from elasticsearch import Elasticsearch

# Connect to the Elasticsearch cluster
es = Elasticsearch("http://localhost:9201")

query = {
  "query": {
    "match": {
      "text": "what is the role of calcium in network activity?"
    }
  }
}

response = es.search(index="test_paragraphs", body=query)

for hit in response['hits']['hits']:
    print(f'SCORE: {hit["_score"]}')
    print(f'ARTICLE: {hit["_source"]["title"]} ({hit["_source"]["doi"]})')
    print(f'SECTION: {hit["_source"]["section"]}')
    print()
    print(hit['_source']['text'])
    print('====')