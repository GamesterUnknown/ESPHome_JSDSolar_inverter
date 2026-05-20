import json

with open('scratch_targets.json', encoding='utf-8') as f:
    targets = json.load(f)

# Group targets by sheet or category
print("Generating YAML entries...")

# Let's map target registers to YAML components.
# We have two main sections:
# 1. Version registers (0-9, 16-37, 56-63) - update_interval: 24h
# 2. Regular sensors - update_interval: default (10s)

# Version registers:
# 0-9: SN code (Text Sensor)
# 16-37: Versions
# 56-63: Identifiers

# Target numbers:
version_decs = list(range(0, 10)) + list(range(16, 38)) + list(range(56, 64))

# Let's load the full Excel data to get all version registers exactly right
import openpyxl
wb = openpyxl.load_workbook(r'docs\INV-Modbus地址表3KU（外发）V1.20.xlsx', data_only=True)
ws_ver = wb[' WF_Version']

versions_meta = []
for r in ws_ver.iter_rows(values_only=True):
    if r[1] is not None:
        try:
            dec = int(r[1])
            if dec in version_decs:
                versions_meta.append({
                    'dec': dec,
                    'hex': r[2],
                    'name': r[5],
                    'type': r[6],
                    'unit': r[7],
                    'usage': r[8]
                })
        except ValueError:
            pass

# Let's format the version sensors
version_yaml = []
# SN code is text_sensor
sn_code_yaml = """  # ── SN Code (Serial Number) ─────────────────────────────────────────────────
  - platform: modbus_controller
    modbus_controller_id: inverter
    name: "${friendly_name} SN Code"
    id: sn_code
    register_type: holding
    address: 0
    register_count: 10
    response_size: 20
    raw_encode: ANSI
    update_interval: 24h
"""

version_yaml.append("# ==========================================================================")
version_yaml.append("# WF_Version block (registers 16-37, 56-63) - Read once on startup")
version_yaml.append("# ==========================================================================")

for v in versions_meta:
    if 0 <= v['dec'] <= 9:
        continue # handled by SN Code text sensor
    # Convert hex address string to int for proper formatting in yaml
    addr_hex = f"0x{v['hex']}"
    # Name formatting: capitalize, replace _ with space, etc.
    raw_name = v['name']
    name = f"${{friendly_name}} {raw_name.replace('_', ' ')}"
    # Generate unique ID
    safe_id = raw_name.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('&', 'and').replace('.', '').replace(',', '').replace('-', '_').replace('__', '_')
    if safe_id.endswith('_h') or safe_id.endswith('_l'):
        pass
    else:
         if v['name'] == 'Equipment type_L':
             safe_id = 'equipment_type_l'
    
    yaml_snippet = f"""  - platform: modbus_controller
    modbus_controller_id: inverter
    name: "{name}"
    id: {safe_id}
    register_type: holding
    address: {addr_hex}
    value_type: U_WORD
    update_interval: 24h"""
    version_yaml.append(yaml_snippet)

print("Version YAML generated.")
with open('scratch_version_yaml.yaml', 'w', encoding='utf-8') as f:
    f.write('\n\n'.join(version_yaml))
