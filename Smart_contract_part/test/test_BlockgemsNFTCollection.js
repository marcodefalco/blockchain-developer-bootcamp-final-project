const BlockgemsNFTcollection = artifacts.require("BlockgemsNFTCollection");

contract("BlockgemsNFTCollection", async accounts => {
  it("should put 1 NFT into the owner's wallet at launch", async () => {
    const instance = await BlockgemsNFTcollection.deployed();
    const balance = await instance.balanceOf(accounts[0]);
    assert.equal(balance.valueOf(), 1);
  });
  it("should pause the minting", async () => {
    const instance = await BlockgemsNFTcollection.deployed();
    const new_state = await instance.pause(false);
    assert.equal(new_state.receipt.status, true);
  });
  it("should unpause the minting", async () => {
    const instance = await BlockgemsNFTcollection.deployed();
    const new_state = await instance.pause(true);
    assert.equal(new_state.receipt.status, true);
  });
  it("should get 'https://replaceme1.json' as a TokenURI for token #1 ", async () => {
    const instance = await BlockgemsNFTcollection.deployed();
    const base_uri = await instance.tokenURI(1);
    assert.equal(base_uri.valueOf(), 'https://replaceme1.json');
  });
  it("should change 'https://replaceme' to 'https://newhosting' as a TokenURI for token #1 ", async () => {
    const instance = await BlockgemsNFTcollection.deployed();
    const new_base_uri = await instance.setBaseURI('https://newhosting');
    assert.equal(new_base_uri.receipt.status, true);
  });


  it("should get 'https://newhosting1.json' as a TokenURI for token #1 ", async () => {
    const instance = await BlockgemsNFTcollection.deployed();
    const base_uri = await instance.tokenURI(1);
    assert.equal(base_uri.valueOf(), 'https://newhosting1.json');
  });


  it("should whitelist account 2 ", async () => {
    const instance = await BlockgemsNFTcollection.deployed();
    const new_wl_account = await instance.whitelistUser(accounts[1]);
    assert.equal(new_wl_account.receipt.status, true);;
  });

  it("should confirm that account 2 is on the whitelist ", async () => {
    const instance = await BlockgemsNFTcollection.deployed();
    const wl = await instance.whitelisted(accounts[1]);
    assert.equal(wl, true);
  });

})