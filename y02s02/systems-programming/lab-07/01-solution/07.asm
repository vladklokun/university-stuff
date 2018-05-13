	section .text
	global  _main
	extern  _stat, _localtime, _strftime, _puts

_main:
	push    rbx

; get file attributes
	lea     rdi, [rel filepath]
	lea     rsi, [rel statstr]
	call	_stat
; struct stat now in statstr

; convert access time (time_t) to time struct (struct tm)
	lea     rdi, [rel statstr]
	add     rdi, 40; access st_atime
	call    _localtime 
; time struct now in rax

; format tm struct as full month name
	lea     rdi, [rel datestr]
	mov     rsi, 32
	lea     rdx, [rel fmtmonout]
	mov     rcx, rax
	call    _strftime
;

; print resulting month
	lea     rdi, [rel datestr]
	call    _puts
; print resulting month

	pop rbx
	ret

	section .data
fmtoutstr:
	db "%s", 10, 0
fmtmonout:
	db "%B", 0
filepath:
	db "testfile", 0

	section .bss
statstr:
	resb 256
datestr:
	resb 256

