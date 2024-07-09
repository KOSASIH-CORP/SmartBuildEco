import solc

class SmartContractCompiler:
    def __init__(self):
        pass

    def compile_contract(self, contract_code):
        compiled_contract = solc.compile(contract_code)
        return compiled_contract
