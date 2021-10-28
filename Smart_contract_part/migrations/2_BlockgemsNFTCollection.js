
settings = {
  name: 'Blockgems NFT collection',
  symbol: 'bGEM',
  baseURI: 'https://replaceme'

}

const NerdyCoderClones = artifacts.require("BlockgemsNFTCollection");

module.exports = function (deployer) {
  deployer.deploy(BlockgemsNFTCollection, settings.name, settings.symbol, settings.baseURI);
};
