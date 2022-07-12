import os
import sys
from pystyle import Colorate, Colors, Center
from settings import *
import sys
all()
def system():
        if os.name == "nt":
           os.system('cls')
        else:
            os.system('clear')
system()
        
header = """
          ____                                    
        ,'  , `.               ___      ,---,     
     ,-+-,.' _ |             ,--.'|_  ,--.' |     
  ,-+-. ;   , ||             |  | :,' |  |  :     
 ,--.'|'   |  ;|             :  : ' : :  :  :     
|   |  ,', |  ':  ,--.--.  .;__,'  /  :  |  |,--. 
|   | /  | |  || /       \ |  |   |   |  :  '   | 
'   | :  | :  |,.--.  .-. |:__,'| :   |  |   /' : 
;   . |  ; |--'  \__\/: . .  '  : |__ '  :  | | | 
|   : |  | ,     ," .--.; |  |  | '.'||  |  ' | : 
|   : '  |/     /  /  ,.  |  ;  :    ;|  :  :_:,' 
;   | |`-'     ;  :   .'   \ |  ,   / |  | ,'     
|   ;/         |  ,     .-./  ---`-'  `--''       
'---'           `--`---'                    """

print(Colorate.Horizontal(Colors.red_to_blue, Center.Center(header)))
while True:
   
    command = input('#-@-> ')
    if command == "exit":
        sys.exit()