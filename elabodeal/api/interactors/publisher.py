from elabodeal.api.interactors import Interactor


class CreatePublisherInteractor(Interactor):
	def __init__(self, user_repo, publisher_repo):
		self.user_repo = user_repo
		self.publisher_repo = publisher_repo

	def execute(
		self, user, first_name, 
		last_name, swift, account_number):

		publisher = self.publisher_repo.add(
			swift=swift,
			last_name=last_name,
			first_name=first_name,
			account_number=account_number
		)

		user.publisher = publisher

		self.user_repo.save(user)

		return publisher


class FollowPublisherInteractor(Interactor):
	def __init__(self, user_repo, publisher_repo):
		self.user_repo = user_repo
		self.publisher_repo = publisher_repo

	def execute(self, user, publisher_id):
		user_already_following = user.already_following(publisher_id)
		
		if user_already_following: return

		publisher = self.publisher_repo.get_one_by(id=publisher_id)

		user.followers.add(publisher)
		publisher.followers.add(user)

		self.user_repo.save(user)
		self.publisher_repo.save(publisher)


class UnFollowPublisherInteractor(Interactor):
	def __init__(self, user_repo, publisher_repo):
		self.user_repo = user_repo
		self.publisher_repo = publisher_repo

	def execute(self, user, publisher_id):
		user_already_following = user.already_following(publisher_id)
		
		if not user_already_following: return

		publisher = self.publisher_repo.get_one_by(id=publisher_id)

		user.followers.remove(publisher)
		publisher.followers.remove(user)
		
		self.user_repo.save(user)
		self.publisher_repo.save(publisher)


class UpdatePublisherProfileInteractor(Interactor):
	def __init__(self, publisher_repo, product_repo):
		self.product_repo = product_repo
		self.publisher_repo = publisher_repo

	def execute(
		self, 
		publisher,
		bio,
		banner_text, 
		who_you_are,
		banner_product
	):
		if banner_product: banner_product = self.product_repo.get_one_by(id=banner_product)

		publisher.bio = bio
		publisher.who_you_are = who_you_are
		publisher.banner_text = banner_text
		publisher.banner_product = banner_product

		self.publisher_repo.save(publisher)

		return publisher


class UpdatePublisherProfileBannerImgInteractor(Interactor):
	def __init__(self, publisher_repo, file_repo):
		self.file_repo = file_repo
		self.publisher_repo = publisher_repo

	def execute(self, publisher, banner_img):
		if banner_img: banner_img = self.file_repo.add(banner_img, type='image')

		publisher.banner_img = banner_img

		self.publisher_repo.save(publisher)

		return publisher

class UpdatePublisherProfileAvatarImgInteractor(Interactor):
	def __init__(self, publisher_repo, file_repo):
		self.file_repo = file_repo
		self.publisher_repo = publisher_repo

	def execute(self, publisher, avatar_img):
		if avatar_img: avatar_img = self.file_repo.add(avatar_img, type='image')

		publisher.avatar_img = avatar_img	

		self.publisher_repo.save(publisher)

		return publisher