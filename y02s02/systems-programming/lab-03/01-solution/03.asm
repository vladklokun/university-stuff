	section .text
	global  _main
	extern  _printf

_main:
	push  rbx
	lea   r15, [rel resstr] ; load resstr pointer (current position)

	mov   rdx, 48 ; put ASCII symbol 48
	mov   rcx, 16 ; loop counter

loop1:
	push  rcx    ; save counter on stack
	and   rcx, 3 ; rcx % 4 = rcx & (4 - 1)
	cmp   rcx, 0 ; if divisible by 4 
	jne   addsymbol

addnewline:
	mov   [rel r15], byte 10 ; add newline character
	inc   r15 ; increment current position

addsymbol:
	pop   rcx ; restore counter value
	mov   [rel r15], rdx ; add current symbol to current position
	inc   r15 ; increment current position
	mov   [rel r15], byte ' ' ; add a space at current position
	inc   r15 ; increment current pos for space symbol

	inc   rdx ; increment current symbol code

	dec   rcx ; decrement loop counter
	cmp   rcx, 0
	jne   loop1 

	lea   rdi, [rel fmtstrout]
	lea   rsi, [rel resstr]
	xor   rax, rax
	call  _printf
	
	pop   rbx
	ret

	section .data
fmtstrout: db "%s", 10, 0

	section .bss
resstr:       resb 255
