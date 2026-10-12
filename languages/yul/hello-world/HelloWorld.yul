object "HelloWorld" {
    code {
        // "Hello World" as a 32-byte word, returned as raw bytes
        mstore(0, 0x48656c6c6f20576f726c64000000000000000000000000000000000000000000)
        return(0, 11)
    }
}
