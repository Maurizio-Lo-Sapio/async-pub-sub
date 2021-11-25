import queue
from typing import Any

import config
from data import Data

class Tasks:
    tasks_queue = None

    def __init__(self) -> None:
        self.tasks_queue = queue.Queue()

    def fill(self, data_list: Any) -> None:
        # blocks all the threads calling wait on the event
        global wait_event
        config.wait_event.clear()

        for data in data_list:
            self.tasks_queue.put(Data(data))

        # releases the wainting threads in the Worker class
        config.wait_event.set()