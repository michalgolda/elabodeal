from elabodeal.api.endpoints import Endpoint
from elabodeal.api.repositories import (
    FileRepository,
    UserRepository,
    ProductRepository,
    PublisherRepository
)
from elabodeal.api.interactors import (
    CreatePublisherInteractor,
    FollowPublisherInteractor,
    UnFollowPublisherInteractor,
    UpdatePublisherProfileInteractor,
    UpdatePublisherProfileBannerImgInteractor,
    UpdatePublisherProfileAvatarImgInteractor
)
from elabodeal.api.serializers import (
    PublisherProfileSerializer,
    CreatePublisherRequestSerializer,
    FollowPublisherRequestSerializer,
    UpdatePublisherProfileRequestSerializer,
    UpdatePublisherProfileAvatarImgRequestSerializer,
    UpdatePublisherProfileBannerImgRequestSerializer
)


class CreatePublisherEndpoint(Endpoint):
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


class UpdatePublisherProfileEndpoint(Endpoint):
    def put(self, request):
        serialized_request = UpdatePublisherProfileRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        publisher = request.user.publisher

        product_repo = ProductRepository()
        publisher_repo = PublisherRepository()

        interactor = UpdatePublisherProfileInteractor(
            product_repo=product_repo,
            publisher_repo=publisher_repo
        )
        updated_publisher = interactor.execute(
            publisher,
            **serialized_request.validated_data
        )

        serialized_updated_publisher = PublisherProfileSerializer(updated_publisher)

        return self.respond(
            data={ 'profile': serialized_updated_publisher.data },
            status=200
        )


class UpdatePublisherProfileBannerImgEndpoint(Endpoint):
    def put(self, request):
        serialized_request = UpdatePublisherProfileBannerImgRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        publisher = request.user.publisher

        file_repo = FileRepository()
        publisher_repo = PublisherRepository()

        interactor = UpdatePublisherProfileBannerImgInteractor(
            file_repo=file_repo,
            publisher_repo=publisher_repo
        )
        updated_publisher = interactor.execute(
            publisher,
            **serialized_request.validated_data
        )

        serialized_updated_publisher = PublisherProfileSerializer(updated_publisher)

        return self.respond(
            data={ 'profile': serialized_updated_publisher.data },
            status=200
        )


class UpdatePublisherProfileAvatarImgEndpoint(Endpoint):
    def put(self, request):
        serialized_request = UpdatePublisherProfileAvatarImgRequestSerializer(
            data=request.data
        )
        serialized_request.is_valid(raise_exception=True)

        publisher = request.user.publisher

        file_repo = FileRepository()
        publisher_repo = PublisherRepository()

        interactor = UpdatePublisherProfileAvatarImgInteractor(
            file_repo=file_repo,
            publisher_repo=publisher_repo
        )
        updated_publisher = interactor.execute(
            publisher,
            **serialized_request.validated_data
        )

        serialized_updated_publisher = PublisherProfileSerializer(updated_publisher)

        return self.respond(
            data={ 'profile': serialized_updated_publisher.data },
            status=200
        )