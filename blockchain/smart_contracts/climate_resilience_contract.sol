pragma solidity ^0.8.0;

contract ClimateResilienceContract {
    address private owner;
    uint public climateResilience;

    constructor() public {
        owner = msg.sender;
    }

    function setClimateResilience(uint _resilience) public {
        require(msg.sender == owner, "Only the owner can set the climate resilience");
        climateResilience = _resilience;
    }

    function getClimateResilience() public view returns (uint) {
        return climateResilience;
    }
}
