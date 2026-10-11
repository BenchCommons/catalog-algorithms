        * = $c000

        ldx #0
loop:   lda msg,x
        beq done
        jsr $ffd2       ; KERNAL CHROUT
        inx
        bne loop
done:   rts

msg:    .text "HELLO WORLD"
        .byte 13, 0
