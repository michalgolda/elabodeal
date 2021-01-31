from elabodeal.models import Publisher
from elabodeal.api.repositories import Repository


class PublisherRepository(Repository):
    def get(self, id: int) -> Publisher:
        return Publisher.objects.filter(id=id).first()

    def delete(self, publisher: Publisher) -> None:
        publisher.delete()

    def save(self, publisher: Publisher) -> Publisher:
        publisher.save()

        return publisher