import qiskit

class IOTQuantumComputing:
    def __init__(self):
        self.backend = qiskit.BasicAer.get_backend('qasm_simulator')

    def create_quantum_circuit(self, num_qubits):
        circuit = qiskit.QuantumCircuit(num_qubits)
        return circuit

    def add_quantum_gates(self, circuit, gates):
        for gate in gates:
            circuit.append(gate, [0])
        return circuit

    def execute_quantum_circuit(self, circuit):
        job = qiskit.execute(circuit, self.backend)
        result = job.result()
        return result

# Example usage:
iot_qc = IOTQuantumComputing()
num_qubits = 2
circuit = iot_qc.create_quantum_circuit(num_qubits)
gates = [qiskit.gates.HGate(), qiskit.gates.CXGate()]
circuit = iot_qc.add_quantum_gates(circuit, gates)
result = iot_qc.execute_quantum_circuit(circuit)
print(result)
