from abc import ABC, abstractmethod


class IInteractor(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs) -> None:
        raise NotImplementedError()


class Interactor(IInteractor):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        pass