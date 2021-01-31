from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ErrorRegistry


class UpdateUserSettingsInteractor(Interactor):
    def execute(self, user: object, options: dict) -> None:
        has_changed = False

        for attr_name, attr_value in options.items():
            if getattr(user, attr_name) != attr_value:
                setattr(user, attr_name, attr_value)

                if attr_name == 'email':
                    user.email_verified = False

                has_changed = True

        if has_changed:
            user.save()