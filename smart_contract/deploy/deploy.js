async function main() {
    const [deployer] = await ethers.getSigners();
    console.log("Deploying contracts with the account:", deployer.address);

    const TokenizedAsset = await ethers.getContractFactory("TokenizedAsset");
    const tokenizedAsset = await TokenizedAsset.deploy();
    console.log("TokenizedAsset contract deployed to:", tokenizedAsset.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
