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