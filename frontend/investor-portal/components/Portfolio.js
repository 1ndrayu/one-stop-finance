import { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import { ContractAddress, abi } from '../config'; // Replace with your contract ABI and address

export default function Portfolio() {
  const [tokens, setTokens] = useState([]);
  const [account, setAccount] = useState('');

  useEffect(() => {
    const loadPortfolio = async () => {
      if (window.ethereum) {
        const provider = new ethers.providers.Web3Provider(window.ethereum);
        const signer = provider.getSigner();
        const address = await signer.getAddress();
        setAccount(address);

        const contract = new ethers.Contract(ContractAddress, abi, provider);
        const ownedTokens = await contract.getUserTokens(address);
        setTokens(ownedTokens);
      }
    };

    loadPortfolio();
  }, [account]);

  return (
    <div>
      <h2>Your Portfolio</h2>
      <div>
        {tokens.map((token, index) => (
          <div key={index}>
            <h3>Asset ID: {token.assetId}</h3>
            <p>Value: {ethers.utils.formatUnits(token.value, 'ether')} ETH</p>
            <button>Buy</button>
            <button>Sell</button>
          </div>
        ))}
      </div>
    </div>
  );
}
