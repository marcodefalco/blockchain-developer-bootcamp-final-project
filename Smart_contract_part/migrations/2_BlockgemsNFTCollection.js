
settings = {
  name: 'Blockgems NFT collection',
  symbol: 'bGEM',
  baseURI: 'https://replaceme'

}

const BlockgemsNFTcollection = artifacts.require("BlockgemsNFTCollection");

module.exports = function (deployer) {
  deployer.deploy(BlockgemsNFTcollection, settings.name, settings.symbol, settings.baseURI);
};
