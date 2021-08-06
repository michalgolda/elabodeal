from elabodeal.celery.tasks import send_email
from elabodeal.api.interactors import Interactor
from elabodeal.emails import ConfirmEmailChangeEmailDTO


def update_model_attrs(model, attrs):
	is_updated = False

	for attr_name, attr_value in attrs.items():
		if attr_value != None:
			if getattr(model, attr_name) != attr_value:
				setattr(model, attr_name, attr_value)

				is_updated = True

	return is_updated 


class UpdateUserSettingsInteractor(Interactor):
	def __init__(self, user_repo):
		self.user_repo = user_repo

	def execute(self, user, fields):
		updated_model_attrs = update_model_attrs(
			user,
			fields
		)

		if updated_model_attrs:
			self.user_repo.save(user)


class UpdatePublisherSettingsInteractor(Interactor):
	def __init__(self, publisher_repo):
		self.publisher_repo = publisher_repo

	def execute(self, publisher, fields):
		updated_model_attrs = update_model_attrs(
			publisher,
			fields
		)

		if updated_model_attrs:
			self.publisher_repo.save(publisher)


class ChangeEmailRequestInteractor(Interactor):
	def __init__(self, verification_code_repo):
		self.verification_code_repo = verification_code_repo

	def execute(self, email):
		verification_code = self.verification_code_repo.add(email=email)

		email_context = {
			'code': verification_code.code
		}

		email_dto = ConfirmEmailChangeEmailDTO(
			to=email,
			context=email_context
		)

		serialized_email_dto = email_dto.asdict()

		send_email.delay(serialized_email_dto)


class ConfirmEmailChangeRequestInteractor(Interactor):
	def __init__(self, user_repo, verification_code_repo):
		self.user_repo = user_repo
		self.verification_code_repo = verification_code_repo

	def execute(self, user, email):
		user.email = email

		self.user_repo.save(user)
		self.verification_code_repo.delete_by(email=email)


class ChangePasswordInteractor(Interactor):
	def __init__(self, user_repo):
		self.user_repo = user_repo

	def execute(self, user, new_password):
		user.set_password(new_password)

		self.user_repo.save(user)

