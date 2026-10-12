    .global _start
    .text
_start:
    mov x0, #1          // stdout
    ldr x1, =msg
    mov x2, #12         // length
    mov x8, #64         // sys_write
    svc #0

    mov x0, #0
    mov x8, #93         // sys_exit
    svc #0

    .data
msg:
    .ascii "Hello World\n"
