pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";

contract PredictiveMaintenanceContract {
    address private owner;
    mapping (address => uint256) public maintenanceSchedules;

    constructor() public {
        owner = msg.sender;
    }

    function setSchedule(address _device, uint256 _schedule) public {
        require(msg.sender == owner, "Only the owner can set the schedule");
        maintenanceSchedules[_device] = _schedule;
    }

    function getSchedule(address _device) public view returns (uint256) {
        return maintenanceSchedules[_device];
    }
}
