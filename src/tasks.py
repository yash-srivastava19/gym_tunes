from datetime import datetime
from crewai import Task
    
date = datetime.today().strftime('%Y-%m-%d')
timezone = datetime.now().astimezone().tzinfo

class SchedulingTask():
    def __init__(self) -> None:
        pass

    def generate_schedule_task(self, agent, desc, time_for_play):
        return Task(
            description=f"Schedule an event with the message as '{desc}'. Schedule it for today. Today's date is {date} (it's in YYYY-MM-DD format) and make the timezone be {timezone} at time {time_for_play}.",
            agent=agent,
            expected_output="Check of the task was sucessfully completed.",
        )