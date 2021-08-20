from elabodeal.api.endpoints import Endpoint
from elabodeal.api.repositories import (
    UserRepository,
    PublisherRepository
)
from elabodeal.api.interactors import (
    CreatePublisherInteractor,
    FollowPublisherInteractor,
    UnFollowPublisherInteractor
)
from elabodeal.api.serializers import (
    CreatePublisherRequestSerializer,
    FollowPublisherRequestSerializer
)


class CreatePublisherEndpoint(Endpoint):
    auth_required = True

    def post(self, request):
        serialized_request = CreatePublisherRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        user = request.user

        user_repo = UserRepository()
        publisher_repo = PublisherRepository()

        interactor = CreatePublisherInteractor(
            user_repo=user_repo,
            publisher_repo=publisher_repo
        )
        interactor.execute(
            user,
            **serialized_request.validated_data
        )

        return self.respond(status=201)


class FollowersEndpoint(Endpoint):
    auth_required = True

    def post(self, request):
        serialized_request = FollowPublisherRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        user = request.user

        user_repo = UserRepository()
        publisher_repo = PublisherRepository()

        interactor = FollowPublisherInteractor(
            user_repo=user_repo,
            publisher_repo=publisher_repo
        )
        interactor.execute(user, **serialized_request.validated_data)

        return self.respond(status=200)

    def delete(self, request):
        serialized_request = FollowPublisherRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        user = request.user

        user_repo = UserRepository()
        publisher_repo = PublisherRepository()

        interactor = UnFollowPublisherInteractor(
            user_repo=user_repo,
            publisher_repo=publisher_repo
        )
        interactor.execute(user, **serialized_request.validated_data)

        return self.respond(status=200)