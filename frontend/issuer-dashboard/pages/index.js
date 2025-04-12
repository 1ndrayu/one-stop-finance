import { useState } from 'react';
import AssetForm from '../components/AssetForm';

export default function Home() {
  return (
    <div className="container">
      <h1>Issuer Dashboard</h1>
      <AssetForm />
    </div>
  );
}
