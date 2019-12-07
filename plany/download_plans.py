from urllib.request import urlretrieve

addr = "http://plan.zs9elektronik.pl/plany/o.html"
n = 31

for i in range(1, n+1):
    urlretrieve(addr.replace(".html", f"{i}.html"), f"o{i}.html")