from elasticsearch import Elasticsearch
from app.config import ELASTIC_PORT, ELASTIC_HOST

es = Elasticsearch([f'http://{ELASTIC_HOST}:{ELASTIC_PORT}'], ca_certs=False, verify_certs=False)

settings= {"settings": {
    "index": {
      "max_ngram_diff": 10
    },
    "analysis": {
      "analyzer": {
        "my_analyzer": {
          "tokenizer": "my_tokenizer",
          "filter" : ["lowercase"]
        }
      },
      "tokenizer": {
        "my_tokenizer": {
          "type": "ngram",
          "min_gram": 3,
          "max_gram": 10,
          "token_chars": [
            "letter",
            "digit"
          ],
        }
      }
    }
  }}
mapping_lesson= {
"mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "my_analyzer"
      },
      "tags": {
        "type": "text",
        "analyzer": "my_analyzer"
      }
    }
  }
}
mapping_post = {
"mappings": {
    "properties": {
      "title": {
        "type": "text",
        "analyzer": "my_analyzer"
      },
      "tags": {
        "type": "text",
        "analyzer": "my_analyzer"
      }
    }
  }
}
mapping_user={
  "mappings": {
    "properties": {
      "username": {
        "type": "text",
        "analyzer": "my_analyzer"
      },
    }
  }
}
mapping = {
  "settings":settings['settings'],
  "mappings":mapping_post['mappings']
}
mapping_lesson = {
  "settings": settings['settings'],
  "mappings": mapping_lesson['mappings']
}
mapping_user = {
  "settings": settings['settings'],
  "mappings": mapping_user['mappings']
}


def creating_indexes():
  if not es.indices.exists(index='posts'):
    es.indices.create(index='posts', body=mapping)
  if not es.indices.exists(index='users'):
    es.indices.create(index='users', body=mapping_user)
  if not es.indices.exists(index='achievements'):
    es.indices.create(index='achievements', body=mapping)
  if not es.indices.exists(index='categories'):
    es.indices.create(index='categories', body=mapping)
  if not es.indices.exists(index='courses'):
    es.indices.create(index='courses', body=mapping)
  if not es.indices.exists(index='lessons'):
    es.indices.create(index='lessons', body=mapping_lesson)


creating_indexes()
