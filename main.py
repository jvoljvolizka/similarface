import os
from bs4 import BeautifulSoup
import time
import subprocess

if __name__ == "__main__":

    sourceFile='test2.jpeg'
    found = False
    x = 0

    while (not found):
        similarity = ""
        x = x+1
        os.system("wget https://thispersondoesnotexist.com/image -q -O target.jpeg")
        print("test")
        targetFile='target.jpeg'

        out = subprocess.check_output("curl -F 'image=@/var/www/similar.jvoljvolizka.me/public_html/target.jpeg'   172.17.0.2:5000",shell=True) 
        with open("index.html") as fp:
            soup = BeautifulSoup(fp)
        new_link = soup.new_tag('h1')
        new_link.string="counter " + str(x)
        new_p = soup.new_tag('p')
        new_p.string = out
        old_b = soup.h1.replace_with(new_link)
        old_b2 = soup.p.replace_with(new_p)
        with open("index.html", "w") as outf:
                outf.write(str(soup))
        parse = out.split(" ")
        print(parse[-1])
        if (float(parse[-1]) < 0.2):
            break



        print(str(x ))


