import { useState } from 'react';
import Web3Modal from 'web3modal';
import { ethers } from 'ethers';

export default function WalletConnectButton() {
  const [account, setAccount] = useState(null);
  const [web3Modal, setWeb3Modal] = useState(null);

  // Initialize Web3Modal on component mount
  useState(() => {
    const modal = new Web3Modal({
      cacheProvider: true,
      providerOptions: {
        walletconnect: {
          package: WalletConnectProvider, // We are using WalletConnect
          options: {
            infuraId: process.env.NEXT_PUBLIC_INFURA_PROJECT_ID, // Use your Infura Project ID
          },
        },
      },
    });
    setWeb3Modal(modal);
  }, []);

  const connectWallet = async () => {
    const connection = await web3Modal.connect();
    const provider = new ethers.providers.Web3Provider(connection);
    const signer = provider.getSigner();
    const address = await signer.getAddress();
    setAccount(address);
  };

  return (
    <div>
      {!account ? (
        <button onClick={connectWallet}>Connect Wallet</button>
      ) : (
        <p>Connected as: {account}</p>
      )}
    </div>
  );
}
