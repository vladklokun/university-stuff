	section .text
	global    _main
	extern    _printf, _scanf

_main:
	push    rbx ; align the stack (8 byte for return address)

	lea     rdi, [rel fmtoutstr] ; load pointer to format string
	lea     rsi, [rel inputprompt] ; same for input prompt string
	call    _printf

	lea     rdi, [rel fmtinstr]
	lea     rsi, [rel instr]
	call    _scanf

	lea     r8, [rel instr + 1] ; load second string element

.loop:
	mov     rax, 0x2000004 ; SYS_WRITE
	mov     rdi, 1 ; STDOUT
	lea     rsi, [rel r8]
	mov     rdx, 1 ; write 1 byte (char)
	syscall

	add     r8, 2 ; advance 2 bytes (next even char)

	cmp     byte [r8], 0 ; check if string ended
	jne     .loop ; if not, repeat the loop

	mov     rax, 0x2000004
	mov     rdi, 1 ; STDOUT
	lea     rsi, [rel newline]
	mov     rdx, 1 ; write 1 byte (char)
	syscall

	pop     rbx ; clean up the stack (8 bytes back)
	ret

	section .data
fmtoutstr:    db "%s", 10, 0 ; "%s\n"
inputprompt:  db "Enter a string: ", 0
fmtinstr:     db "%[^", 10, "]s", 0 ; "%[^\n]s"
newline:      db 10

	section .bss
instr:        resb    255 ; reserve 255 bytes
