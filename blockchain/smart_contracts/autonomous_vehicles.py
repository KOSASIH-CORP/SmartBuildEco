pragma solidity ^0.8.0;

import "https://github.com/autonomous-vehicles-solidity/contracts/Vehicle.sol";

contract AutonomousVehicles {
    address private owner;
    mapping (uint256 => Vehicle) public vehicles;

    constructor() public {
        owner = msg.sender;
    }

    function createVehicle(uint256 id, string memory name, string memory description) public {
        Vehicle memory vehicleInstance = Vehicle(id, name, description, new uint256[](0));
        vehicles[id] = vehicleInstance;
    }

    function updateVehicleSoftware(uint256 id, uint256[] memory softwareUpdate) public {
        require(vehicles[id].id == id, "Vehicle not found");
        vehicles[id].updateSoftware(softwareUpdate);
    }

    function requestVehicleService(uint256 id, uint256[] memory serviceRequest) public {
        Vehicle memory vehicleInstance = vehicles[id];
        return vehicleInstance.requestService(serviceRequest);
    }
}
