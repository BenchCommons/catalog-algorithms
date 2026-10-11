from amaranth.sim import Simulator

def hello():
    print("Hello World")
    yield

sim = Simulator(None)
sim.add_process(hello)
sim.run()
