pragma solidity ^0.8.0;

import "https://github.com/iotexproject/iotex-iot-solidity/contracts/IoTDevice.sol";

contract InternetOfThings {
    address private owner;
    mapping (uint256 => IoTDevice) public devices;

    constructor() public {
        owner = msg.sender;
    }

    function createDevice(uint256 id, string memory name, string memory description) public {
        IoTDevice memory device = IoTDevice(id, name, description, new uint256[](0));
        devices[id] = device;
    }

    function sendData(uint256 id, uint256[] memory data) public {
        require(devices[id].id == id, "Device not found");
        devices[id].data = data;
    }

    function receiveData(uint256 id) public view returns (uint256[] memory) {
        IoTDevice memory device = devices[id];
        return device.data;
    }
}
