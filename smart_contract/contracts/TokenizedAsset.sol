// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenizedAsset is ERC20, Ownable {
    struct Asset {
        string name;
        string assetType;
        uint256 value;
        string metadataURI;
        uint256 totalTokens;
    }

    mapping(uint256 => Asset) public assets;
    uint256 public assetCount;

    event AssetTokenized(uint256 assetId, string name, uint256 totalTokens, uint256 value);
    event TokensTransferred(uint256 assetId, address from, address to, uint256 amount);

    constructor() ERC20("Tokenized Asset", "TKA") {}

    function tokenizeAsset(
        string memory name,
        string memory assetType,
        uint256 value,
        string memory metadataURI,
        uint256 totalTokens
    ) external onlyOwner returns (uint256) {
        assetCount++;
        assets[assetCount] = Asset(name, assetType, value, metadataURI, totalTokens);
        _mint(msg.sender, totalTokens);
        emit AssetTokenized(assetCount, name, totalTokens, value);
        return assetCount;
    }

    function transferTokens(
        uint256 assetId,
        address to,
        uint256 amount
    ) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to transfer tokens");
        _transfer(msg.sender, to, amount);
        emit TokensTransferred(assetId, msg.sender, to, amount);
    }

    function getAssetDetails(uint256 assetId) external view returns (string memory, string memory, uint256, string memory, uint256) {
        Asset memory asset = assets[assetId];
        return (asset.name, asset.assetType, asset.value, asset.metadataURI, asset.totalTokens);
    }
}
