import json,urllib.request,urllib.parse,time,sys,re
B="https://data.economie.gouv.fr/api/explore/v2.1/catalog/datasets/%s/records"
DS={"decp-2022-marches-valides":"objet","decp-v3-marches-valides":"objet","decp_augmente":"objetmarche"}
TERMS=["infectiovigilance","logiciel d'hygiène","logiciel hygiène hospitalière","logiciel d'épidémiologie","logiciel épidémiologie","surveillance des infections","nosokos","icnet","bmr bhre logiciel","antibiothérapie logiciel","aide à la prescription antibiotique","lumed","zinc","consores","epiclic","clarisys","bac'express","infection associée aux soins logiciel"]
def get(ds,where):
    out=[];off=0
    while True:
        q=urllib.parse.urlencode({"where":where,"limit":100,"offset":off})
        for a in range(4):
            try: d=json.load(urllib.request.urlopen(B%ds+"?"+q,timeout=90));break
            except Exception as e: err=e;time.sleep(2**a)
        else: print("ERR",ds,where,err,file=sys.stderr);return out
        out+=d["results"];off+=100
        if off>=d.get("total_count",0) or off>=300:return out
res={}
for ds,obj in DS.items():
    for t in TERMS:
        for r in get(ds,f'search({obj},"{t}")'):
            o=r.get(obj) or ""
            res.setdefault((o[:120],str(r.get("datenotification"))),{**r,"ds":ds,"obj":o,"terms":set()})["terms"].add(t)
out=[]
for v in res.values():
    v["terms"]=sorted(v["terms"]);out.append(v)
json.dump(out,open("decp_ipc_kw.json","w"),ensure_ascii=False,default=str)
print(len(out))
