pragma solidity ^0.8.0;

import "https://github.com/quantum-resistant-cryptography-solidity/contracts/QuantumResistantCrypto.sol";

contract QuantumResistantCryptography {
    address private owner;
    mapping (uint256 => QuantumResistantCrypto) public cryptoInstances;

    constructor() public {
        owner = msg.sender;
    }

    function createCryptoInstance(uint256 id, string memory name, string memory description) public {
        QuantumResistantCrypto memory cryptoInstance = QuantumResistantCrypto(id, name, description, new uint256[](0));
        cryptoInstances[id] = cryptoInstance;
    }

    function encryptData(uint256 id, uint256[] memory data) public {
        require(cryptoInstances[id].id == id, "Crypto instance not found");
        cryptoInstances[id].encrypt(data);
    }

    function decryptData(uint256 id, uint256[] memory encryptedData) public view returns (uint256[] memory) {
        QuantumResistantCrypto memory cryptoInstance = cryptoInstances[id];
        return cryptoInstance.decrypt(encryptedData);
    }
}
