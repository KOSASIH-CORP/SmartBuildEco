pragma solidity ^0.8.0;

contract OracleNetwork {
    address[] public nodes;
    mapping (address => uint256) public nodeBalances;

    constructor() {
        nodes.push(msg.sender);
        nodeBalances[msg.sender] = 100;
    }

    function addNode(address node) public {
        nodes.push(node);
        nodeBalances[node] = 100;
    }

    function getNodeBalance(address node) public view returns (uint256) {
        return nodeBalances[node];
    }

    function sendTransaction(address from, address to, uint256 amount) public {
        require(nodeBalances[from] >= amount, "Insufficient balance");
        nodeBalances[from] -= amount;
        nodeBalances[to] += amount;
    }
}
