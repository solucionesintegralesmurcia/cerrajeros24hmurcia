import re,json,glob,os,sys
d=sys.argv[1]
for f in sorted(glob.glob(d+"/*.html")):
    s=open(f).read()
    h1=len(re.findall(r"<h1",s))
    lds=re.findall(r'<script type="application/ld\+json">(.*?)</script>',s,re.S)
    types=[json.loads(x)["@type"] for x in lds]
    links=set(re.findall(r'href="([a-z0-9\-]+\.html)"',s))
    bad=[l for l in links if not os.path.exists(os.path.join(d,l))]
    t=re.search("<title>(.*?)</title>",s).group(1)
    print(os.path.basename(f),"h1=",h1,types,len(t),"BAD:"+str(bad) if bad else "")
