pragma solidity ^0.8.0;

import "https://github.com/holographic-solidity/contracts/HolographicDataStorage.sol";

contract HolographicDataStorage {
    address private owner;
    mapping (uint256 => HolographicDataStorage) public holographicData;

    constructor() public {
        owner = msg.sender;
    }

    function createHolographicData(uint256 id, string memory name, string memory description) public {
        HolographicDataStorage memory holographicDataInstance = HolographicDataStorage(id, name, description, new uint256[](0));
        holographicData[id] = holographicDataInstance;
    }

    function storeHolographicData(uint256 id, uint256[] memory data) public {
        require(holographicData[id].id == id, "Holographic data not found");
        holographicData[id].store(data);
    }

    function retrieveHolographicData(uint256 id) public view returns (uint256[] memory) {
        HolographicDataStorage memory holographicDataInstance = holographicData[id];
        return holographicDataInstance.retrieve();
    }
}
