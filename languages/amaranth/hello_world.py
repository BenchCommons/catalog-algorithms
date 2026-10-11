from amaranth.hdl import Module
from amaranth.sim import Simulator


async def hello(ctx):
    print("Hello World")


sim = Simulator(Module())
sim.add_testbench(hello)
sim.run()
