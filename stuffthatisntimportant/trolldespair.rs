// fn main() {
//     let name = "Kabo";
//     println!("Hello {}!", name );
// }
// prints my name and println! is the function lol println is a macro, and we use ! to invoke it

// struct Greeting{
//     name: String,
// }

// fn main(){
//     let greeting = Greeting{
//         name: "Kabo".to_string()
//     };

//     println!("Hello, {}!", greeting.name )
// } // String is different from &str, &str is string slice.

// //What is a constructor in Rust?
// struct Greeting {
//     name: String,
// }
// impl Greeting{
//     fn new(name: &str ) -> Self{
//         Greeting {
//             name: name.to_string(),
//         }
//     }
// }
// fn main() {
//     let greeting = Greeting::new("Kabo");
//     println!("Hello, {}!", greeting.name);
// }
// // Impl block allows us to create a wtf is that tbh

// How do i make it so that I can accept either a &str or a String?

// struct Greeting {
//     name: String,
// }
// impl Greeting {
//     fn new<T: AsRef<str>>(name: T) -> Self { // The T means we have changed the type that our name is changing from a specific type to a generic type. The AsRef makes rust be asked to provide and accept any type (T) that can be represented as a str (not same as Str) 
//         Greeting { 
//             name: name.as_ref().to_string(), // AsRef is a method we can use on name, an object and it'll be referenced as a string slice. What can we do with a string slice? We can change it to String using the method .to_string()
//         } 
//     }
// }
// fn main() {
//     let greeting = Greeting::new("Kabo");
//     println!("Hello, {}!", greeting.name) // How can I ask a greeting to print itself? , i don't want it to show .name
// }
// use std::fmt; // We used a library, fmt, 

// struct Greeting {
//     name: String,
// }
// impl Greeting {
//     fn new<T: AsRef<str>>(name: T) -> Self {
//         Greeting { 
//             name: name.as_ref().to_string(), // AsRef is a method we can use on name, an object and it'll be referenced as a string slice. What can we do with a string slice? We can change it to String using the method .to_string()
//         } 
//     }
// }

// impl fmt::Display for Greeting{ // The new part, according to the documentation we implemented (impl) a Display for a custom type, Greeting,
//     fn fmt(&self, f: &mut fmt:: Formatter<'_>) -> fmt::Result {
//         write!(f, "Hello, {}!", self.name) // All we needed to do is copy the documentation word for word and make greeting print itself, making something printable on its own, This is where we edit to put the flavor text
//     }
// }
// fn main() {
//     let greeting = Greeting::new("Kabo"); // Where we put the argument
//     println!("{}", greeting) // The special syntax is  from the write!(f, "Hello, {}, self.name above.
// } 
