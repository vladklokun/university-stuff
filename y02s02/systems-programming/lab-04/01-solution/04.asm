	section .text
	global  _main
	extern  _printf, _scanf

_main:
	push    rbx ; stack alignment
	
	lea     rdi, [rel fmtstrout]
	lea     rsi, [rel inputprompt]
	mov     al, 0
	call    _printf

	mov     r15, 4 ; 4 rows in matrix
	lea     r14, [rel matrix] ; store base of matrix
; start input loop
inputloop:
	lea     rdi, [rel fmtrowin]
	lea     rsi, [rel r14]     ; current row index 0
	lea     rdx, [rel r14 + 4] ; current row index 1
	lea     rcx, [rel r14 + 8] ; current row index 2
	lea     r8,  [rel r14 + 12]; current row index 3
	mov     al, 0
	call    _scanf

	add     r14, 16 ; advance current pos by 32-bit (next int)
	dec     r15 ; decrease loop counter
	jnz     inputloop
; end input loop

	mov     r15, 4 ; loop counter = rows
	lea     r14, [rel matrix] ; store base of matrix
; start output loop
outputloop:
	add     r14, 12 ; 3 * 4 (int size)
	lea     rdi, [rel fmtintout]
	mov     rsi, [rel r14]
	mov     al, 0
	call    _printf

	;add     r14, 4
	dec     r15
	jnz     outputloop
; end output loop

; print newline
	lea     rdi, [rel newline]
	mov     al, 0
	call    _printf

	pop     rbx ; stack alignment
	ret

	section .data
fmtstrout:      db "%s", 10, 0
fmtrowin:       db "%d %d %d %d", 0
fmtintout:      db "%d ", 0
inputprompt:    db "Please enter a 4x4 matrix:", 0
newline:        db 10, 0

	section .bss
matrix:         resd 16  ; resd since we're storing 32-bit integers

