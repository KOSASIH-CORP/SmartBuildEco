pragma solidity ^0.8.0;

import "https://github.com/enjin/enjin-solidity/contracts/ERC1155.sol";

contract BlockchainBasedGaming {
    address private owner;
    mapping (uint256 => GameItem) public gameItems;

    struct GameItem {
        uint256 id;
        string name;
        string description;
        uint256 rarity;
    }

    constructor() public {
        owner = msg.sender;
    }

    function createGameItem(uint256 id, string memory name, string memory description, uint256 rarity) public {
        GameItem memory gameItem = GameItem(id, name, description, rarity);
        gameItems[id] = gameItem;
    }

    function mintGameItem(uint256 id, address player) public {
        require(gameItems[id].id == id, "Game item not found");
        ERC1155.mint(player, id, 1);
    }

    function transferGameItem(uint256 id, address from, address to) public {
        require(gameItems[id].id == id, "Game item not found");
        ERC1155.transfer(from, to, id, 1);
    }
}
