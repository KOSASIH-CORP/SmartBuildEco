pragma solidity ^0.8.0;

import "https://github.com/QAI-solidity/contracts/QuantumAIModel.sol";

contract QuantumArtificialIntelligence {
    address private owner;
    mapping (uint256 => QuantumAIModel) public qaiModels;

    constructor() public {
        owner = msg.sender;
    }

    function createQAIModel(uint256 id, string memory name, string memory description) public {
        QuantumAIModel memory qaiModelInstance = QuantumAIModel(id, name, description, new uint256[](0));
        qaiModels[id] = qaiModelInstance;
    }

    function trainQAIModel(uint256 id, uint256[] memory trainingData) public {
        require(qaiModels[id].id == id, "QAI model not found");
        qaiModels[id].train(trainingData);
    }

    function reasonQuantumly(uint256 id, uint256[] memory inputData) public view returns (uint256[] memory) {
        QuantumAIModel memory qaiModelInstance = qaiModels[id];
        return qaiModelInstance.reasonQuantumly(inputData);
    }
}
