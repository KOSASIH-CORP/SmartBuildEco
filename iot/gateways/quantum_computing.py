import qiskit
from qiskit import QuantumCircuit, execute

class QuantumComputing:
    def __init__(self, backend):
        self.backend = backend

    def create_circuit(self, num_qubits):
        circuit = QuantumCircuit(num_qubits)
        return circuit

    def add_gates(self, circuit, gates):
        for gate in gates:
            circuit.append(gate, [i for i in range(circuit.num_qubits)])
        return circuit

    def execute_circuit(self, circuit):
        job = execute(circuit, self.backend)
        result = job.result()
        return result

    def get_measurement(self, result):
        measurement = result.get_counts()
        return measurement

# Example usage:
backend = qiskit.BasicAer.get_backend('qasm_simulator')
quantum_computing = QuantumComputing(backend)
circuit = quantum_computing.create_circuit(5)
gates = [qiskit.gates.HGate(), qiskit.gates.CXGate()]
circuit = quantum_computing.add_gates(circuit, gates)
result = quantum_computing.execute_circuit(circuit)
measurement = quantum_computing.get_measurement(result)
print(measurement)
