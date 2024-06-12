import httpx
import json
import asyncio
import time
from colorama import Fore, Style, init
import os
import datetime
from dotenv import load_dotenv

init()
load_dotenv() 

def parsingURiandSplit(uri):
    replacedulu = uri.replace("tgWebAppData=", "").replace("%3D", "=").replace("%257B", "{").replace("%2522", '''\\"''').replace("%253A", ":").replace("%252C", ",").replace("%257D", "}").replace("%26", "&")
    splitkan = replacedulu.split("&tgWebAppPlatform")
    return splitkan[0].replace("\\", "")

async def getAccountInfo(session, token):
    url = "https://api.yescoin.gold/account/getAccountInfo"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.get(url, headers=headers)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getAccountInfo, HTTP Error, try again ... {e}")
            continue

async def getAccountBuildInfo(session, token):
    url = "https://api.yescoin.gold/build/getAccountBuildInfo"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.get(url, headers=headers)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getAccountBuildInfo, HTTP Error, try again ... {e}")
            continue

# 
async def getGameInfo(session, token):
    url = "https://api.yescoin.gold/game/getGameInfo"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.get(url, headers=headers)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getGameInfo, HTTP Error, try again ... {e}")
            continue

async def getCommonTaskList(session, token):
    url = "https://api.yescoin.gold/task/getCommonTaskList"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.get(url, headers=headers)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to getCommonTaskList, HTTP Error, try again ... {e}")
            continue

async def claimCoin(session, token, cointoclaim):
    url = "https://api.yescoin.gold/game/collectCoin"

    payload = json.dumps(cointoclaim-10)

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.post(url, headers=headers, data=payload)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimCoin, HTTP Error, try again ... {e}")
            continue

async def claimOffline(session, token):
    url = "https://api.yescoin.gold/user/offline"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiI2NjkzNTY4Njg4IiwiY2hhdElkIjoiNjY5MzU2ODY4OCIsImlhdCI6MTcxNzU5MDExMCwiZXhwIjoxNzIwMTgyMTEwLCJyb2xlQXV0aG9yaXplcyI6W10sInVzZXJJZCI6MTc5MjE5MDkzMzQwNzQ2OTU2OH0.gfwz6xp9cItO0GSZsniyHDEgSUYDnA9s0A8LmO0o-F1Z-hEErQeRS5z1Uly3vJZc4VWlNvTat7s3ClzSPDQqOA',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.post(url, headers=headers)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimOffline, HTTP Error, try again ... {e}")
            continue

async def claimRecovery(session, token):
    url = "https://api.yescoin.gold/game/recoverCoinPool"

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-length': '0',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.post(url, headers=headers)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimRecovery, HTTP Error, try again ... {e}")
            continue

async def upgradeBoost(session, token, id):
    url = "https://api.yescoin.gold/build/levelUp"

    payload = json.dumps(id)
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.post(url, headers=headers, data=payload)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimRecovery, HTTP Error, try again ... {e}")
            continue

async def createToken(session, query):
    url = "https://api.yescoin.gold/user/login"

    payload = json.dumps({
        "code": f"{query}"
    })

    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': "",
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.post(url, headers=headers, data=payload)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to refreshToken, HTTP Error, try again ... {e}")
            continue

async def claimTask(session, token, idtask):
    url = "https://api.yescoin.gold/task/finishTask"

    payload = json.dumps(idtask)
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'origin': 'https://www.yescoin.gold',
        'priority': 'u=1, i',
        'referer': 'https://www.yescoin.gold/',
        'sec-ch-ua': '"Microsoft Edge";v="125", "Chromium";v="125", "Not.A/Brand";v="24", "Microsoft Edge WebView2";v="125"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'token': f'{token}',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0'
    }

    while True:
        try:
            res = await session.post(url, headers=headers, data=payload)

            if res.status_code == 200:
                # print(res.json())
                return res.json()
            else:
                continue
        except httpx.HTTPError as e:
            print(f"Error to claimTask, HTTP Error, try again ... {e}")
            continue

async def runCreateToken():
    async with httpx.AsyncClient() as session:
        try:
            with open('querydata.txt', 'r') as tf:
                querys = tf.readlines()
                for i in range(len(querys)):
                    # print(querys[i].strip())
                    queryURI = querys[i].strip()
                    query = parsingURiandSplit(queryURI)
                    # print(query)
                    token_new = await createToken(session, query)
                    
                    querys[i] = f"{token_new['data']['token']}\n"

                    with open('tokens.txt', 'w+') as tf:
                        tf.writelines(querys)
        except FileNotFoundError:
            print("Fill the querydata.txt first!")
            qf = open('querydata.txt', 'w')
            qf.write("query1\nquery2\ndst")
            qf.close
            exit()

async def runAll(token):
    async with httpx.AsyncClient(timeout=60) as session:
        account = await getAccountInfo(session, token)
        boost = await getAccountBuildInfo(session, token)
        game_info = await getGameInfo(session, token)
        tasks_list = await getCommonTaskList(session, token)
        cointoclaim = round((game_info['data']['coinPoolLeftCount']/10)) # Satuannya 10:1 coin
        claim = await claimCoin(session, token, int(os.getenv("COIN_PER_CLAIM")))
        await claimOffline(session, token)
        current_amounts = account['data']['currentAmount']
        
        status_upgrade = "-"
        if os.getenv("AUTO_UPGRADE") == "yes" or os.getenv("AUTO_UPGRADE") == "y":
            if current_amounts > boost['data']['singleCoinUpgradeCost'] or current_amounts > boost['data']['coinPoolRecoveryUpgradeCost'] or current_amounts > boost['data']['coinPoolTotalUpgradeCost'] or current_amounts > boost['data']['swipeBotUpgradeCost']:
                status_upgrade = f"{Fore.GREEN}Upgrading{Style.RESET_ALL}"
                for i in range(1,5):
                    await upgradeBoost(session, token, i)
            else:
                status_upgrade = f"{Fore.YELLOW}Waiting{Style.RESET_ALL}"
        else:
            status_upgrade = "Off"

        status_task = "-"
        if os.getenv("AUTO_TASKS") == "yes" or os.getenv("AUTO_TASKS") == "y":
            for task in tasks_list['data']:
                # print(task['taskId'])
                idtask = task['taskId']
                tasks = await claimTask(session, token, idtask)
                if tasks['message'] == "task already finish":
                    status_task = f"{Fore.GREEN}Finish{Style.RESET_ALL}"
                else:
                    status_task = f"{Fore.YELLOW}{tasks['message']}{Style.RESET_ALL}"
        else:
            status_task = "Off"

        if boost['data']['coinPoolLeftRecoveryCount'] > 0 and cointoclaim < 100:
            await claimRecovery(session, token)
            game_info = await getGameInfo(session, token)
            # cointoclaim = round((game_info['data']['coinPoolLeftCount']/10) - 100) # Satuannya 10:1 coin
            claim = await claimCoin(session, token, int(os.getenv("COIN_PER_CLAIM")))

        # Printed out status
        acc_id = f"{account['data']['userId']}"
        lvl_acc = f"{account['data']['userLevel']}"
        rank_acc = f"{account['data']['rank']}"
        bal_acc = f"{account['data']['currentAmount']}"

        recovery_bal = "-"
        if boost['data']['coinPoolLeftRecoveryCount'] > 0:
            recovery_bal = f"{Fore.GREEN}{boost['data']['coinPoolLeftRecoveryCount']}{Style.RESET_ALL}"
        else:
            recovery_bal = f"{Fore.RED}{boost['data']['coinPoolLeftRecoveryCount']}{Style.RESET_ALL}"

        status_claim = "-"
        if claim['message'] == "Success":
            status_claim = f"{Fore.GREEN}{claim['message']}{Style.RESET_ALL}"
        else:
            status_claim = f"{Fore.YELLOW}Error to claim{Style.RESET_ALL}"

        print(f"[{acc_id}] | Level : {lvl_acc} | Rank : {rank_acc} | Balance : {Fore.GREEN}{bal_acc}{Style.RESET_ALL} | Coin available : {Fore.YELLOW}{str(cointoclaim)}{Style.RESET_ALL} | Recovery : {recovery_bal} | Auto upgrade : {status_upgrade} | Tasks : {status_task} | Claim : {status_claim}") 

async def runRefreshToken():
   async with httpx.AsyncClient(timeout=60) as session:
        with open('querydata.txt', 'r') as tf:
            querys = tf.readlines()
            for i in range(len(querys)):
                # print(querys[i].strip())
                queryURI = querys[i].strip()
                query = parsingURiandSplit(queryURI)
                # print(query)
                token_new = await createToken(session, query)
                
                querys[i] = f"{token_new['data']['token']}\n"

                with open('tokens.txt', 'w') as tf:
                    tf.writelines(querys)

async def main():
    # token = ""
    os.system('cls') # remove the printed
    
    print("Create new tokens started!")
    await runCreateToken()
    print("Create new tokens success!")

    sekarang = time.time()
    nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))

    while sekarang < nanti:
        print("""
                           _         _           _   
 _   _  ___  ___  ___ ___ (_)_ __   | |__   ___ | |_ 
| | | |/ _ \/ __|/ __/ _ \| | '_ \  | '_ \ / _ \| __|
| |_| |  __/\__ \ (_| (_) | | | | | | |_) | (_) | |_ 
 \__, |\___||___/\___\___/|_|_| |_| |_.__/ \___/ \__|
 |___/                                                                                                
              """)
        start = time.time()
        schedules = []
        with open('tokens.txt', 'r') as tf:
            tokens = tf.readlines()
            for i in range(len(tokens)):
                # print(tokens[i].strip())
                token = tokens[i].strip()
                schedules.append(asyncio.create_task(runAll(token)))

        # gather to run concurently
        await asyncio.gather(*schedules) # BOOOMMMM TO RUN

        print("")
        finish = time.time()-start
        #################### CHANGE THE REFRESH HERE ####################
        claim_remaining = int(os.getenv("REFRESH_CLAIM")) # set to 2 menit or 120 seconds
        refresh_token_at = datetime.datetime.fromtimestamp(nanti).strftime("%H:%M:%S")
        ###############################################################

        while claim_remaining:
            hour, secs = divmod(claim_remaining, 60) 
            timer = '{:02d}'.format(secs) 
            print(f"Execution time : {Fore.YELLOW}{round(finish, 2)}{Style.RESET_ALL} seconds | Refresh tokens after : {Fore.YELLOW}{refresh_token_at}{Style.RESET_ALL} | Refresh after : {Fore.YELLOW}{timer}{Style.RESET_ALL} seconds", end="\r")
            time.sleep(1) 
            claim_remaining -= 1
    
        sekarang = time.time() + int(os.getenv("REFRESH_CLAIM"))
        if sekarang >= nanti:
            print("")
            print("Refresh tokens started!")
            await runRefreshToken()
            print("Refresh tokens success!")
            time.sleep(2)
            nanti = time.time() + int(os.getenv("REFRESH_TOKEN"))
            
        os.system('cls') # remove the printed 

if __name__ == "__main__":
    asyncio.run(main())