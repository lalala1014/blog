from haystack import indexes
from blog.models import text
class textIndex(indexes.SearchIndex, indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)
    def get_model(self):
        return text
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
