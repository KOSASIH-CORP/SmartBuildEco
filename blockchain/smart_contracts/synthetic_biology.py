pragma solidity ^0.8.0;

import "https://github.com/synthetic-biology-solidity/contracts/Genome.sol";

contract SyntheticBiology {
    address private owner;
    mapping (uint256 => Genome) public genomes;

    constructor() public {
        owner = msg.sender;
    }

    function createGenome(uint256 id, string memory name, string memory description) public {
        Genome memory genomeInstance = Genome(id, name, description, new uint256[](0));
        genomes[id] = genomeInstance;
    }

    function designGenome(uint256 id, uint256[] memory designParameters) public {
        require(genomes[id].id == id, "Genome not found");
        genomes[id].design(designParameters);
    }

    function simulateGenomeBehavior(uint256 id, uint256[] memory simulationParameters) public view returns (uint256[] memory) {
        Genome memory genomeInstance = genomes[id];
        return genomeInstance.simulate(simulationParameters);
    }
}
