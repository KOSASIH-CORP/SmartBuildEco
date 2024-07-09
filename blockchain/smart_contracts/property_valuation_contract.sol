pragma solidity ^0.8.0;

contract PropertyValuationContract {
    address private owner;
    uint public propertyValue;

    constructor() public {
        owner = msg.sender;
    }

    function setValue(uint _value) public {
        require(msg.sender == owner, "Only the owner can set the value");
        propertyValue = _value;
    }

    function getValue() public view returns (uint) {
        return propertyValue;
    }
}
