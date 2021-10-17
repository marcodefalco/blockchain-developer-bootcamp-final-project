# blockchain-developer-bootcamp-final-project

# NFT bragging rights (provisional name)

## Background

In the NFT space, decentralized markets such as Rarible and OpenSea allow you to buy and sell directly using your MetaMask wallet. As all the transactions are recorded on the blockchain, you can prove to the world that you were one of the early adopters/owners of say, BAYC, CryptoPunks, Chromie Squiggles, Fidenza etc. The idea is that people might love to show off that they bought early and sold at the top. Or, if you like different metrics, people might enjoy to show conviction: e.g. they had extreme diamond hands while their NFT was going through a lot of negative volatility and yet recovered later. Another idea could be that a user might want to signal that he or she was an early 'discoverer / believer' into a project that later became big.

I believe it is possible to create a. contests that reward these behavior with monetary prizes or b.  dapps that recognize the value of the above feats with 'badges of honor'.

## Application mechanics:
1. The user connects their wallet to the dapp
2. They will select a contest they want to participate in.
3. They will mint a token for the selected contest (e.g.: 2x on your NFT trade (realized profit) by buying an NFT for x and selling it later for 2x by 12/31/21)
4. All the funds coming from the minting create a prize pool for that given contest.
5. the dapp is able to track the wallet transactions to verify who won the contest.
6. Funds are distributed pro quota to the winning addresses once the contest time is expired.
7. (optional) the Winner addresses are recorded in a public leaderboard for everyone to know.

## (Alternative / MVP) Application mechanics (In case the above turns out too complicated):
1. The user connects their wallet.
2. The app checks their wallet against pre-set parameters, representing interesting achievements (e.g. The address has purchased BAYC below 1 eth (or before a certain date) and never sold so far).
3. After the checks, the app displays the mintable tokens: example: A cool badge that says: ' I bought BAYC before it was cool.'
4. The user can mint the token and own them in their wallet.
