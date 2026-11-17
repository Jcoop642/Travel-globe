import json, sys
tpl, seed, mljs, mlcss, out = sys.argv[1:6]
places = json.load(open(seed))
if isinstance(places, dict): places = places.get('places') or places.get('features')
cols = {"krishna": "#F2A33A", "retreat": "#F29CB8", "ecovillage": "#6CC08B", "volunteer": "#6EC3F4", "coliving": "#A884F3", "event": "#F25FA8", "work": "#7FA3C7", "hub": "#FF8A65", "sailing": "#3FC1B0", "housesit": "#F5C451"}
names = {'krishna':'Krishna','ecovillage':'Ecovillages','coliving':'Co-living','retreat':'Retreats','volunteer':'Volunteering','hub':'Hubs and regions','event':'Festivals','work':'Work','housesit':'Housesits','sailing':'Sailing'}
layers = {k:{'n':names[k],'c':cols.get(k,'#ffffff')} for k in names}
keep = ['id','name','layer','country','lat','lon','people','crowd','social','cost','stay','kv','who','vibe','link','status','region']
slim = [{k:p.get(k) for k in keep if p.get(k) not in (None,'')} for p in places]
s = open(tpl).read()
js = open(mljs).read().replace('</script', '<\\/script')
s = s.replace('/*MLCSS*/', open(mlcss).read()).replace('/*MLJS*/', js).replace('/*PLACES*/', json.dumps(slim, ensure_ascii=False).replace('</', '<\\/')).replace('/*LAYERS*/', json.dumps(layers))
open(out,'w').write(s); print(len(slim), 'places', len(s)//1024, 'KB', sorted(set(p['layer'] for p in slim)))
