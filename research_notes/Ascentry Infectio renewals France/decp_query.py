import json, urllib.request, urllib.parse, time, sys
B="https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/%s/records"
DS={"decp-2022-marches-valides":("objet",["titulaire_id_1","titulaire_id_2","titulaire_id_3"]),
    "decp-v3-marches-valides":("objet",["titulaire_id_1","titulaire_id_2","titulaire_id_3"]),
    "decp_augmente":("objetmarche",["siretetablissement","id_cotitulaire1","id_cotitulaire2"]),
    "decp_aws":("objet",[]),
    "decp-2022-marches-exclus":("objet",["titulaire_id_1","titulaire_id_2"]),
    "decp-v3-marches-invalides":("objet",["titulaire_id_1","titulaire_id_2"])}
SIRENS=["326649407","349314948","915233837"]
TERMS=["infectio","ynfectio","ynfectiolabo","byg4lab","byg","partner4lab","info partner","infopartner","vigiact","vigi@ct","infection tracker","ascentry","epidemiologie hygiene logiciel"]
def get(ds,where):
    out=[];off=0
    while True:
        q=urllib.parse.urlencode({"where":where,"limit":100,"offset":off})
        for a in range(4):
            try:
                d=json.load(urllib.request.urlopen(B%ds+"?"+q,timeout=90));break
            except Exception as e:
                err=e;time.sleep(2**a)
        else:
            print("ERR",ds,where,err,file=sys.stderr);return out
        out+=d["results"];off+=100
        if off>=d.get("total_count",0) or off>=1000:return out
allr={}
for ds,(obj,ids) in DS.items():
    wh=[]
    for f in ids:
        for s in SIRENS: wh.append(f'startswith({f},"{s}")')
    for t in TERMS: wh.append(f'search({obj},"{t}")')
    for w in wh:
        rs=get(ds,w)
        for r in rs:
            key=(ds,str(r.get("id")),str(r.get("datenotification")),str(r.get("montant")),str(r.get("idmodification","")))
            allr.setdefault(key,{"ds":ds,"match":[], **r})["match"].append(w)
        if rs: print(ds,w,len(rs),file=sys.stderr)
json.dump(list(allr.values()),open("decp_hits.json","w"),ensure_ascii=False,indent=1,default=str)
print(len(allr))
