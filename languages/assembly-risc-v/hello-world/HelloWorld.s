    .global _start
    .text
_start:
    li a0, 1            # stdout
    la a1, msg
    li a2, 12           # length
    li a7, 64           # sys_write
    ecall

    li a0, 0
    li a7, 93           # sys_exit
    ecall

    .data
msg:
    .ascii "Hello World\n"
