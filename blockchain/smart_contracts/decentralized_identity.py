pragma solidity ^0.8.0;

import "https://github.com/uport-project/uport-identity-solidity/contracts/Identity.sol";

contract DecentralizedIdentity {
    address private owner;
    mapping (address => Identity) public identities;

    constructor() public {
        owner = msg.sender;
    }

    function createIdentity(string memory name, string memory email) public {
        Identity memory identity = Identity(name, email);
        identities[msg.sender] = identity;
    }

    function updateIdentity(string memory name, string memory email) public {
        require(identities[msg.sender] != 0, "Identity not found");
        identities[msg.sender].name = name;
        identities[msg.sender].email = email;
    }

    function getIdentity(address account) public view returns (Identity) {
        return identities[account];
    }
}
