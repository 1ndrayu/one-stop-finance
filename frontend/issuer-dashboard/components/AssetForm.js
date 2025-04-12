import { useState } from 'react';
import { ethers } from 'ethers';
import Web3Modal from 'web3modal';
import { ContractAddress, abi } from '../config'; // Replace with your contract ABI and address

export default function AssetForm() {
  const [name, setName] = useState('');
  const [assetType, setAssetType] = useState('');
  const [value, setValue] = useState('');
  const [metadataURI, setMetadataURI] = useState('');
  const [totalTokens, setTotalTokens] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const web3Modal = new Web3Modal();
    const connection = await web3Modal.connect();
    const provider = new ethers.providers.Web3Provider(connection);
    const signer = provider.getSigner();

    const contract = new ethers.Contract(ContractAddress, abi, signer);

    try {
      const tx = await contract.tokenizeAsset(
        name,
        assetType,
        ethers.utils.parseUnits(value, 'ether'),
        metadataURI,
        totalTokens
      );
      console.log('Transaction sent:', tx);
      await tx.wait();
      alert('Asset tokenized successfully!');
    } catch (error) {
      console.error(error);
      alert('Error tokenizing asset');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <div>
        <label>Asset Name</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />
      </div>
      <div>
        <label>Asset Type</label>
        <input type="text" value={assetType} onChange={(e) => setAssetType(e.target.value)} required />
      </div>
      <div>
        <label>Asset Value (ETH)</label>
        <input type="number" value={value} onChange={(e) => setValue(e.target.value)} required />
      </div>
      <div>
        <label>Metadata URI</label>
        <input type="text" value={metadataURI} onChange={(e) => setMetadataURI(e.target.value)} />
      </div>
      <div>
        <label>Total Tokens</label>
        <input type="number" value={totalTokens} onChange={(e) => setTotalTokens(e.target.value)} required />
      </div>
      <button type="submit">Tokenize Asset</button>
    </form>
  );
}
