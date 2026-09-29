import json,urllib.request,urllib.parse,time,sys
B="https://boamp-datadila.opendatasoft.com/api/explore/v2.1/catalog/datasets/boamp/records"
TERMS=sys.argv[1:]
out={}
for t in TERMS:
    off=0
    while True:
        q=urllib.parse.urlencode({"where":f'"{t}"',"limit":100,"offset":off,"select":"idweb,objet,nomacheteur,titulaire,dateparution,type_avis,nature_libelle,procedure_libelle,code_departement,url_avis,donnees"})
        for a in range(4):
            try: d=json.load(urllib.request.urlopen(B+"?"+q,timeout=120));break
            except Exception as e: err=e;time.sleep(2**a)
        else: print("ERR",t,err,file=sys.stderr);break
        for r in d["results"]: out.setdefault(r["idweb"],{**r,"terms":[]})["terms"].append(t)
        print(t,off,d["total_count"],file=sys.stderr)
        off+=100
        if off>=d["total_count"] or off>=500: break
json.dump(list(out.values()),open("boamp_hits.json","w"),ensure_ascii=False)
