	global    _main
	extern    _scanf
	extern    _printf
	
	section .text
_main:
	push    rbx ; align the stack

	lea     rdi, [rel fmtoutstr] ; load format string
	lea     rsi, [rel inputprompt] ; load input prompt text
	call    _printf

	lea     rdi, [rel fmtinstr] ; load input format string
	lea     rsi, [rel inputstr] ; load pointer to stored data
	call    _scanf

	lea     rdi, [rel fmtoutstr] ; load format string
	lea     rsi, [rel inputstr] ; load the string we read
	call    _printf

	pop     rbx ; clean up the stack
	ret

	section .data
fmtoutstr:      db "%s", 10, 0 ; equivalent to "%s\n"
inputprompt:    db "Enter a string:", 0
fmtinstr:       db "%[^", 10, "]s", 0 ; equiv to "%[^\n]s"

	section .bss
inputstr:    resb    256 
