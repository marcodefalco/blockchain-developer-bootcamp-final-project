
settings = {
  name: 'Blockgems NFT collection',
  symbol: 'bGEM',
  _initBaseURI: 'https://replaceme'

}

const BlockgemsNFTcollection = artifacts.require("BlockgemsNFTCollection");

module.exports = function (deployer) {
  deployer.deploy(BlockgemsNFTcollection, settings.name, settings.symbol, settings._initBaseURI);
};
