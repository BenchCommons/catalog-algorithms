// WGSL has no printing; this fragment shader renders the colors of the "Hello World" logo instead.
@fragment
fn main() -> @location(0) vec4<f32> {
    return vec4<f32>(0.0, 0.47, 0.84, 1.0);
}
