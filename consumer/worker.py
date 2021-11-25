import queue

import config
from tasks import Tasks
from processor import Processor
import greetings_pb2

class Worker:
    tasks = None
    processor = None
    workers = []
    results = []
    lock = None

    def __init__(self) -> None:
        self.tasks = Tasks()
        self.processor = Processor()
        self.lock = config.threading.Lock()

        for i in range(config.threads_number):
            self.workers.append(config.threading.Thread(target=self.process_tasks, daemon=True))

    def process_tasks(self) -> None:
        while True:
            config.wait_event.wait()

            try:
                data = self.tasks.tasks_queue.get_nowait()

                self.lock.acquire()
                self.results.append(self.processor.process(data))
                self.lock.release()

                self.tasks.tasks_queue.task_done()
            except queue.Empty:
                continue

    def start(self) -> None:
        for worker in self.workers:
            worker.start()

    def callback(self, ch, method, properties, body):
        greetings = greetings_pb2.Greetings()
        greetings.ParseFromString(body)

        for i in range(4):
            self.tasks.fill([greetings.greetings, greetings.greetings, greetings.greetings])
            self.tasks.tasks_queue.join()

            print(f'result: {i:2d}')
            for result in self.results:
                print(result)

            self.results = []
