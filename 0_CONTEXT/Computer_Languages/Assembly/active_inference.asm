; Active Inference Implementation in x86-64 Assembly
; Simplified floating-point belief update example

section .data
    ; Generative model parameters
    a_matrix: dq 0.8, 0.1, 0.1, 0.0  ; P(o|s) for 2 states, 2 observations
               dq 0.1, 0.8, 0.1, 0.0
    b_matrix: dq 0.9, 0.1, 0.0, 0.0  ; P(s'|s,a) simplified
               dq 0.1, 0.9, 0.0, 0.0

    ; Belief state (4 states)
    beliefs: dq 0.25, 0.25, 0.25, 0.25

    ; Temporary storage
    temp: dq 0.0, 0.0, 0.0, 0.0

    msg: db "Assembly Active Inference Demo", 10, 0

section .text
    global _start

_start:
    ; Print message
    mov rax, 1          ; sys_write
    mov rdi, 1          ; stdout
    mov rsi, msg
    mov rdx, 27         ; message length
    syscall

    ; Initialize beliefs (uniform distribution)
    call initialize_beliefs

    ; Run several inference cycles
    mov rcx, 5          ; 5 cycles
inference_loop:
    push rcx

    ; Update beliefs based on observation (simplified)
    mov rdi, 1          ; observation = 1
    call update_beliefs

    ; Select action (simplified)
    call select_action

    pop rcx
    loop inference_loop

    ; Exit
    mov rax, 60         ; sys_exit
    xor rdi, rdi
    syscall

initialize_beliefs:
    ; Set uniform beliefs
    mov rax, __float64__(0.25)
    mov [beliefs], rax
    mov [beliefs+8], rax
    mov [beliefs+16], rax
    mov [beliefs+24], rax
    ret

update_beliefs:
    ; Simplified Bayesian update
    ; beliefs[i] = a_matrix[observation][i] * beliefs[i]
    mov rbx, beliefs
    mov rcx, 4          ; 4 states
    xor rsi, rsi
update_loop:
    ; Load current belief
    movsd xmm0, [rbx + rsi*8]

    ; Multiply by likelihood (simplified)
    movsd xmm1, [a_matrix + rsi*8]
    mulsd xmm0, xmm1

    ; Store updated belief
    movsd [temp + rsi*8], xmm0

    inc rsi
    loop update_loop

    ; Normalize beliefs
    call normalize_beliefs
    ret

normalize_beliefs:
    ; Calculate sum
    xorpd xmm2, xmm2    ; sum = 0
    mov rcx, 4
    xor rsi, rsi
sum_loop:
    addsd xmm2, [temp + rsi*8]
    inc rsi
    loop sum_loop

    ; Normalize each belief
    mov rcx, 4
    xor rsi, rsi
norm_loop:
    movsd xmm0, [temp + rsi*8]
    divsd xmm0, xmm2
    movsd [beliefs + rsi*8], xmm0
    inc rsi
    loop norm_loop
    ret

select_action:
    ; Simplified action selection based on highest belief
    mov rbx, beliefs
    xor rsi, rsi
    xor rax, rax        ; best action
    movsd xmm1, [rbx]   ; max belief
    mov rcx, 4
find_max:
    movsd xmm0, [rbx + rsi*8]
    comisd xmm0, xmm1
    jbe not_higher
    movsd xmm1, xmm0
    mov rax, rsi
not_higher:
    inc rsi
    loop find_max
    ret
