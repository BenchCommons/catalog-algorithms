#![cfg_attr(not(feature = "std"), no_std, no_main)]

#[ink::contract]
mod hello_world {
    #[ink(storage)]
    pub struct HelloWorld {}

    impl HelloWorld {
        #[ink(constructor)]
        pub fn new() -> Self {
            Self {}
        }

        #[ink(message)]
        pub fn hello(&self) -> ink::prelude::string::String {
            "Hello World".into()
        }
    }
}
