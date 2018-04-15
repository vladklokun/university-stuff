	section .text
	global  _main
	extern  _time, _localtime, _strftime, _puts

_main:
	push    rbx

; get current time
	lea     rdi, [rel rawtime]
	call    _time
; current time_t is now in rawtime

; convert raw time to tm struct
	lea     rdi, [rel rawtime]
	call    _localtime
; tm struct is now in rax

; add half a year
	mov     r15, rax ; pointer to struct tm
	add     r15, 16 ; access tm_mon at rax + 16
	add     qword [r15], qword 6 ; add half a year
	cmp     qword [r15], 12 ; check for overflow
	jg      monalreadynormal ; jump if mon <= 12
	sub     qword [r15], 12 ; if mon > 12, correct overflow
;

monalreadynormal:
; format tm struct as full month name
	lea     rdi, [rel resmon]
	mov     rsi, 32
	lea     rdx, [rel fmtmonout]
	mov     rcx, rax
	call    _strftime
; resulting month is now in resmon 

; print full name of the resulting month 
	lea     rdi, [rel resmon]
	call    _puts
;
	
	pop     rbx
	ret

	section .data
fmtmonout:      db "%B", 0

	section .bss
rawtime:        resq 1
resmon:         resb 32

