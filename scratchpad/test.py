event = {
    "payload": "These unique properties of qubits allow quantum computers to perform certain calculations much faster than classical computers. For example, they can solve complex problems in cryptography, optimize large systems, or simulate the behavior of molecules for drug discovery."
}

data = event['payload']

for line in data.split('\n'):
    print(line)