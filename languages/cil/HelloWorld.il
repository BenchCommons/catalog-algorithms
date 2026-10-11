.assembly extern mscorlib {}
.assembly HelloWorld {}

.method static void Main()
{
    .entrypoint
    ldstr "Hello World"
    call void [mscorlib]System.Console::WriteLine(string)
    ret
}
