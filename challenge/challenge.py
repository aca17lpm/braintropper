import time
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Union, List


@dataclass
class HourlyTask:
    """A task to be done every hour, and backfilled if not up to date."""

    #: From when should this task start occurring?
    start_from: datetime

    #: Until when should this task occur?
    repeat_until: Union[datetime, None] = None

    #: What, if any, is the first time that has been done for this task?
    earliest_done: Union[datetime, None] = None

    #: What if any is the last (most recent) time that has been done for this
    #: task?
    latest_done: Union[datetime, None] = None

    @property
    def next_to_do(self) -> Union[datetime, None]:
        """Return the next datetime that needs doing."""

        # @TODO for recent find latest_done, if not equal to repeat_until, return plus one hour
        #  for backfill find earliest_done, return none if equal to start_from,
        #  if not then subtract one hour and return datetime

        # returning recent
        if (self.latest_done != self.repeat_until) :
            next = self.latest_done + timedelta(hours=1)
            return next
        # returning backfill
        elif (self.earliest_done != self.start_from) :
            next = self.earliest_done - timedelta(hours=1)
            return next
        else :
            return None

    def schedule(self, when: datetime) -> None:
        """Schedule this task at the 'when' time, update local time markers."""

        # @TODO update latest_done and earliest_done to reflect new time from when
        
        raise NotImplementedError("Fill me in!")


class Scheduler:
    """Schedule some work."""

    def __init__(self):
        """Initialise Scheduler."""
        self.task_store = []

    def register_task(self, task: HourlyTask) -> None:
        """Add a task to the local store of tasks known about."""
        self.task_store.append(task)

    def register_tasks(self, task_list: List[HourlyTask]) -> None:
        """Add several tasks to the local store of tasks."""
        [self.register_task(task) for task in task_list]

    def get_tasks_to_do(self) -> List[HourlyTask]:
        """Get the list of tasks that need doing."""
        # @TODO get all tasks where next_to_do != None
        return []

    def schedule_tasks(self) -> None:
        """Schedule the tasks.

        Tasks should be prioritised so that tasks with a recent "to do" date
        are done before any that need backfilling.
        """
        tasks = self.get_tasks_to_do()
        now = datetime.utcnow()
        now_hour_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        last_hour_start = now_hour_start - timedelta(hours=1)
        [task.schedule(last_hour_start) for task in tasks]


@dataclass
class Controller:
    """Use a Scheduler to repeatedly check and schedule tasks."""

    #: The scheduler that we are controlling
    scheduler: Scheduler

    #: How long to wait between each schedule check
    throttle_wait: timedelta

    #: Daemon mode?
    run_forever: bool = True

    #: Run this many times (if not in Daemon mode)
    run_iterations: int = 0

    def run(self):
        """Run scheduler"""
        while self.run_iterations or self.run_forever:
            before = datetime.utcnow()
            self.scheduler.schedule_tasks()
            self.run_iterations -= 1
            after = datetime.utcnow()
            elapsed = after - before
            wait = self.throttle_wait.total_seconds() - elapsed.total_seconds()
            time.sleep(max([0, wait]))
