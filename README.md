# braintropper
## Lucian Murdin

# Description

Scheduler task for Demand Logic: sorting tasks to operate on last hour's worth of data, then backfill if already complete.

# Notes

Time spent : 2 hours over a few days
I started by reading the brief and trying to understand the object of the task. I moved on to implementing the next_to_do function to detect which period was next for a task to fill out. I then updated the get_tasks_to_do function for the scheduler to organise the tasks by ones which had open to_do periods and by most recent. I used extra time as I required more time to read and understand the brief.

I encountered the most difficulty in understanding the "when" parameter. I first took it to mean the current time for each task, but I then re-read the brief and realised it meant the last full hour. I intended to use this parameter to detect which tasks needed completing first with recent to_do periods (by comparing when to latest_done), but I realised that in the schedule_tasks function "get_tasks_to_do" is called before "schedule", which provides the "when" parameter that I needed. I refactored by code to use on latest/earliest_done and start_from, repeat_until in the next_to_do function.

I believe if I spent more time on this task I would achieve greater understanding and be able to complete my code, as currently I have only made a start on the first couple of tasks and not moved on to backfill and tasks keeping track of progress.

Thanks for the opportunity and your consideration.