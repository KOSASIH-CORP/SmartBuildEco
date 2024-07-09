pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";

contract BuildingInspectionContract {
    address private owner;
    mapping (address => uint256) public inspectionResults;

    constructor() public {
        owner = msg.sender;
    }

    function setResult(address _building, uint256 _result) public {
        require(msg.sender == owner, "Only the owner can set the result");
        inspectionResults[_building] = _result;
    }

    function getResult(address _building) public view returns (uint256) {
        return inspectionResults[_building];
    }
}
