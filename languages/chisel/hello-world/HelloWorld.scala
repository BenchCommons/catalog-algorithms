import chisel3._

class HelloWorld extends Module {
  val io = IO(new Bundle {})
  printf("Hello World\n")
}
