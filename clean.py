fhuman= open("humanconv.txt","r",encoding="utf-8", errors="ignore")
fbot=open("botconv.txt","r", encoding="utf-8", errors="ignore")

fhumanclean= open("humanconvclean.txt","a",encoding="utf-8", errors="ignore")
fbotclean=open("botconvclean.txt","a", encoding="utf-8", errors="ignore")

for line in fhuman.readlines():
    if(line!='\n'):
        fhumanclean.write(line)


for line in fbot.readlines():
    if(line!='\n'):
        fbotclean.write(line)
