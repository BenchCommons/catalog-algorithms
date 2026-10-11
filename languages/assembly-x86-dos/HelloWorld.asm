
.model small
.data
        msg db 10d,13d,"Hello World$"

.code
        mov ax,@data
        mov ds,ax
                                        
        lea dx,msg                      
        mov ah,09h                      
        int 21h                         

        mov ax,4c00h                    
        int 21h                         
end
