import os

# ElasticSearch
ELASTIC_HOST = os.environ.get("ELASTIC_HOST", "elasticsearch")
ELASTIC_PORT = os.environ.get("ELASTIC_PORT", 9200)
