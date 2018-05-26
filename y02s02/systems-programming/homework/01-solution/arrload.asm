	section .text
	global  _loadarr
	extern  _fopen, _fclose, _fscanf, _printf

; loadarr(long *arr, char *filename)
_loadarr:
	; set up the stack
	push    rbp
	mov     rbp, rsp

	; transfer arguments
	mov     r15, rdi      ; r15 = arr
	mov     r14, rsi      ; r14 = filename
	; open the file
	mov     rdi, r14
	lea     rsi, [rel moderead]
	call    _fopen
	mov     [rel fp], rax ; fp = fopen(filename, "r");

	mov     r13, r15      ; store current array index
	mov     r12, 10       ; i = 10
readarr:
	; read number from file
	mov     rdi, [rel fp]
	lea     rsi, [rel fmtldn]
	mov     rdx, r13
	mov     al, 0
	call    _fscanf 
	; fscanf(fp, "%ld\n", &a[i]);
	add     r13, 8        ; advance to next element
	dec     r12           ; decrease loop counter
	cmp     r12, 0
	jnz     readarr       ; check if loop didnt end
; end readarr

	mov     r13, r15
	mov     r12, 10
printarr:
	lea     rdi, [rel fmtldn]
	mov     rsi, [rel r13]
	mov     al, 0
	call    _printf
	add     r13, 8
	dec     r12
	cmp     r12, 0
	jnz     printarr

fclose:
	mov     rdi, [rel fp] 
	call    _fclose

	mov     rsp, rbp
	pop     rbp
	ret
; end loadarr()

	section .bss
fp:     resq 1

	section .data
moderead:
	db "r", 0
fmtldn:
	db "%ld", 10, 0

