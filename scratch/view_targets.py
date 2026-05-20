import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch_targets.json', encoding='utf-8') as f:
    res = json.load(f)

for r in res:
    print(f'{r["sheet"]}: Dec={r["dec"]}, Hex={r["hex"]}, Name={r["name"]}, Type={r["type"]}, Unit={r["unit"]}, Usage={r["usage"]}')
