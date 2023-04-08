from abc import ABC, abstractmethod


class KeyboardHandler(ABC):

    @abstractmethod
    def is_up_pressed(self) -> bool:
        pass

    @abstractmethod
    def is_down_pressed(self) -> bool:
        pass

    @abstractmethod
    def is_left_pressed(self) -> bool:
        pass

    @abstractmethod
    def is_right_pressed(self) -> bool:
        pass

    @abstractmethod
    def clear_flags(self) -> None:
        pass