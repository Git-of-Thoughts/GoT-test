import PySpice.Logging.Logging as Logging
logger = Logging.setup_logging()

from PySpice.Doc.ExampleTools import find_libraries
from PySpice.Probe.Plot import plot
from PySpice.Spice.Library import SpiceLibrary
from PySpice.Spice.Netlist import Circuit
from PySpice.Unit import *

# Define the circuit
circuit = Circuit('Inverting Amplifier')

circuit.V(1, '+Vcc', circuit.gnd, 15@u_V)
circuit.V(2, '-Vcc', circuit.gnd, -15@u_V)
circuit.V(3, 'input', circuit.gnd, 'sine(0 10m 1k)')

circuit.R(1, 'input', 2, 10@u_kΩ)
circuit.R(2, 2, 'output', 100@u_kΩ)
circuit.C(1, 2, 'output', 10@u_uF)
circuit.X(1, 'OP07', 'NC', '+Vcc', '-Vcc', 2, 'output')

# Define the OP07 in the library
libraries_path = find_libraries()
spice_library = SpiceLibrary(libraries_path)
circuit.include(spice_library['OP07'])

# Perform an operating point analysis
simulator = circuit.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.transient(step_time=1@u_us, end_time=1@u_ms)

# Plot the output
plot(analysis['output'])
