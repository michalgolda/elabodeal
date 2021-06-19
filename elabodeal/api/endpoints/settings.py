from elabodeal.api.endpoints import Endpoint
from elabodeal.api.permissions import PublisherOnlyAccess
from elabodeal.api.interactors import (
	UpdateUserSettingsInteractor,
	UpdatePublisherSettingsInteractor,
	ChangeEmailRequestInteractor,
	ConfirmEmailChangeRequestInteractor
)
from elabodeal.api.repositories import (
	UserRepository,
	PublisherRepository,
	VerificationCodeRepository
)
from elabodeal.api.serializers import (
	UpdateUserSettingsRequestSerializer,
	UpdatePublisherSettingsRequestSerializer,
	ChangeEmailRequestSerializer,
	ConfirmEmailChangeRequestSerializer
)


class MeUpdateSettingsEndpoint(Endpoint):
	def put(self, request):
		user = request.user

		serialized_request = UpdateUserSettingsRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		user_repo = UserRepository()

		interactor = UpdateUserSettingsInteractor(
			user_repo=user_repo
		)
		interactor.execute(
			user, 
			serialized_request.validated_data
		)

		return self.respond(status=200)


class MeUpdatePublisherSettingsEndpoint(Endpoint):
	permission_classes = [PublisherOnlyAccess]

	def put(self, request):
		publisher = request.user.publisher

		serialized_request = UpdatePublisherSettingsRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		publisher_repo = PublisherRepository()

		interactor = UpdatePublisherSettingsInteractor(
			publisher_repo=publisher_repo
		)
		interactor.execute(
			publisher,
			serialized_request.validated_data
		)

		return self.respond(status=200)


class MeChangeEmailRequestEndpoint(Endpoint):

	def post(self, request):
		serialized_request = ChangeEmailRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		verification_code_repo = VerificationCodeRepository()

		interactor = ChangeEmailRequestInteractor(
			verification_code_repo=verification_code_repo
		)
		interactor.execute(**serialized_request.validated_data)

		return self.respond(status=200)


class MeConfirmEmailChangeRequestEndpoint(Endpoint):

	def post(self, request):
		user = request.user

		serialized_request = ConfirmEmailChangeRequestSerializer(
			data=request.data
		)
		serialized_request.is_valid(raise_exception=True)

		user_repo = UserRepository()
		verification_code_repo = VerificationCodeRepository()

		interactor = ConfirmEmailChangeRequestInteractor(
			user_repo=user_repo,
			verification_code_repo=verification_code_repo
		)
		interactor.execute(
			user, 
			**serialized_request.validated_data
		)

		return self.respond(status=200)