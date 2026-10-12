// OpenCL C 1.2+ kernel
__kernel void hello_world(void)
{
    if (get_global_id(0) == 0) {
        printf("Hello World\n");
    }
}
