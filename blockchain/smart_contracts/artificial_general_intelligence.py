pragma solidity ^0.8.0;

import "https://github.com/AGI-solidity/contracts/AGIModel.sol";

contract ArtificialGeneralIntelligence {
    address private owner;
    mapping (uint256 => AGIModel) public agiModels;

    constructor() public {
        owner = msg.sender;
    }

    function createAGIModel(uint256 id, string memory name, string memory description) public {
        AGIModel memory agiModelInstance = AGIModel(id, name, description, new uint256[](0));
        agiModels[id] = agiModelInstance;
    }

    function trainAGIModel(uint256 id, uint256[] memory trainingData) public {
        require(agiModels[id].id == id, "AGI model not found");
        agiModels[id].train(trainingData);
    }

    function reason(uint256 id, uint256[] memory inputData) public view returns (uint256[] memory) {
        AGIModel memory agiModelInstance = agiModels[id];
        return agiModelInstance.reason(inputData);
    }
}
