from abc import ABC, abstractmethod


class Interactor(ABC):
   
   @abstractmethod
   def execute(self, *args, **kwargs):
   		raise NotImplementedError