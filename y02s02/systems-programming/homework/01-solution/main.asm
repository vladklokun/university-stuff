	section .text
	global  _main
	extern  _printf, _loadarr, _scanf, _findmin, _findmax, _dir,\
	_tree

_main:
	push    rbx ; prepare the stack

taskselection:
	; print selection prompt
	lea     rdi, [rel selprompt]
	mov     al, 0
	call    _printf

	; scan the choice
	lea     rdi, [rel fmtsel]
	lea     rsi, [rel sel]
	mov     al, 0
	call    _scanf

	; '1' (49) = task1, '2' (50) = task2
	; any other char = exit
	cmp     byte [rel sel], 49
	je      task1
	cmp     byte  [rel sel], 50
	je      task2
	jmp     exit

task1:
	; prompt for lower and upper bounds (a, b)
	lea     rdi, [rel abprompt]
	mov     al, 0
	call    _printf

	; read the bounds
	lea     rdi, [rel fmtab]
	lea     rsi, [rel a]
	lea     rdx, [rel b]
	mov     al, 0
	call    _scanf

	; load array from file
	lea     rdi, [rel arr]
	lea     rsi, [rel filename]
	call    _loadarr

	; findmin(arr, lowerbound, upperbound);
	lea     rdi, [rel arr]
	mov     rsi, [rel a]
	mov     rdx, [rel b]
	call    _findmin
	mov     [rel resmin], rax

	; findmax(arr, lowerbound, upperbound);
	lea     rdi, [rel arr]
	mov     rsi, [rel a]
	mov     rdx, [rel b]
	call    _findmax
	mov     [rel resmax], rax

	; print min and max values
	lea     rdi, [rel fmtld]
	mov     rsi, [rel resmin] 
	mov     rdx, [rel resmax]
	mov     al, 0
	call    _printf

	; return to task selection
	jmp     taskselection

task2:
	call    _dir          ; emulate DIR
	call    _tree         ; print directory tree
	jmp     taskselection ; return to task selection

exit:
	pop     rbx           ; clean up the stack
	xor     rax, rax      ; EXIT_SUCCESS
	ret

	section .bss
sel:    resb 256
a:      resq 1
b:      resq 1
resmin: resq 1
resmax: resq 1
arr:    resq 10

	section .data
selprompt:
	db "Welcome!", 10,\
	   "Please select the task (1, 2).", 10,\
	   "If you want to quit, type anything else.", 10,\
	   "Your choice: ", 0
fmtsel:
	db "%s", 0
abprompt:
	db "Enter min range bound A and max range bound B:", 10, 0
fmtld:
	db "Min_ab: %ld", 9, "Max_ab: %ld", 10, 0
fmtab:
	db "%ld %ld", 0
filename:
	db "arrtestfile", 0

