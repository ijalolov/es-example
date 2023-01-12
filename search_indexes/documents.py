# Name of the Elasticsearch index
from django.conf import settings
from django_elasticsearch_dsl import Index, Document, fields
from elasticsearch_dsl import analyzer

from books.models import Book

INDEX = Index(settings.ELASTICSEARCH_INDEX_NAMES['books'])

# See Elasticsearch Indices API reference for available settings
INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

html_strip = None


@INDEX.doc_type
class BookDocument(Document):
    """Book Elasticsearch document."""

    id = fields.IntegerField()

    title = fields.TextField()

    description = fields.TextField()

    summary = fields.TextField()

    # publisher = fields.TextField()

    publication_date = fields.DateField()

    state = fields.TextField()

    isbn = fields.TextField()

    price = fields.FloatField()

    pages = fields.IntegerField()

    stock_count = fields.IntegerField()

    tags = fields.TextField(
        attr='tags_indexing',
        fields={
            'raw': fields.TextField(multi=True),
            'suggest': fields.TextField(multi=True),
        },
        multi=True
    )

    class Django(object):
        """Inner nested class Django."""

        model = Book  # The model associate with this Document
