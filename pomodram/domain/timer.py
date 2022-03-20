from abc import abstractmethod, ABC


class Timer(ABC):
    @abstractmethod
    def schedule(self, func, seconds: int, *args, **kwargs) -> None:
        ...
