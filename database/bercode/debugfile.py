<<<<<<< HEAD


filename = "./database/bercode/barReadList.txt"
f = open(filename, 'r')

datalist = f.readlines()

import webbrowser
for i in datalist:
    url = 'https://www.ymm.co.jp/p/detail.php?code='+i
    webbrowser.open(url)
    input()



=======


filename = "./database/bercode/barReadList.txt"
f = open(filename, 'r')

datalist = f.readlines()

import webbrowser
for i in datalist:
    url = 'https://www.ymm.co.jp/p/detail.php?code='+i
    webbrowser.open(url)
    input()



>>>>>>> 5906a4ab66ba0d42e7d0ac461409b3aac70dc8c9
