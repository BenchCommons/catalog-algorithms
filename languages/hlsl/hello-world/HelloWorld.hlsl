// Shaders cannot print text; this compute shader logs it with HLSL's printf (DXC, SM 6.x).
[numthreads(1, 1, 1)]
void main()
{
    printf("Hello World\n");
}
