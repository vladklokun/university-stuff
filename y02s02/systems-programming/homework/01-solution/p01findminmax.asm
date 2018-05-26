	section .text
	global  _findmin, _findmax

%assign ARRAYELCOUNT 10

; returns min value N that satisfies:
; lowerbound < N < upperbound
; if no such value exists, returns -1
; findmin(long int *arr, long lowerbound, long upperbound);
_findmin:
	; set up the stack
	push    rbp
	mov     rbp, rsp

	; load inital values
	mov     r8, rsi           ; r8 = lowerbound
	mov     r9, rdx           ; r9 = upperbound
	mov     r10, 0            ; minchanged = FALSE 
	mov     rax, r9           ; current min value (a[0])
	; rsi holds current array pointer
	lea     rsi, [rdi]        ; rsi = arr
	mov     rcx, ARRAYELCOUNT ; set loop counter
	; rax = currmin = a[0];
	; rsi = &a[0]

findminloop:
	; check if a[i] <= currmin
 	cmp     [rsi], rax
	jg      .enditer
	; finalize iteration if it's not

	; check if a[i] > lowerbound
	cmp     [rsi], r8
	jle     .enditer 
	; finalize iteration if it's not

	; check if a[i] < upperbound
	cmp     [rsi], r9
	jge     .enditer 
	; finalize iteration if it's not

	; since lowerbound < a[i] < upperbound
	; set currmin = a[i]
	mov     rax, [rsi]        ; currmin = a[i]
	mov     r10, 1            ; minchanged = TRUE

.enditer:
	add     rsi, 8            ; select next item in array
	loop    findminloop 

	; if min has not been changed, return rax = -1
	cmp     r10, 1
	je      endfindmin
	mov     rax, -1

endfindmin:
	; clean up the stack
	mov     rsp, rbp
	pop     rbp
	ret
; end _findmin()

; returns max value N that satisfies:
; lowerbound < N < upperbound
; if no such value exists, returns -1
; findmax(long int *arr, long lowerbound, long upperbound);
_findmax:
	; set up the stack
	push    rbp
	mov     rbp, rsp

	; load inital values
	mov     r8, rsi           ; r8 = lowerbound
	mov     r9, rdx           ; r9 = upperbound
	mov     r10, 0            ; maxchanged = FALSE 
	mov     rax, r8           ; current max value = lowerbound
	; rsi holds current array pointer
	lea     rsi, [rdi]        ; rsi = arr
	mov     rcx, ARRAYELCOUNT ; set loop counter
	; rax = currmax = a[0];
	; rsi = &a[0]

findmaxloop:
	; check if a[i] >= currmax
 	cmp     [rsi], rax
	jl      .enditer
	; finalize iteration if it's not

	; check if a[i] > lowerbound
	cmp     [rsi], r8
	jle     .enditer 
	; finalize iteration if it's not

	; check if a[i] < upperbound
	cmp     [rsi], r9
	jge     .enditer 
	; finalize iteration if it's not

	; since lowerbound < a[i] < upperbound
	; set currmax = a[i]
	mov     rax, [rsi]        ; currmax = a[i]
	mov     r10, 1            ; maxchanged = TRUE

.enditer:
	add     rsi, 8            ; select next item in array
	loop    findmaxloop 

	; if max has not been changed, return rax = -1
	cmp     r10, 1
	je      endfindmax
	mov     rax, -1

endfindmax:
	; clean up the stack
	mov     rsp, rbp
	pop     rbp
	ret
; end _findmax()

