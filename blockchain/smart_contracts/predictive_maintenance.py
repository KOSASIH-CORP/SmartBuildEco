pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

contract PredictiveMaintenance {
    address private owner;
    mapping (uint256 => Machine) public machines;

    struct Machine {
        uint256 id;
        string name;
        uint256[] sensorData;
        uint256 maintenanceThreshold;
    }

    constructor() public {
        owner = msg.sender;
    }

    function createMachine(uint256 id, string memory name, uint256 maintenanceThreshold) public {
        Machine memory machine = Machine(id, name, new uint256[](0), maintenanceThreshold);
        machines[id] = machine;
    }

    function addSensorData(uint256 id, uint256 sensorData) public {
        require(machines[id].id == id, "Machine not found");
        machines[id].sensorData.push(sensorData);
    }

    function predictMaintenance(uint256 id) public view returns (bool) {
        Machine memory machine = machines[id];
        uint256 averageSensorData = SafeMath.div(SafeMath.sum(machine.sensorData), machine.sensorData.length);
        return averageSensorData >= machine.maintenanceThreshold;
    }
}
