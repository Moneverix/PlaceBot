import requests
from time import sleep


print('''
       _       _                  _           _   
      | |     | |                | |         | |  
  _ __| |_ __ | | __ _  ___ ___  | |__   ___ | |_ 
 | '__| | '_ \| |/ _` |/ __/ _ \ | '_ \ / _ \| __|
 | |  |_| |_) | | (_| | (_|  __/ | |_) | (_) | |_ 
 |_|  (_) .__/|_|\__,_|\___\___| |_.__/ \___/ \__|
        | |                                       
        |_|   \n\n                                    
''')

print('In the input box below put pixel coordinate and color seperated by a comma to add it into queue, each pixel '
      'will be placed after ~3 minutes. \n\n'
      'Correct Format: a1 red, a2 blue, a3 yellow and so on until youre bored\n')

user_input = input('Comma-Seperated list of coords & colors: ')

coords_list = user_input.split(',')

coords_list = [coord.strip() for coord in coords_list]

coords_list = [coord for coord in coords_list if coord]


print(f'Check if this is a correct list "{coords_list}", if yes, press ENTER to continue, if there are typos, restart the script')

input('\nPress ENTER')

print('''
███████ ███████ ███    ██ ██████  ██ ███    ██  ██████         ██  
██      ██      ████   ██ ██   ██ ██ ████   ██ ██           ██  ██ 
███████ █████   ██ ██  ██ ██   ██ ██ ██ ██  ██ ██   ███         ██ 
     ██ ██      ██  ██ ██ ██   ██ ██ ██  ██ ██ ██    ██     ██  ██ 
███████ ███████ ██   ████ ██████  ██ ██   ████  ██████         ██  
                                                                   
                                                                   
''')


# Main loop, sending messages in the place channel on CnekGDPS

while coords_list:

    payload = {
        'content': f"r!pl {coords_list[0]}"
    }

    header = {
        'authorization': "" ########################################### Your token here, this is IMPORTANT ####################################################################
    }

    r = requests.post('https://discord.com/api/v9/channels/963762408143355914/messages', # Don't change this
                      json=payload,
                      headers=header)
    print(f'Sent {coords_list[0]}. | Next pixel in 3 minutes')
    if coords_list:
        coords_list.pop(0)
        if coords_list:
            sleep(180)
            continue
        else:
            print('No more coords to send')
            break
    else:
        print('No more coords to send')
        break

print('''
███████ ██ ███    ██ ██ ███████ ██   ██ ███████ ██████  
██      ██ ████   ██ ██ ██      ██   ██ ██      ██   ██ 
█████   ██ ██ ██  ██ ██ ███████ ███████ █████   ██   ██ 
██      ██ ██  ██ ██ ██      ██ ██   ██ ██      ██   ██ 
██      ██ ██   ████ ██ ███████ ██   ██ ███████ ██████  
                                                        
                                                        
\n''')
input('Press Enter to close the script.')