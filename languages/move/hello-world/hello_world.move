module hello::hello_world {
    use std::string::{Self, String};

    public fun hello(): String {
        string::utf8(b"Hello World")
    }
}
