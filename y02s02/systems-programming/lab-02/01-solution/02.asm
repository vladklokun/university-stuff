	section .text
	global  _main
	extern  _printf, _scanf, _tolower

_main:
	push    rbx ; align stack for 8 byte return address

	lea     rdi, [rel sfmtstr]
	lea     rsi, [rel inputprompt]
	xor     rax, rax
	call    _printf

	lea     rdi, [rel fmtinstr]
	lea     rsi, [rel instr]
	call    _scanf

	lea     r15, [rel instr] ; store input string in r15
	lea     r14, [rel resstr] ; store resulting string ptr in r14

printlower:
	movsx   rdi, byte [rel r15]
	mov     al, 0
	call    _tolower

	mov     [rel r14], rax ; save tolower() result to resstr
	inc     r14 ; increment resulting string pointer
	inc     r15 ; increment input string pointer
	cmp     byte [rel r15], 0 ; check if instr ended
	jne     printlower ; loop if it didnt end

	mov     byte [rel r14], 0 ; zeroise string

	lea     rdi, [rel sfmtstr]
	lea     rsi, [rel resstr] ; load pointer to built string 
	xor     rax, rax
	call    _printf

	pop     rbx
	ret

	section .data
inputprompt:    db "Enter a string:", 0
fmtinstr:       db "%[^", 10, "]s", 0 ; "%[^\n]s"
sfmtstr:        db "%s", 10, 0
	
	section .bss
instr:          resb 255
resstr:         resb 255
