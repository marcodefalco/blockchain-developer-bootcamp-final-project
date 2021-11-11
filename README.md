# blockchain-developer-bootcamp-final-project

# Project Name: BlockGems NFT club (provisional)

## Background:

The NFT space is still very opaque when it comes to data visibility. On Opensea, users can access average prices and volumes, but there is a lack of information for many other metrics that would still be of extreme value to the educated NFT investor who aims to act rationally rather than go after the hype for a project.
Much of the so called alpha is discussed on Discord, specifically in those communities that are centered around NFTs. Hence the need to pull charts within a Discord community to show important project metrics, e.g. Distribution of a token, Unique ownership rates, floor price, median price etc.

Enter the Blockgems bots. 

Application mechanics:

The First part of the app is a minting app. The user can go on the page and mint one or multiple 'gems'.

To access the analytics service gems will be required in the Discord.

Thanks to the Collab.Land bot (simply a tool used by this project), the users that own gems will be allowed into private channels of that BlockGems Discord community.

In these Channels, they will be able to input commands to summon Sapphire, a Discord bot that will return charts based on the user input.

example: !lastsales 0xbc4ca0eda7647a8ab7c2061c2e118a18a936f13d will return the last transaction chart of the BoredApe Yacht club NFT.

The code for this bot is available within this repo.

## Directory structure:

1. hashlips_art_engine -> art engine to create the generative art. I have not added/ edited any code here.
2. Smart_contract_part -> self explanatory
3. Front_end_base_dapp-main -> self explanatory
4. Discord_bot -> the python script that will return the charts in the Discrod channel

## Frontend Link:

https://blockgems-nft.herokuapp.com/

## My ethereum adress for the NFT certificate:

    0x6a8C69DC2040c1C594Be2F3947e15669536DD59F

## Point 9: In your README.md, be sure to have clear instructions on: 

- Installing dependencies for your project 
For the dapp:you just need node and yarn (to install the dependencies do: yarn add all).

In case you want to check the python bot you need the following list. But you don't have to look at this code as this is just an extra piece I am doing to give a 'meaningful utility' to the token I have created:

import discord
from discord.ext import commands
import random
import requests 
import datetime
from zipfile import ZipFile
import os
import plotly.graph_objects as go
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import json
import pandas as pd

- Accessing or—if your project needs a server (not required)—running your project
You can mint a token using Rinkeby Eth and then use !join in the discord at this link to test the bot in the XYZ channel:

https://discord.gg/bSpzVszJw6

- Running your smart contract unit tests and which port a local testnet should be running on.
Port: HTTP://127.0.0.1:8545
Unit tests:
just run test_BlockgemsNFTCollection.js using the truffle console.

## Screencast link:
https://www.loom.com/share/76fe5318cc49485f88fdaa3be631ce11

