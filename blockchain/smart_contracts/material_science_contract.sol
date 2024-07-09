pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";

contract MaterialScienceContract {
    address private owner;
    mapping (address => uint256) public materialProperties;

    constructor() public {
        owner = msg.sender;
    }

    function setProperty(address _material, uint256 _property) public {
        require(msg.sender == owner, "Only the owner can set the property");
        materialProperties[_material] = _property;
    }

    function getProperty(address _material) public view returns (uint256) {
        return materialProperties[_material];
    }
}
