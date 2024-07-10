pragma solidity ^0.8.0;

import "https://github.com/cybersecurity-solidity/contracts/SecureData.sol";

contract Cybersecurity {
    address private owner;
    mapping (uint256 => SecureData) public secureData;

    constructor() public {
        owner = msg.sender;
    }

    function createSecureData(uint256 id, string memory name, string memory description) public {
        SecureData memory secureDataInstance = SecureData(id, name, description, new uint256[](0));
        secureData[id] = secureDataInstance;
    }

    function encryptData(uint256 id, uint256[] memory data) public {
        require(secureData[id].id == id, "Secure data not found");
        secureData[id].encrypt(data);
    }

    function decryptData(uint256 id, uint256[] memory encryptedData) public view returns (uint256[] memory) {
        SecureData memory secureDataInstance = secureData[id];
        return secureDataInstance.decrypt(encryptedData);
    }
}
