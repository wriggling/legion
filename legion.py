import os
from os import system
import random
import time
import requests as r
from colorama import Fore
from pystyle import Colors, Write, Colorate, Center

v = Colors.blue_to_purple
rr = Colors.red_to_yellow
er = Colors.red_to_black
wr = Colors.green_to_white
ff = Colors.yellow_to_red
ii = Colors.blue_to_cyan
tt = Colors.red_to_white
cc = Colors.green_to_white
gg = Colors.yellow_to_green


def clear(): return os.system('cls') if os.name == 'nt' else os.system('clear')
os.system("mode con cols=120 lines=50")

def update_title(sent, deleted, errors):
    """Updates the console title with the latest stats."""
    system(f"title LEGION  ^|  Sent: {sent}  ^|  Deleted: {deleted}  ^|  Errors: {errors}")

def print_header(username, userid, channel_id):
    """Prints the centered ASCII art header."""
    # Use a raw string (r"...") to prevent backslashes from being interpreted as escape sequences.
    legion = """
                                   __                                           __
                                  (**)                                         (**)
                                  IIII                                         IIII
                                  ####                                         ####
                                  HHHH     Madness comes, and madness goes     HHHH
                                  HHHH    An insane place, with insane moves   HHHH
                                  ####   Battles without, for battles within   ####
                               ___IIII___        Where evil lives,          ___IIII___
                            .-`_._"**"_._`-.      and evil rules         .-`_._"**"_._`-.
                           |/``  .`\/`.  ``\|    Breaking them up,      |/``  .`\/`.  ``\|
                           `     }    {     '  just breaking them in    `     }    {     '
                                 ) () (  Quickest way out, quickest way wins  ) () (
                                 ( :: )      Never disclose, never betray     ( :: )
                                 | :: |   Cease to speak or cease to breath   | :: |
                                 | )( |        And when you kill a man,       | )( |
                                 | || |          you're a murderer            | || |
                                 | || |             Kill many                 | || |
                                 | || |        and you're a conqueror         | || |
                                 | || |        Kill them all ... Ooh..        | || |
                                 | || |           Oh you're a God!            | || |
                                 ( () )                       -Vozzy          ( () )
                                  \  /                                         \  /
                                   \/                                           \/

                             #       #        #   # #        #       #       #   #        
                           #  #     #  ##########  #   #    ######## #       #   #        
                            #      #         ##   # # #    #    #           #  ########## 
                                 ##        ## #      #    #    #           #     #     #  
                               ##        ##   #     # #       #          ##      #        
                             ##        ##    ##    #   #     #         ##        #        
                           ##                 #         #   #        ##           ######  

""" 
    info = f"""
                                                     USER INFO:
                                            USERNAME: @{username}
                                            USER ID: {userid}
                                            CHANNEL: {channel_id}
                                                 L  E  G  I  O  N
────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────\n\n\n
"""
    try:
        for line in legion.splitlines():
            print(Center.XCenter(Colorate.Horizontal(rr, line, 1)))
        for line in info.splitlines():
            print(Center.XCenter(Colorate.Horizontal(v, line, 1)))
    except OSError:
        # Fallback if terminal size can't be determined (e.g., in some IDEs)
        print(Colorate.Horizontal(rr, legion, 1))
        print(Colorate.Horizontal(v, info, 1))

def main():
    token = input(f"{Fore.RED}Enter Token Here: ")
    channel_id = input(f"{Fore.RED}Enter Channel ID Here: ")

    # Get and validate user-defined wait times
    try:
        min_wait = int(input(f"{Fore.RED}Enter Minimum Wait Time (seconds, default: 2): ") or 2)
    except ValueError:
        min_wait = 2
    
    try:
        max_wait = int(input(f"{Fore.RED}Enter Maximum Wait Time (seconds, default: 4): ") or 4)
    except ValueError:
        max_wait = 4

    # Ensure min_wait is not greater than max_wait
    if min_wait > max_wait:
        print(Colorate.Horizontal(er, "Minimum wait time was greater than maximum. Swapping them.", 1))
        min_wait, max_wait = max_wait, min_wait


    clear()

    sent_count = 0
    deleted_count = 0
    error_count = 0
    update_title(sent_count, deleted_count, error_count)

    messages = ['i agree', 'true', 'real', 'fax dude', 'yeah', 'exactly', 'true af', 'definitely', 'definitely true', 'fax', 'indeed', 'for sure', 'totally', 'could be', 'maybe', 'i disagree', 'probably', 'probably not', 'idk', 'cool', 'not true', 'incorrect', 'definitely not', 'nah', 'wrong', 'lol', 'okay', 'ok', 'k', 'bruh', 'unreal', 'nope', 'fs', 'fs bro', 'peekaboo', 'bro wtf r you talking about', 'hm', 'ugly asl', 'nigga what', 'nigga', 'brother', 'dang', 'xanax', 'hru?', 'im bored', 'im bored asl', 'tired', 'im sleepy', 'tired asf', 'air', 'clipped', 'clown', 'yo what', 'ignored', 'test', 'continuing on', 'nice', 'oh lol', 'wtf lol', 'jeez', 'thats crazy', 'crazy', 'wild asl', 'wild twin', 'big 2025', 'no', 'ikr', 'wild', 'oh shit', 'jvc', 'ur a furry', 'yo wassup bro', 'nigga stfu', 'igh bro', 'wtf you talking about', 'yap', 'heavy', 'cuminnabun', 'crazy as shit', 'insane', 'insane works', 'gah dam', 'twin', 'cover', 'im back', 'nigga what the fuck', 'goodness', 'loner', 'bro no stop it', 'yap', 'oh my god we dont care', 'stupid', 'dickhead', 'idiot', 'clown', 'yappatron', 'stop yapping', 'goodness', 'alright brother', 'dam brother', 'wsp brother', 'wtf brother', 'dam bro', 'yoooo', 'hahahaha', 'LOL', 'XD', 'LMAO', 'LO', 'OL', 'LOOOLOLOOLL','LMAOOOOOOOOO', 'stfu LMAO', 'ah shucks', 'wow', 'loser', 'random', 'what the hell?', 'talking nonsense', 'bruh', 'LMFAOOOOOO XD', 'ROFL', 'rofl', 'lmao', 'LMFAO', 'ok rofl', 'nigga', 'bro what', 'rofl xd', '🥱', '😶', '😂', '🤣🤣', '💀', '💀💀💀', '💔', '😭😭😭😭', '😭', '😭😭😭💔💔💔💔', '☠️', '☠️☠️', '🫡', '👋👋', 'great', 'thats amazing', '????', 'stop talking', '!?!??????!!?', '??????????????', '🤷‍♂️', '😹😹', 'hilarious brother', 'tip', ':/', ':)', ':(', ';(', '):', '(:', 'c:', ':c', '>:c', 'c:<', '>:(', '(:<', '>;)', '(;<', '>;c', 'c;<', 'UwU', 'T-T', 'yup', 'wow', 'y?']
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Authorization': token
    }
    try:
        userinfo = r.get('https://canary.discordapp.com/api/v9/users/@me', headers=headers).json()
        username = userinfo["username"]
        discriminator = userinfo["discriminator"]
        userid = userinfo["id"]
    except (r.exceptions.RequestException, KeyError):
        print(Colorate.Horizontal(er, "Invalid token or failed to connect to Discord. Please check your token and try again.", 1))
        return

    print_header(username, userid, channel_id)

    while True:
        wait_time = random.randint(min_wait, max_wait)

        message = random.choice(messages)
        json_data = {
            'content': message
        }
        send_req = r.post(f"https://discord.com/api/v9/channels/{channel_id}/messages", headers=headers, json=json_data)
        
        if send_req.status_code == 200:
            sent_count += 1
            message_id = send_req.json()['id']
            delete_req = r.delete(f"https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}", headers=headers)
            
            if delete_req.status_code == 204: # 204 No Content is success for a DELETE request
                deleted_count += 1
                log_message = f"[ LEGION ] | [Waiting {wait_time} seconds...] Sent message > {message} | deleted it"
                print(Colorate.Horizontal(Colors.green_to_red, log_message, 1))
            else:
                error_count += 1
                error_message = f"Failed to delete message. Status: {delete_req.status_code}"
                print(Colorate.Horizontal(Colors.red_to_black, error_message, 1))
        else:
            error_count += 1
            error_message = f"Failed to send message. Status: {send_req.status_code}"
            print(Colorate.Horizontal(Colors.red_to_black, error_message, 1))
        
        update_title(sent_count, deleted_count, error_count)
        time.sleep(wait_time)

if __name__ == "__main__":
    main()
