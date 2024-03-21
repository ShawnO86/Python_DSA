from abc import ABC, abstractmethod
class UndoCommand(ABC):
    
    @abstractmethod
    def execute(self):
        pass