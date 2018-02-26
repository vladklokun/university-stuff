	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.intel_syntax noprefix
	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
## BB#0:
	push	rbp
	mov	rbp, rsp
	sub	rsp, 288
	lea	rdi, [rip + L_.str]
	mov	rax, qword ptr [rip + ___stack_chk_guard@GOTPCREL]
	mov	rax, qword ptr [rax]
	mov	qword ptr [rbp - 8], rax
	mov	dword ptr [rbp - 276], 0
	mov	al, 0
	call	_printf
	lea	rdi, [rip + L_.str.1]
	lea	rsi, [rbp - 272]
	mov	dword ptr [rbp - 280], eax ## 4-byte Spill
	mov	al, 0
	call	_scanf
	lea	rdi, [rip + L_.str.2]
	lea	rsi, [rbp - 272]
	mov	dword ptr [rbp - 284], eax ## 4-byte Spill
	mov	al, 0
	call	_printf
	mov	rsi, qword ptr [rip + ___stack_chk_guard@GOTPCREL]
	mov	rsi, qword ptr [rsi]
	cmp	rsi, qword ptr [rbp - 8]
	mov	dword ptr [rbp - 288], eax ## 4-byte Spill
	jne	LBB0_2
## BB#1:
	xor	eax, eax
	add	rsp, 288
	pop	rbp
	ret
LBB0_2:
	call	___stack_chk_fail

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"Please enter a string:"

L_.str.1:                               ## @.str.1
	.asciz	"%s"

L_.str.2:                               ## @.str.2
	.asciz	"You entered: \"%s\"\n"


.subsections_via_symbols
