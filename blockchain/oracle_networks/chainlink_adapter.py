pragma solidity ^0.8.0;

import "https://github.com/chainlink-solidity/contracts/ChainlinkAdapter.sol";

contract ChainlinkAdapter {
    address private owner;
    mapping (uint256 => ChainlinkAdapter) public adapters;

    constructor() public {
        owner = msg.sender;
    }

    function createAdapter(uint256 id, string memory name, string memory description) public {
        ChainlinkAdapter memory adapterInstance = ChainlinkAdapter(id, name, description, new uint256[](0));
        adapters[id] = adapterInstance;
    }

    function requestExternalData(uint256 id, uint256[] memory requestData) public {
        require(adapters[id].id == id, "Adapter not found");
        adapters[id].requestData(requestData);
    }

    function receiveExternalData(uint256 id, uint256[] memory responseData) public {
        ChainlinkAdapter memory adapterInstance = adapters[id];
        adapterInstance.receiveData(responseData);
    }
}
