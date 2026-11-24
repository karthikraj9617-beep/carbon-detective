import pathlib,json,base64,mimetypes
P=pathlib.Path
assets={p.name:[mimetypes.guess_type(p.name)[0] or 'application/octet-stream',base64.b64encode(p.read_bytes()).decode()] for p in P('public').iterdir() if p.is_file()}
P('dist/server').mkdir(parents=True,exist_ok=True)
P('dist/server/index.js').write_text('const assets='+json.dumps(assets)+';const data='+P('worker/data.json').read_text()+';\n'+P('worker/handler.js').read_text())
