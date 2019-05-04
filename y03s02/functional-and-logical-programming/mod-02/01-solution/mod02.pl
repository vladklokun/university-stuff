% Оголошуємо динамічні предикаті — ті, що можуть змінитись в базі даних
:- dynamic
	stack/2,
	task/2.

% task(id, name, duration).
% завдання(ID, ім'я, тривалість виконання (с)).
task(0, [send_email, 10]).
task(1, [cleanup, 55]).
task(2, [backup_db, 100]).
task(3, [run_checks, 50]).

% stack(name, [tasks]).
% стек(ім'я, [список завдань у стеку за ID]).
stack(s0, [0, 1, 2, 3]).
stack(s1, [1, 0, 3]).
stack(s2, [1, 2, 3]).

% Рекурсивна перевірка, чи є завдання в стеці
% task_in_stack(завдання, стек)
task_in_stack(Task, [Task | _]).
task_in_stack(Task, [_ | T]) :-
	task_in_stack(Task, T).

tasks_take_longer_than(StackName, Task, DurationThreshold) :-
	% Отримати зміст завдань в стеку
	stack(StackName, StackContents),
	% Отримати завдання зі стеку
	task_in_stack(Task, StackContents),
	% Знайти тривалість завдання
	task(Task, [_, Duration]),
	% Істина, якщо тривалість більша за поріг.
	Duration > DurationThreshold.

% push(Task, Stack, NewStack).
push(Task, Stack, [Task | Stack]).
% pop(Stack, NewStack, PoppedItem).
pop([StackHead | StackTail], StackTail, StackHead).

% Витягнути верхній елемент стеку і записати
% отриманий стек в динамічну базу даних
pop_db(StackName) :-
	% Знайти стек і його зміст за ім'ям
	stack(StackName, Contents),
	% Витягнути верхній елемент
	pop(Contents, NewContents, _),
	% Видалити знання про минулий стек з бази даних
	retract(stack(StackName, _)),
	% І замінити їх новими
	assertz(stack(StackName, NewContents)).
