	section .text
	global  _main
	extern  _fopen, _fclose, _puts, _fgetc, _fputc

error:
	lea     rdi, [rel errmsg]
	call    _puts
	jmp     exit

_main:
	push    rbx

; open ifile for reading
	lea     rdi, [rel ifile]
	lea     rsi, [rel readmode]
	call    _fopen
	mov     [rel ifp], rax
	cmp     rax, 0
	je      error
;

; open ofile for reading
	lea     rdi, [rel ofile]
	lea     rsi, [rel writemode]
	call    _fopen
	mov     [rel ofp], rax
	cmp     rax, 0
	je      error
;

; read ifile by character and copy to ofile
.loop:
	mov     rdi, [rel ifp]
	call    _fgetc         ; get character from ifile
	movsx   rdi, byte al   ; sign-extend it and load
	mov     rsi, [rel ofp]
	call    _fputc         ; write character to ofile
	movsx   eax, byte al   ; sign-extend recently written character
	cmp     eax, -1        ; check if c == EOF
	jne     .loop          ; jump if c != EOF
;

; close ifile
	mov     rdi, [rel ifp]
	call    _fclose
;

; close ofile
	mov     rdi, [rel ofp]
	call    _fclose
;

exit:
	pop     rbx
	ret

	section .data
ifile:
	db "infile", 0
ofile:
	db "outfile", 0
readmode:
	db "r", 0
writemode:
	db "w", 0
errmsg:
	db "fopen() failed", 10, 0

	section .bss
ifp:
	resb 16
ofp:
	resb 16

