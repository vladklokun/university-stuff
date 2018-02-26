	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 10, 11
	.intel_syntax noprefix
	.globl	_main
	.align	4, 0x90
_main:                                  ## @main
## BB#0:
	push	rbp
	mov	rbp, rsp
	sub	rsp, 320
	lea	rdi, [rip + L_.str]
	mov	rax, qword ptr [rip + ___stack_chk_guard@GOTPCREL]
	mov	rax, qword ptr [rax]
	mov	qword ptr [rbp - 8], rax
	mov	dword ptr [rbp - 276], 0
	mov	qword ptr [rbp - 288], 0
	mov	al, 0
	call	_printf
	lea	rdi, [rip + L_.str.1]
	lea	rsi, [rbp - 272]
	mov	dword ptr [rbp - 300], eax ## 4-byte Spill
	mov	al, 0
	call	_scanf
	lea	rdi, [rip + L_.str.2]
	lea	rsi, [rbp - 272]
	mov	dword ptr [rbp - 304], eax ## 4-byte Spill
	mov	al, 0
	call	_printf
	lea	rdi, [rbp - 272]
	mov	dword ptr [rbp - 308], eax ## 4-byte Spill
	call	_strlen
	mov	qword ptr [rbp - 288], rax
	mov	qword ptr [rbp - 296], 0
LBB0_1:                                 
	mov	rax, qword ptr [rbp - 296]
	cmp	rax, qword ptr [rbp - 288]
	jae	LBB0_6
## BB#2:                                
	mov	rax, qword ptr [rbp - 296]
	add	rax, 1
	and	rax, 1
	cmp	rax, 0
	jne	LBB0_4
## BB#3:                                
	lea	rdi, [rip + L_.str.3]
	mov	rax, qword ptr [rbp - 296]
	movsx	esi, byte ptr [rbp + rax - 272]
	mov	al, 0
	call	_printf
	mov	dword ptr [rbp - 312], eax ## 4-byte Spill
LBB0_4:                                 
	jmp	LBB0_5
LBB0_5:                                 
	mov	rax, qword ptr [rbp - 296]
	add	rax, 1
	mov	qword ptr [rbp - 296], rax
	jmp	LBB0_1
LBB0_6:
	mov	rax, qword ptr [rip + ___stack_chk_guard@GOTPCREL]
	mov	rax, qword ptr [rax]
	cmp	rax, qword ptr [rbp - 8]
	jne	LBB0_8
## BB#7:
	xor	eax, eax
	add	rsp, 320
	pop	rbp
	ret
LBB0_8:
	call	___stack_chk_fail

	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"Enter a string:\n"

L_.str.1:                               ## @.str.1
	.asciz	"%[^\n]s"

L_.str.2:                               ## @.str.2
	.asciz	"You entered: %s\n"

L_.str.3:                               ## @.str.3
	.asciz	"%c\n"


.subsections_via_symbols
