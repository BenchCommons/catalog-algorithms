#include <metal_stdlib>
using namespace metal;

// Metal 3.2+ supports os_log in shaders.
kernel void hello_world()
{
    os_log_default.log("Hello World");
}
