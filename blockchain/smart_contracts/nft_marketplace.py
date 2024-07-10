pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";

contract NFTMarketplace {
    address private owner;
    mapping (address => mapping (uint256 => NFT)) public nftOwners;
    mapping (uint256 => NFT) public nftList;

    struct NFT {
        uint256 id;
        string name;
        string description;
        uint256 price;
    }

    constructor() public {
        owner = msg.sender;
    }

    function createNFT(uint256 id, string memory name, string memory description, uint256 price) public {
        NFT memory nft = NFT(id, name, description, price);
        nftList[id] = nft;
        nftOwners[msg.sender][id] = nft;
    }

    function buyNFT(uint256 id) public payable {
        require(nftList[id].price <= msg.value, "Insufficient funds");
        nftOwners[msg.sender][id] = nftList[id];
        nftList[id].owner = msg.sender;
    }
}
