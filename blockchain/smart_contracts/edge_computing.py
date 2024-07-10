pragma solidity ^0.8.0;

import "https://github.com/edge-computing-solidity/contracts/EdgeNode.sol";

contract EdgeComputing {
    address private owner;
    mapping (uint256 => EdgeNode) public edgeNodes;

    constructor() public {
        owner = msg.sender;
    }

    function createEdgeNode(uint256 id, string memory name, string memory description) public {
        EdgeNode memory edgeNodeInstance = EdgeNode(id, name, description, new uint256[](0));
        edgeNodes[id] = edgeNodeInstance;
    }

    function processEdgeData(uint256 id, uint256[] memory data) public {
        require(edgeNodes[id].id == id, "Edge node not found");
        edgeNodes[id].processData(data);
    }

    function requestEdgeService(uint256 id, uint256[] memory serviceRequest) public {
        EdgeNode memory edgeNodeInstance = edgeNodes[id];
        return edgeNodeInstance.requestService(serviceRequest);
    }
}
