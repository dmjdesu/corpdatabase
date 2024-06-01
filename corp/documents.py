from elasticsearch_dsl import Document, Text, connections
from django.conf import settings

# Elasticsearchの接続設定を取得
es_hosts = settings.ELASTICSEARCH_DSL['default']['hosts']
connections.create_connection(hosts=[es_hosts])

class CompanyDocument(Document):
    name = Text()
    description = Text()
    industry = Text()

    class Index:
        name = 'companies'

    def save(self, **kwargs):
        return super().save(**kwargs)
