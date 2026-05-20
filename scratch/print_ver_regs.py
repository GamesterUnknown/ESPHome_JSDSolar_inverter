import openpyxl, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook(r'docs\INV-Modbus地址表3KU（外发）V1.20.xlsx', data_only=True)
ws = wb[' WF_Version']

version_targets = set(list(range(0, 10)) + list(range(16, 38)) + list(range(56, 64)))

seen = set()
for r in ws.iter_rows(values_only=True):
    if r[1] is None:
        continue
    try:
        dec = int(r[1])
        if dec in version_targets:
            key = (dec, str(r[5]))
            if key not in seen:
                seen.add(key)
                print(f'Dec={dec:3d}  Hex=0x{str(r[2]).zfill(4)}  Type={str(r[6]):15s}  Name={r[5]}')
    except ValueError:
        pass
