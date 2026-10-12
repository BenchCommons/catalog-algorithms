.global _main
.align 2

_main:
    mov x0, #1              ; stdout
    adrp x1, msg@PAGE
    add x1, x1, msg@PAGEOFF
    mov x2, #12             ; length
    mov x16, #4             ; write
    svc #0x80

    mov x0, #0
    mov x16, #1             ; exit
    svc #0x80

.data
msg: .ascii "Hello World\n"
