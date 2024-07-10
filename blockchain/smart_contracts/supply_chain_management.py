pragma solidity ^0.8.0;

contract SupplyChainManagement {
    address private owner;
    mapping (uint256 => Product) public products;

    struct Product {
        uint256 id;
        string name;
        string description;
        uint256 quantity;
        address manufacturer;
        address[] distributors;
    }

    constructor() public {
        owner = msg.sender;
    }

    function createProduct(uint256 id, string memory name, string memory description, uint256 quantity) public {
        Product memory product = Product(id, name, description, quantity, msg.sender, new address[](0));
        products[id] = product;
    }

    function addDistributor(uint256 id, address distributor) public {
        require(products[id].manufacturer == msg.sender, "Only the manufacturer can add distributors");
        products[id].distributors.push(distributor);
    }

    function trackProduct(uint256 id) public view returns (Product) {
        return products[id];
    }
}
