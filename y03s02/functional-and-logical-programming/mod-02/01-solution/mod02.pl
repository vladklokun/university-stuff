% task(id, name, duration, date).
% queue(name, [tasks]).
task(0, send_email, 10).
task(1, cleanup, 20).
task(2, backup_db, 100).
task(3, run_checks, 50).

tasklist_add(Item, Tasklist, [Item|Tasklist]).

% Check if task is in queue
task_in_queue(Task, [Task | _]).
task_in_queue(Task, [_ | T]) :-
	task_in_queue(Task, T).

% queue_tasks([], []).
% queue_tasks([TasksH | TasksT], [TasksH | TasksT]).

tasks_take_longer_than(Queue, Task, DurationThreshhold) :-
	task_in_queue(Task, Queue),
	task(Task, _, Duration),
	Duration > DurationThreshhold.

% push(Task, Queue, Res).
push(Task, Queue, [Task | Queue]).
% pop(Queue, Res).
pop([QueueHead | QueueTail], Task).
