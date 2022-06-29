from abc import ABC, ABCMeta, abstactmethod
from re import I 
from collections.ab import Iterable

class DeadlinedMetaReminder(Iterable, metaclass=ABCMeta):
    
    @abstactmethod
    def is_due(self):
        pass
    
    