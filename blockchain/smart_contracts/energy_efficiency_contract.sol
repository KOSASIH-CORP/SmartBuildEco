pragma solidity ^0.8.0;

contract EnergyEfficiencyContract {
    address private owner;
    uint public energyConsumption;

    constructor() public {
        owner = msg.sender;
    }

    function setEnergyConsumption(uint _consumption) public {
        require(msg.sender == owner, "Only the owner can set the energy consumption");
        energyConsumption = _consumption;
    }

    function getEnergyConsumption() public view returns (uint) {
        return energyConsumption;
    }
}
