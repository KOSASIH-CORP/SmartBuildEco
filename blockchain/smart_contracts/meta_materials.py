pragma solidity ^0.8.0;

import "https://github.com/meta-materials-solidity/contracts/MetaMaterial.sol";

contract MetaMaterials {
    address private owner;
    mapping (uint256 => MetaMaterial) public metaMaterials;

    constructor() public {
        owner = msg.sender;
    }

    function createMetaMaterial(uint256 id, string memory name, string memory description) public {
        MetaMaterial memory metaMaterialInstance = MetaMaterial(id, name, description, new uint256[](0));
        metaMaterials[id] = metaMaterialInstance;
    }

    function designMetaMaterial(uint256 id, uint256[] memory designParameters) public {
        require(metaMaterials[id].id == id, "Meta material not found");
        metaMaterials[id].design(designParameters);
    }

    function simulateMetaMaterialBehavior(uint256 id, uint256[] memory simulationParameters) public view returns (uint256[] memory) {
        MetaMaterial memory metaMaterialInstance = metaMaterials[id];
        return metaMaterialInstance.simulate(simulationParameters);
    }
}
