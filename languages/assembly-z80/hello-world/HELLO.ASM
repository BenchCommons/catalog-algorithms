        org 0100h

        ld de, msg
        ld c, 9         ; BDOS print string
        call 5
        ret

msg:    db 'Hello World$'
