from elabodeal.api.interactors import Interactor
from elabodeal.api.exceptions import ErrorRegistry


class UpdatePublisherSettingsInteractor(Interactor):
    def execute(self, user: object, options: dict) -> None:
        publisher = user.publisher
        if not publisher:
            raise ErrorRegistry.UPDATE_PUBLISHER_SETTINGS(
                'If you change publisher settings you must be a publisher'
            )

        has_changed = False

        for attr_name, attr_value in options.items():
            if getattr(publisher, attr_name) != attr_value:
                setattr(publisher, attr_name, attr_value)

                has_changed = True

        if has_changed:
            publisher.save()