OPENQASM 3.0;
// Quantum circuits cannot print text; the classical register reads 1 on measurement.
qubit q;
bit hello;
x q;
hello = measure q;
