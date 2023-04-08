import time
from abc import ABC, abstractmethod
from threading import Thread


class ClockListener(ABC):
    @abstractmethod
    def clock_ticked(self):
        pass


class Clock:

    periodic_time: float = 1.0  # provided that the time is in seconds
    listeners: list[ClockListener] = []
    active: bool = False

    def start(self):
        self.active = True
        thread = Thread(target=self.run)  # call run() in a new thread
        thread.start()

    def stop(self):
        self.active = False
        # try to interrupt the thread

    def run(self):
        while self.active:
            # sleep
            time.sleep(self.periodic_time)
            # print("woke up")
            # loop on the listeners list
            for listener in self.listeners:
                # call clock_ticked()
                listener.clock_ticked()

    def add_listener(self, listener: ClockListener):
        self.listeners.append(listener)

    def speed_up(self):
        self.periodic_time = self.periodic_time * 0.95
