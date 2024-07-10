pragma solidity ^0.8.0;

import "https://github.com/erc725-solidity/contracts/ERC725Identity.sol";

contract ERC725Identity {
    address private owner;
    mapping (uint256 => ERC725Identity) public identities;

    constructor() public {
        owner = msg.sender;
    }

    function createIdentity(uint256 id, string memory name, string memory description) public {
        ERC725Identity memory identityInstance = ERC725Identity(id, name, description, new uint256[](0));
        identities[id] = identityInstance;
    }

    function updateIdentityAttributes(uint256 id, uint256[] memory attributes) public {
        require(identities[id].id == id, "Identity not found");
        identities[id].updateAttributes(attributes);
    }

    function authenticateIdentity(uint256 id, uint256[] memory authenticationData) public view returns (bool) {
        ERC725Identity memory identityInstance = identities[id];
        return identityInstance.authenticate(authenticationData);
    }
}
