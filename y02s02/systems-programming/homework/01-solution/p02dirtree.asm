	section .text
	global  _dir, _tree
	extern  _system

; emulates windows DIR behavior
; dir(void)
_dir:
	push    rbp
	mov     rbp, rsp

	lea     rdi, [rel ls]
	call    _system

	mov     rsp, rbp
	pop     rbp

	ret
; end dir()

; prints directory contents as a tree
; tree(void)
_tree:
	push    rbp
	mov     rbp, rsp

	lea     rdi, [rel tree]
	call    _system

	mov     rsp, rbp
	pop     rbp

	ret
; end tree()

	section .data
ls:
	db "ls", 0
tree:
	db "find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'",\
	0
