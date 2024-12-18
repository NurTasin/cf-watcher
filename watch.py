import argparse
import requests as req
import os
import time

def getStatus(handle: str):

    res= req.get(f"https://codeforces.com/api/user.status?handle={handle}").json()
    return res

def getAccepteds(handle: str):
    status = getStatus(handle)
    result = []
    for i in status['result']:
        if i['verdict']=='OK':
            result.append(i)
    return result

argparser = argparse.ArgumentParser(prog="cfwatch")
argparser.add_argument("handle", help="Handle of the user you want to track")

argv = argparser.parse_args()
print(f"Watching user {argv.handle}")
success_res_cnt = len(getAccepteds(argv.handle))
print(f" Success Count : {str(success_res_cnt).ljust(4)}", end="\r")
while True:
    try:
        success_res_cnt_n = len(getAccepteds(argv.handle))
        print(f"Success Count : {str(success_res_cnt_n).ljust(4)}", end="\r")
        if(success_res_cnt_n>success_res_cnt):
            success_res_cnt=success_res_cnt_n
            os.system("ffplay -autoexit -nodisp -loglevel quiet -i .\\aaa.mp3")
        
        time.sleep(15)
    except KeyboardInterrupt:
        print()
        break
