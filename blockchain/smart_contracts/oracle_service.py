pragma solidity ^0.8.0;

contract OracleService {
    address private owner;
    mapping (string => uint256) public data;

    constructor() public {
        owner = msg.sender;
    }

    function updateData(string memory key, uint256 value) public {
        require(msg.sender == owner, "Only the owner can update data");
        data[key] = value;
    }

    function getData(string memory key) public view returns (uint256) {
        return data[key];
    }
}
