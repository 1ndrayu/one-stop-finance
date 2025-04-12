// frontend/config.js

export const ContractAddress = "0xYourContractAddress"; // Replace with your deployed contract address

export const abi = [
  // Replace with your smart contract ABI
  {
    "inputs": [
      {
        "internalType": "string",
        "name": "_name",
        "type": "string"
      },
      {
        "internalType": "string",
        "name": "_assetType",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "_value",
        "type": "uint256"
      },
      {
        "internalType": "string",
        "name": "_metadataURI",
        "type": "string"
      },
      {
        "internalType": "uint256",
        "name": "_totalTokens",
        "type": "uint256"
      }
    ],
    "name": "tokenizeAsset",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "_owner",
        "type": "address"
      }
    ],
    "name": "getUserTokens",
    "outputs": [
      {
        "internalType": "tuple[]",
        "components": [
          {
            "internalType": "uint256",
            "name": "assetId",
            "type": "uint256"
          },
          {
            "internalType": "uint256",
            "name": "value",
            "type": "uint256"
          }
        ],
        "name": "",
        "type": "tuple[]"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
  // Add more ABI entries as needed for additional contract functions
];
