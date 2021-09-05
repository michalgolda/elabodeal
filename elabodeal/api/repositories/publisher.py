from elabodeal.models import Publisher
from elabodeal.api.repositories import Repository


class PublisherRepository(Repository):
    def add(self, *args, **kwargs):
        return Publisher.objects.create(*args, **kwargs)

    def get_all_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).all()

    def get_one_by(self, *args, **kwargs):
        return self._query_filter(*args, **kwargs).first()

    def delete_by(self, *args, **kwargs):
        return any(self._query_filter(*args, **kwargs).delete())

    def save(self, publisher):
        publisher.save()

        return publisher
    
    def _query_filter(self, *args, **kwargs):
        return Publisher.objects.filter(*args, **kwargs)