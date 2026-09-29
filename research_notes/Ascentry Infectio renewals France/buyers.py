import json,urllib.request,urllib.parse,time,sys,re
B="https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/%s/records"
BUY={"verdun":"VERDUN","saint-mihiel":"MIHIEL","triangle":"TRIANGLE","bar-le-duc":"BAR LE DUC","saint-dizier":"DIZIER","grenoble":"GRENOBLE","reims":"REIMS","nancy":"NANCY","abbeville":"ABBEVILLE","dijon":"DIJON","nevers":"NEVERS"}
KW=re.compile(r"(?i)logiciel|middleware|informati|épidémio|epidemio|hygi|bactério|bacterio|microbio|infect|antibio|maldi|byg|partner|nosokos|sil\b")
def get(ds,where,sel):
    out=[];off=0
    while True:
        q=urllib.parse.urlencode({"where":where,"limit":100,"offset":off})
        for a in range(4):
            try: d=json.load(urllib.request.urlopen(B%ds+"?"+q,timeout=90));break
            except Exception as e: err=e;time.sleep(2**a)
        else: print("ERR",ds,where,err,file=sys.stderr);return out
        out+=d["results"];off+=100
        if off>=d.get("total_count",0) or off>=2000:return out
rows=[]
for k,v in BUY.items():
    for ds,nf,of in [("decp_augmente","nomacheteur","objetmarche"),("decp-v3-marches-valides","acheteur_nom","objet")]:
        rs=get(ds,f'search({nf},"{v}") and (search({of},"logiciel") or search({of},"bactériologie") or search({of},"microbiologie") or search({of},"épidémiologie") or search({of},"hygiène") or search({of},"middleware"))',None)
        for r in rs:
            o=(r.get(of) or "").replace("\n"," ")
            if KW.search(o): rows.append((k,ds,r.get("datenotification"),r.get("dureemois"),r.get("montant"),r.get(nf),r.get("denominationunitelegale") or r.get("titulaire_denominationsociale_1") or r.get("titulaire_id_1"),o[:200]))
seen=set()
for x in sorted(rows,key=lambda x:(x[0],str(x[2]))):
    key=(x[0],x[2],x[7][:60])
    if key in seen: continue
    seen.add(key);print(" | ".join(str(i) for i in x))
