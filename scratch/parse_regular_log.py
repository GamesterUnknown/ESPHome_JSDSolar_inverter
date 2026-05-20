import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

raw = """[uart_debug:113]: [MASTER ] <<< 01:10:41:43:00:01:02:00[01:12:15.123][D][uart_debug:113]: [MASTER ] <<< 03:B9:A6[01:12:15.135][D][uart_debug:113]: [SLAVE ] <<< 01:10:41:43:00:01:E4:21[01:12:15.162][D][uart_debug:113]: [MASTER ] <<< 01:10:41:64:00:01:02:00:00:FF:70[01:12:15.188][D][uart_debug:113]: [SLAVE ] <<< 01:10:41:64:00:01:54:2A[01:12:15.206][D][uart_debug:113]: [MASTER ] <<< 01:03:00:39:00:01:54:07[01:12:15.235][D][uart_debug:113]: [SLAVE ] <<< 01:03:02:00:40:B9:B4[01:12:22.476][D][uart_debug:113]: [MASTER ] <<< 01:03:00:00:00:0A:C5:CD[01:12:22.531][D][uart_debug:113]: [SLAVE ] <<< 01:03:14:37:33:32:35:31:32:30:36:30:30:30:31:31:33:00:00:00:00:00:00:C9:EF[01:12:22.554][D][uart_debug:113]: [MASTER ] <<< 01:03:00:00:00:0A:C5:CD[01:12:22.605][D][uart_debug:113]: [SLAVE ] <<< 01:03:14:37:33:32:35:31:32:30:36:30:30:30:31:31:33:00:00:00:00:00:00:C9:EF[01:12:22.632][D][uart_debug:113]: [MASTER ] <<< 01:03:00:10:00:02:C5:CE[01:12:22.677][D][uart_debug:113]: [SLAVE ] <<< 01:03:04:00:01:00:05:6B:F0[01:12:22.695][D][uart_debug:113]: [MASTER ] <<< 01:03:00:1A:00:02:E5:CC[01:12:22.734][D][uart_debug:113]: [SLAVE ] <<< 01:03:04:01:00:00:2E:7B:D3[01:12:22.766][D][uart_debug:113]: [MASTER ] <<< 01:03:00:43:00:02:35:DF[01:12:22.775][D][uart_debug:113]: [SLAVE ] <<< 01:03:04:02:00:10:00:F6:4B[01:12:22.795][D][uart_debug:113]: [MASTER ] <<< 01:03:00:46:00:04:A5:DC[01:12:22.845][D][uart_debug:113]: [SLAVE ] <<< 01:03:08:00:00:00:00:00:00:00:00:95:D7[01:12:22.869][D][uart_debug:113]: [MASTER ] <<< 01:03:00:50:00:04:44:18[01:12:22.911][D][uart_debug:113]: [SLAVE ] <<< 01:03:08:00:00:00:00:00:00:00:00:95:D7[01:12:22.938][D][uart_debug:113]: [MASTER ] <<< 01:03:00:58:00:06:44:1B[01:12:22.988][D][uart_debug:113]: [SLAVE ] <<< 01:03:0C:00:00:00:00:00:00:00:00:00:00:00:00:93:70[01:12:23.028][D][uart_debug:113]: [MASTER ] <<< 01:03:00:80:00:02:C5:E3[01:12:23.074][D][uart_debug:113]: [SLAVE ] <<< 01:03:04:01:F5:00:00:EB:FD[01:12:23.099][D][uart_debug:113]: [MASTER ] <<< 01:03:00:84:00:02:84:22[01:12:23.146][D][uart_debug:113]: [SLAVE ] <<< 01:03:04:00:2C:00:00:3B:FA[01:12:23.176][D][uart_debug:113]: [MASTER ] <<< 01:03:00:8F:00:04:75:E2[01:12:23.219][D][uart_debug:113]: [SLAVE ] <<< 01:03:08:20:50:00:00:00:00:00:00:C7:CA[01:12:23.247][D][uart_debug:113]: [MASTER ] <<< 01:03:00:96:00:06:25:E4[01:12:23.298][D][uart_debug:113]: [SLAVE ] <<< 01:03:0C:00:00:00:00:00:00:00:00:00:00:00:00:93:70[01:12:23.324][D][uart_debug:113]: [MASTER ] <<< 01:03:00:A0:00:01:84:28[01:12:23.373][D][uart_debug:113]: [SLAVE ] <<< 01:03:02:00:00:B8:44[01:12:23.398][D][uart_debug:113]: [MASTER ] <<< 01:03:01:40:00:01:84:22[01:12:23.428][D][uart_debug:113]: [SLAVE ] <<< 01:03:02:00:00:B8:44[01:12:23.450][D][uart_debug:113]: [MASTER ] <<< 01:03:01:95:00:03:14:1B[01:12:23.501][D][uart_debug:113]: [SLAVE ] <<< 01:03:06:00:00:00:00:00:00:21:75[01:12:23.515][D][uart_debug:113]: [MASTER ] <<< 01:03:01:9B:00:02:B4:18[01:12:23.553][D][uart_debug:113]: [SLAVE ] <<< 01:03:04:00:00:00:00:FA:33[01:12:23.579][D][uart_debug:113]: [MASTER ] <<< 01:03:01:BF:00:08:74:14[01:12:23.621][D][uart_debug:113]: [SLAVE ] <<< 01:03:10:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:E4:59[01:12:23.646][D][uart_debug:113]: [MASTER ] <<< 01:03:02:21:00:08:15:BE[01:12:23.694][D][uart_debug:113]: [SLAVE ] <<< 01:03:10:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:00:E4:59[01:12:23.736][D][uart_debug:113]: [MASTER ] <<< 01:03:02:67:00:08:F4:6B[01:12:23.792][D][uart_debug:113]: [SLAVE ] <<< 01:03:10:00:00:00:02:00:00:00:17:00:00:00:17:00:00:01:03:3D:79"""

# Split into individual MASTER packets
master_packets = re.findall(r'\[MASTER \] <<< ([0-9A-Fa-f:]+)', raw)

regular_addrs = set()
regular_ranges = []

for pkt in master_packets:
    bytes_ = [int(b, 16) for b in pkt.split(':') if b]
    # Need at least 6 bytes: slave, fc, addrH, addrL, countH, countL
    if len(bytes_) < 6:
        continue
    slave = bytes_[0]
    fc = bytes_[1]
    # Only FC=03 (read) packets with exactly 8 bytes total (slave+fc+addrH+addrL+cntH+cntL+crcL+crcH)
    if fc == 0x03 and len(bytes_) == 8:
        addr = (bytes_[2] << 8) | bytes_[3]
        count = (bytes_[4] << 8) | bytes_[5]
        regular_ranges.append((addr, count))
        for a in range(addr, addr + count):
            regular_addrs.add(a)
    # FC=0x10 (write): slave + fc + addrH + addrL + cntH + cntL + byteCount + data... + crc
    # We skip writes for now

# Print unique sorted ranges
print(f"Unique MASTER FC=03 packets found: {len(regular_ranges)}")
print(f"Unique addresses touched: {len(regular_addrs)}")
print()
print("Ranges (start, count, end):")
# Deduplicate ranges
seen = set()
deduped = []
for r in regular_ranges:
    if r not in seen:
        seen.add(r)
        deduped.append(r)

for start, count in deduped:
    print(f"  0x{start:04X} + {count} = 0x{start:04X}..0x{start+count-1:04X}  (dec {start}..{start+count-1})")

print()
print("Python set literal for gen_map.py REGULAR_RANGES:")
print("REGULAR_RANGES = [")
for start, count in deduped:
    print(f"    (0x{start:04X}, {count}),")
print("]")
