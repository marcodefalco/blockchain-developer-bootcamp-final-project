
settings = {
  name: 'Blockgems NFT collection (Rinkeby)',
  symbol: 'bGEMr',
  _initBaseURI: 'https://replaceme/'

}

const BlockgemsNFTcollection = artifacts.require("BlockgemsNFTCollectionRinkeby");

module.exports = function (deployer) {
  deployer.deploy(BlockgemsNFTcollection, settings.name, settings.symbol, settings._initBaseURI);
};
