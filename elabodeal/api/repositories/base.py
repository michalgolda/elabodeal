from abc import ABC, abstractmethod


class Repository(ABC):

    @abstractmethod
    def add(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    def get_all_by(self, *args, **kwargs):
    	raise NotImplementedError

    @abstractmethod
    def get_one_by(self, *args, **kwargs):
    	raise NotImplementedError

    @abstractmethod
    def delete_by(self, *args, **kwargs):
        raise NotImplementedError
