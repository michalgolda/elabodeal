from typing import List
from abc import ABC, abstractmethod


class Repository(ABC):
    @abstractmethod
    def get(self, id: int) -> object:
        raise NotImplementedError()

    @abstractmethod
    def delete(self, object: object) -> None:
        raise NotImplementedError()

    @abstractmethod
    def save(self, object: object) -> object:
        raise NotImplementedError()