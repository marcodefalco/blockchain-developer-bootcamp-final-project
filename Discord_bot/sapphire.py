TOKEN = 'ODk2MzY3OTg2ODg4MjgyMTIz.YWGFvQ.8mzkJKmlVmMArdPNCWpK5oOyJ4Q'
import discord
from discord.ext import commands
import random
import requests 
import datetime
from zipfile import ZipFile
import os


import plotly.graph_objects as go
#import datapane as dp
import matplotlib.pyplot as plt
plt.style.use('dark_background')


import json

import pandas as pd
client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    
meka_mini = pd.read_csv('meka_mini.csv')
meka_mini['token_id'] = meka_mini['token_id'].astype(str)

coolcats_mini = pd.read_csv('coolcats_mini.csv')
coolcats_mini['token_id'] = coolcats_mini['token_id'].astype(str)

@client.event 
async def  on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message =} ({channel})')

    if message.author == client.user:
        return


    #if message.channel.name == 'bot-commands' or  message.channel.name == '⭐-general':
    if user_message.lower() == '!hello':
        await message.channel.send(f'Hello {username}')
        return 
    elif username.lower() == 'bye':
        await message.channel.send(f'See you later {username}')
        return

    elif user_message.lower() == '!random':
        response = f'This is your random number: {random.randrange(100000)}'
        await message.channel.send(response)
        return
    elif message.content.startswith('!lastsales'):
        collect = message.content[11:]
        df_list = []
        offset = 0
        while offset < 100:
            url = "https://api.opensea.io/api/v1/events?asset_contract_address="+ str(collect) +"&event_type=successful&only_opensea=false&offset="+ str(offset)+"&limit=50"

            headers = {"Accept": "application/json"}

            response = requests.request("GET", url, headers=headers)
            response = response.json()
            df = pd.json_normalize(response,['asset_events'], errors = 'ignore')
            df_list.append(df)
            offset += 50

        df = pd.concat(df_list).reset_index(drop=True)
        name = str(df.loc[0]['asset.asset_contract.name'])
        #df['total_price'] = df['total_price'].astype(float) / 10**18
        df['calc_price'] = (df['total_price'].astype(float) / 10**18) * df['payment_token.eth_price'].astype(float)


        df['created_date'] = pd.to_datetime(df['created_date'], infer_datetime_format=True)
        plt.plot( 'created_date', 'calc_price', data=df, linestyle='none', marker='o', alpha=.4,markeredgewidth=1, c = '#7c75f0', ms=5.5)
        plt.title(f'Latest 100 transactions for the {name} collection')
        plt.grid(alpha = .4, c = '#7c75f0')
        plt.xlabel('Date/Time')
        plt.ylabel('Price in Eth')
        plt.tick_params(axis="x", rotation=20, labelsize = 9)
        plt.savefig('my_plot.jpg', bbox_inches='tight')
        plt.close("all") 
        await message.channel.send(file=discord.File('my_plot.jpg'))
        # await message.channel.send('Join YOU HEARD IT HERE FIRST 👉 https://discord.gg/m4GAzC7R ')
        return

    elif message.content.startswith('!hourlystats'):
        collect = message.content[13:]
        df_list = []
        offset = 0
        while offset < 100:
            url = "https://api.opensea.io/api/v1/events?asset_contract_address="+ str(collect) +"&event_type=successful&only_opensea=false&offset="+ str(offset)+"&limit=50"

            headers = {"Accept": "application/json"}

            response = requests.request("GET", url, headers=headers)
            response = response.json()
            df_each = pd.json_normalize(response,['asset_events'], errors = 'ignore')
            df_list.append(df_each) 
            offset += 50

        df_all = pd.concat(df_list).reset_index(drop=True)
        

        name = str(df_all.loc[0]['asset.asset_contract.name'])
        #df['total_price'] = df['total_price'].astype(float) / 10**18
        df_all['calc_price'] = (df_all['total_price'].astype(float) / 10**18) * df_all['payment_token.eth_price'].astype(float)
        df_all = df_all[['calc_price', 'created_date']]

        df_all['created_date'] = pd.to_datetime(df_all['created_date'], infer_datetime_format=True)
        df_min = df_all.set_index('created_date').groupby(pd.Grouper(freq='h')).min().reset_index(drop=False)
        df_max = df_all.set_index('created_date').groupby(pd.Grouper(freq='h')).max().reset_index(drop=False)
        df_median = df_all.set_index('created_date').groupby(pd.Grouper(freq='h')).median().reset_index(drop=False)
    
        plt.plot( 'created_date', 'calc_price', data=df_median, linestyle='none', marker='D', alpha=.4,markeredgewidth=1, c = '#7c75f0', ms=5.5)
        plt.plot( 'created_date', 'calc_price', data=df_max, linestyle='none', marker='^', alpha=.4,markeredgewidth=1, c = '#7c75f0', ms=5.5)
        plt.plot( 'created_date', 'calc_price', data=df_min, linestyle='none', marker='v', alpha=.4,markeredgewidth=1, c = '#7c75f0', ms=5.5)
        plt.title(f'Hourly Min, Median and Max prices \n for the latest 100 txs in the {name} collection')
        plt.grid(alpha = .4, c = '#7c75f0')
        plt.xlabel('Date/Time')
        plt.ylabel('Price in Eth')
        plt.tick_params(axis="x", rotation=20, labelsize = 9)
        plt.savefig('my_plot.jpg', bbox_inches='tight')
        plt.close("all") 
        await message.channel.send(file=discord.File('my_plot.jpg'))
        # await message.channel.send('Join YOU HEARD IT HERE FIRST 👉 https://discord.gg/m4GAzC7R ')
        return   

    elif message.content.startswith('!listings'):
        collect = message.content[10:]
        df_list = []
        offset = 0
        while offset < 100:
            url = "https://api.opensea.io/api/v1/events?asset_contract_address="+ str(collect) +"&event_type=created&only_opensea=false&offset="+ str(offset)+"&limit=50"

            headers = {"Accept": "application/json"}

            response = requests.request("GET", url, headers=headers)
            response = response.json()
            df_each = pd.json_normalize(response,['asset_events'], errors = 'ignore')
            df_list.append(df_each)
            offset += 50

        df_all = pd.concat(df_list).reset_index(drop=True)
        

        name = str(df_all.loc[0]['asset.asset_contract.name'])
        #df['total_price'] = df['total_price'].astype(float) / 10**18
        df_all['calc_price'] = (df_all['ending_price'].astype(float) / 10**18) * df_all['payment_token.eth_price'].astype(float)
        df_all = df_all[['calc_price', 'created_date']]

        df_all['created_date'] = pd.to_datetime(df_all['created_date'], infer_datetime_format=True)
        df_min = df_all.set_index('created_date').groupby(pd.Grouper(freq='30min')).min().reset_index(drop=False)
        #df_max = df_all.set_index('created_date').groupby(pd.Grouper(freq='h')).max().reset_index(drop=False)
        df_median = df_all.set_index('created_date').groupby(pd.Grouper(freq='30min')).median().reset_index(drop=False)
    
        plt.plot( 'created_date', 'calc_price', data=df_median, linestyle='none', marker='D', alpha=.75,markeredgewidth=1, c = '#579dff', ms=4.5)
        #plt.plot( 'created_date', 'calc_price', data=df_max, linestyle='none', marker='^', alpha=.4,markeredgewidth=1, c = '#7c75f0', ms=5.5)
        plt.plot( 'created_date', 'calc_price', data=df_min, linestyle='none', marker='v', alpha=.75,markeredgewidth=1, c = '#7c75f0', ms=5.5)
        plt.title(f'Tracking the floor and median listing price \nIn the {name} collection (30min interval)')
        plt.grid(alpha = .4, c = '#7c75f0')
        plt.xlabel('Date/Time (Timezone: UTC)')
        plt.ylabel('Price in Eth')
        plt.tick_params(axis="x", rotation=20, labelsize = 9)
        plt.savefig('my_plot.jpg', bbox_inches='tight')
        plt.close("all") 
        await message.channel.send(file=discord.File('my_plot.jpg'))
        # await message.channel.send('Join YOU HEARD IT HERE FIRST 👉 https://discord.gg/m4GAzC7R ')
        return  
    elif message.content.startswith('!xraylistings'):
        collect = message.content[14:]
        df_list = []
        offset = 0
        while offset < 100:
            url = "https://api.opensea.io/api/v1/events?asset_contract_address="+ str(collect) +"&event_type=created&only_opensea=false&offset="+ str(offset)+"&limit=50"

            headers = {"Accept": "application/json"}

            response = requests.request("GET", url, headers=headers)
            response = response.json()
            df = pd.json_normalize(response,['asset_events'], errors = 'ignore')
            df_list.append(df)
            offset += 50

        df = pd.concat(df_list).reset_index(drop=True)
        name = str(df.loc[0]['asset.asset_contract.name'])
        #df['total_price'] = df['total_price'].astype(float) / 10**18
        df['calc_price'] = (df['ending_price'].astype(float) / 10**18) * df['payment_token.eth_price'].astype(float)


        df['created_date'] = pd.to_datetime(df['created_date'], infer_datetime_format=True)
        plt.plot( 'created_date', 'calc_price', data=df, linestyle='none', marker='o', alpha=.4,markeredgewidth=1, c = '#7c75f0', ms=5.5)
        plt.title(f'Latest 100 listings for the {name} collection')
        plt.grid(alpha = .4, c = '#7c75f0')
        plt.xlabel('Date/Time (Timezone: UTC')
        plt.ylabel('Price in Eth')
        plt.tick_params(axis="x", rotation=20, labelsize = 9)
        plt.savefig('my_plot.jpg', bbox_inches='tight')
        plt.close("all") 
        await message.channel.send(file=discord.File('my_plot.jpg'))
        # await message.channel.send('Join YOU HEARD IT HERE FIRST 👉 https://discord.gg/m4GAzC7R ')
        return
    

    elif message.content.startswith('!mekaverse'):
        ct = datetime.datetime.utcnow()
        df_tx_list = []
        offset_tx = 0
        while offset_tx < 100:
            url = "https://api.opensea.io/api/v1/events?asset_contract_address=0x9a534628b4062e123ce7ee2222ec20b86e16ca8f&event_type=successful&only_opensea=false&offset="+ str(offset_tx)+"&limit=50"

            headers = {"Accept": "application/json"}

            response = requests.request("GET", url, headers=headers)
            response = response.json()
            df = pd.json_normalize(response,['asset_events'], errors = 'ignore')
            df_tx_list.append(df)
            offset_tx += 50

        df_tx = pd.concat(df_tx_list).reset_index(drop=True)
        #df['total_price'] = df['total_price'].astype(float) / 10**18
        df_tx['calc_price'] = (df_tx['total_price'].astype(float) / 10**18) * df_tx['payment_token.eth_price'].astype(float)
        df_tx['created_date'] = pd.to_datetime(df_tx['created_date'], infer_datetime_format=True)
        df_tx['asset.token_id'] = df_tx['asset.token_id'].astype(str)
        #Now, for the listings:

        df_ls_list = []
        offset_ls = 0
        while offset_ls < 100:
            url = "https://api.opensea.io/api/v1/events?asset_contract_address=0x9a534628b4062e123ce7ee2222ec20b86e16ca8f&event_type=created&only_opensea=false&offset="+ str(offset_ls)+"&limit=50"

            headers = {"Accept": "application/json"}

            response1 = requests.request("GET", url, headers=headers)
            #print(response1)
            response1 = response1.json()
            df = pd.json_normalize(response1,['asset_events'], errors = 'ignore')
            df_ls_list.append(df)
            offset_ls += 50

        df_ls = pd.concat(df_ls_list).reset_index(drop=True)
        #df['total_price'] = df['total_price'].astype(float) / 10**18
        df_ls['calc_price'] = (df_ls['ending_price'].astype(float) / 10**18) * df_ls['payment_token.eth_price'].astype(float)
        df_ls['created_date'] = pd.to_datetime(df_ls['created_date'], infer_datetime_format=True)
        df_ls['asset.token_id'] = df_ls['asset.token_id'].astype(str)


        merged_ls = meka_mini.merge(df_ls, how='inner', left_on='token_id', right_on = 'asset.token_id')
        merged_tx = meka_mini.merge(df_tx, how='inner', left_on='token_id', right_on = 'asset.token_id')

        merged_ls.drop_duplicates(subset=['token_id'], keep = 'last', inplace = True)
        merged_tx.drop_duplicates(subset=['token_id'], keep = 'last', inplace = True)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
                x=merged_ls['rarity_score'],
                y=merged_ls['calc_price'], mode = 'markers', name = 'listing price', 
                hovertext=merged_ls['asset.token_id']))

        fig.add_trace(go.Scatter(
                x=merged_tx['rarity_score'],
                y=merged_tx['calc_price'], mode = 'markers', name = 'tx price',
                hovertext=merged_tx['asset.token_id']))


        fig.update_layout(title=f'Last 150 transactions and listings for MekaVerse at UTC: {ct}',
                        xaxis_title="Rarity Score",
                        yaxis_title="Price in ETH",)

        dp.Report(
            dp.Plot(fig)
        ).save(path="meka.html")
        await message.channel.send(file=discord.File('meka.html'))
        return
    elif message.content.startswith('!coolcats'):
        ct = datetime.datetime.utcnow()

        df_tx_list = []
        offset_tx = 0
        while offset_tx < 100:
            url = "https://api.opensea.io/api/v1/events?asset_contract_address=0x1a92f7381b9f03921564a437210bb9396471050c&event_type=successful&only_opensea=false&offset="+ str(offset_tx)+"&limit=50"

            headers = {"Accept": "application/json"}

            response = requests.request("GET", url, headers=headers)
            response = response.json()
            df = pd.json_normalize(response,['asset_events'], errors = 'ignore')
            df_tx_list.append(df)
            offset_tx += 50

        df_tx = pd.concat(df_tx_list).reset_index(drop=True)
        #df['total_price'] = df['total_price'].astype(float) / 10**18
        df_tx['calc_price'] = (df_tx['total_price'].astype(float) / 10**18) * df_tx['payment_token.eth_price'].astype(float)
        df_tx['created_date'] = pd.to_datetime(df_tx['created_date'], infer_datetime_format=True)
        df_tx['asset.token_id'] = df_tx['asset.token_id'].astype(str)
        #Now, for the listings:

        df_ls_list = []
        offset_ls = 0
        while offset_ls < 100:
            url = "https://api.opensea.io/api/v1/events?asset_contract_address=0x1a92f7381b9f03921564a437210bb9396471050c&event_type=created&only_opensea=false&offset="+ str(offset_ls)+"&limit=50"

            headers = {"Accept": "application/json"}

            response1 = requests.request("GET", url, headers=headers)
            #print(response1)
            response1 = response1.json()
            df = pd.json_normalize(response1,['asset_events'], errors = 'ignore')
            df_ls_list.append(df)
            offset_ls += 50

        df_ls = pd.concat(df_ls_list).reset_index(drop=True)
        #df['total_price'] = df['total_price'].astype(float) / 10**18
        df_ls['calc_price'] = (df_ls['ending_price'].astype(float) / 10**18) * df_ls['payment_token.eth_price'].astype(float)
        df_ls['created_date'] = pd.to_datetime(df_ls['created_date'], infer_datetime_format=True)
        df_ls['asset.token_id'] = df_ls['asset.token_id'].astype(str)

        #here you insert the rarities:
        merged_ls = coolcats_mini.merge(df_ls, how='inner', left_on='token_id', right_on = 'asset.token_id')
        merged_tx = coolcats_mini.merge(df_tx, how='inner', left_on='token_id', right_on = 'asset.token_id')

        merged_ls.drop_duplicates(subset=['token_id'], keep = 'last', inplace = True)
        merged_tx.drop_duplicates(subset=['token_id'], keep = 'last', inplace = True)

        fig = go.Figure()

        fig.add_trace(go.Scatter(
                x=merged_ls['rarity_score'],
                y=merged_ls['calc_price'], mode = 'markers', name = 'listing price', 
                hovertext=merged_ls['asset.token_id']))

        fig.add_trace(go.Scatter(
                x=merged_tx['rarity_score'],
                y=merged_tx['calc_price'], mode = 'markers', name = 'tx price',
                hovertext=merged_tx['asset.token_id']))


        fig.update_layout(title=f'Last 150 transactions and listings for CoolCats at UTC: {ct}',
                        xaxis_title="Rarity Score",
                        yaxis_title="Price in ETH",)

        fig.write_html("coolcats.html")
        await message.channel.send(file=discord.File('coolcats.html'))
        #await message.channel.send('https://www.pythonanywhere.com/user/BlockGems/files/home/BlockGems/coolcats.html')
        return
    elif message.content.startswith('!sendcoolcats'):
        await message.channel.send(file=discord.File('coolcats.html'))
        return



client.run(TOKEN)       