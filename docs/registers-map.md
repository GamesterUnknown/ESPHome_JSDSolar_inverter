# JSD Solar 3KU — Complete Modbus Register Map

> **Source:** `INV-Modbus地址表3KU（外发）V1.20.xlsx`  
> **Type:** Holding Registers, Function Code 03  
> **Addresses:** 0-based hex (`address:` field in ESPHome)  
>
> **Initial Logger query column:** indicates registers requested by the logger on startup (from startup log data)  
> **Regular Logger query column:** indicates registers requested by the logger during regular operation (from uart_debug log data)  
> **My Logger query column:** indicates registers that already have a sensor defined in `jsd-solar-inverter.yaml` (with the name in the **ESPHome id** column)

## Table of Contents

1. [Document Versions](#version-information)
2. [Communication Format](#communication-format)
3. [Registers](#register-sheets)

---

## Version information
<a name="version-information"></a>

| Version | Author | Date | Changes |
|---------|--------|------|---------|
| V1.0 | Huo Junhong | 2023-09-12 | First draft |
| V1.1 | Huo Junhong | 2023-11-03 | Improve the content of the external agreement |
| V1.2 | Huo Junhong | 2023-11-06 | Modify the external protocol address and add redundancy design. |
| V1.3 | Mao Jiankun | 2023-11-30 | Modify the calibration address table and supplement the calibration object table. |
| V1.4 | Huo Junhong | 2023-12-10 | 1. Corrected the communication format description. 2. Added an FCT driver enable register. 3. Supplemented the address of the inverter DC component... |
| V1.5 | Huo Junhong | 2023-12-15 | 1. Added OTA flashing field. 2. Adjusted the starting address of the user parameter setting field. |
| V1.6 | Huo Junhong | 2024-05-22 | 1. Simplify field data supplementation and organization. 2. Rated field data deletion. 3. Battery current unit changed to 0.1A. 4. Supplementary ex... |
| V1.7 | Huo Junhong | 2024-06-06 | 1. Added explanation of alarm codes. 2. Removed rated information field. 3. Removed charging mode setting field. 4. Updated output priority & opera... |
| V1.8 | Huo Junhong | 2024-06-12 | 1. Added a field for users to set the current execution state. 2. Changed the device model configuration description. |
| V1.9 | Huo Junhong | 2024-07-03 | 1. Added description of BMS connection status. 2. Corrected load percentage unit to '%'. 3. Added 'GEN' output mode, 'MKP' output priority, and 'PV... |
| V1.10 | Huo Junhong | 2024-08-11 | 1. Added battery power, AC power, and generator power fields (Note: These three power values are estimated and have low accuracy! Use with caution!... |
| V1.11 | Huo Junhong | 2024-08-27 | 1. Added power-related data to the Simplify field and adjusted the data structure. 2. Added only power consumption data to the Line field. 3. Suppl... |
| V1.12 | Huo Junhong | 2024-08-27 | 1. Added settings fields related to automatic feeder power switching. |
| V1.13 | Wang Jianfei | 2024-10-29 | 1. Added Factory Test Acceleration to Charge State Switch (FCT) 2. Added Flag to Set Fan Speed to 100 Before Shutdown |
| V1.14 | Bai Yiting | 2024-10-30 | Added instruction to set inverter current reference value for output power less than 50W |
| V1.15 | Mao Jiankun | 2024-11-26 | Add reverse key commands |
| V1.16 | Mao Jiankun and Bai Yiting | 2025-01-08 | 1. Modified the MDC setting range according to VMH6KU requirements. 2. Updated the definition of the Wi-Fi connection flag to be compatible with th... |
| V1.17 | Mao Jiankun | 2025-01-13 | 1. Added alarms 76 and 77: 76CT reverse connection, 77 unstable mains power. 2. Model identification number 0x0038 is used for combined customer an... |
| V1.18 | Lin Jinqiang | 2025-02-06 | 1. Added model description and parameters for 5KVMHU. 2. Added definition for address 0x1020, which can read the inverter's serial number (SN). |
| V1.19 | Wang Jianfei | 2025-02-18 | 1. NTC pages increase discharge temperature |
| V1.20 | Mao Jiankun | 2025-02-20 | 1. Added explanation for version number writing markers. 2. Added options to the 0x412E setting. 3. Added a new RGB screen lock setting 0x414C. |

---

## Communication format
<a name="communication-format"></a>

**Port parameters:** 9600 bps, 8N1 (8 data bits, No parity, 1 stop bit)

### Request (Function Code 0x03 / 0x10)

| Field | Slave Addr | Func Code | Addr High | Addr Low | Reg Count High | Reg Count Low | CRC Low | CRC High |
|------|-----------|-----------|-----------|----------|---------------|--------------|---------|----------|
| Bytes | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

### Available Function Codes

| Code | Description |
|-----|------|
| 0x03 | Read Holding Registers |
| 0x10 | Write Holding Registers |

### Exception Codes

| Code | Description |
|-----|------|
| 1 | Request command function code not allowed |
| 2 | Request to read/write address out of bounds |
| 3 | The written value exceeds the upper and lower limits set by the data. |
| 4 | Unable to receive a reply from the timed communication device for more than 3 seconds |

---

## Registers
<a name="register-sheets"></a>

---

### WF_Version

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ | ✅ | ✅ | sn_code | `0x0000` | 0 | Version status debugging address set |  |  |  |  |
| ✅ | ✅ | ✅ | sn_code | `0x0000` | 0 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+1 | `0x0001` | 1 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+2 | `0x0002` | 2 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+3 | `0x0003` | 3 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+4 | `0x0004` | 4 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+5 | `0x0005` | 5 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+6 | `0x0006` | 6 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+7 | `0x0007` | 7 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+8 | `0x0008` | 8 | SN code | uint16_t |  | Reading and writing |  |
| ✅ | ✅ | ✅ | sn_code+9 | `0x0009` | 9 | SN code | uint16_t |  | Reading and writing |  |
| ✅ |  |  |  | `0x000A` | 10 | reserve | uint16_t |  | Reading and writing |  |
|  |  |  |  | `0x000B` | 11 | reserve | uint16_t |  | Reading and writing |  |
|  |  |  |  | `0x000C` | 12 | reserve | uint16_t |  | Reading and writing |  |
|  |  |  |  | `0x000D` | 13 | reserve | uint16_t |  | Reading and writing |  |
|  |  |  |  | `0x000E` | 14 | reserve | uint16_t |  | Reading and writing |  |
|  |  |  |  | `0x000F` | 15 | SN code lock | uint16_t |  | Reading and writing | To write the serial number, this location must be set to 0xA55A for the serial number to be retained even after power loss. |
| ✅ | ✅ | ✅ | protocol_version | `0x0010` | 16 | Protocol version_H | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | protocol_version+1 | `0x0011` | 17 | Protocol version_L | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | power_board_hw_version | `0x0012` | 18 | Power board hardware version_H | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | power_board_hw_version+1 | `0x0013` | 19 | Power board hardware version_L | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | control_board_hw_version | `0x0014` | 20 | Control board hardware version_H | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | control_board_hw_version+1 | `0x0015` | 21 | Control board hardware version_L | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | hmi_hw_version | `0x0016` | 22 | Centralized control version hardware version H | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | hmi_hw_version+1 | `0x0017` | 23 | Centralized control version hardware version L | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | power_board_sw_version | `0x0018` | 24 | Power board software version_H | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | power_board_sw_version+1 | `0x0019` | 25 | Power board software version_L | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | control_board_sw_version | `0x001A` | 26 | Control board software version_H | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | control_board_sw_version+1 | `0x001B` | 27 | Control board software version_L | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | hmi_sw_version | `0x001C` | 28 | Centralized control software version H | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | hmi_sw_version+1 | `0x001D` | 29 | Centralized control software version L | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | version_time | `0x001E` | 30 | Version Time_H | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | version_time+1 | `0x001F` | 31 | Version Time_L | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | checksum_ver | `0x0020` | 32 | CheckSum_H | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | checksum_ver+1 | `0x0021` | 33 | CheckSum_L | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | pc_protocol_version | `0x0022` | 34 | PC communication protocol version | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | wifi_protocol_version | `0x0023` | 35 | WiFi communication protocol version | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | bms_protocol_version | `0x0024` | 36 | BMS communication protocol version | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | parallel_protocol_version | `0x0025` | 37 | Parallel communication protocol version | uint16_t |  | Read-only |  |
| ✅ |  |  |  | `0x0026` | 38 |  |  |  |  |  |
| ✅ |  |  |  | `0x0027` | 39 |  |  |  |  |  |
| ✅ |  |  |  | `0x0028` | 40 |  |  |  |  |  |
| ✅ |  |  |  | `0x0029` | 41 |  |  |  |  |  |
| ✅ |  |  |  | `0x002A` | 42 |  |  |  |  |  |
| ✅ |  |  |  | `0x002B` | 43 |  |  |  |  |  |
| ✅ |  |  |  | `0x002C` | 44 |  |  |  |  |  |
| ✅ |  |  |  | `0x002D` | 45 |  |  |  |  |  |
| ✅ |  |  |  | `0x002E` | 46 |  |  |  |  |  |
| ✅ |  |  |  | `0x002F` | 47 |  |  |  |  |  |
| ✅ |  |  |  | `0x0030` | 48 |  |  |  |  |  |
| ✅ |  |  |  | `0x0031` | 49 |  |  |  |  |  |
| ✅ |  |  |  | `0x0032` | 50 |  |  |  |  |  |
| ✅ |  |  |  | `0x0033` | 51 |  |  |  |  |  |
| ✅ |  |  |  | `0x0034` | 52 |  |  |  |  |  |
| ✅ |  |  |  | `0x0035` | 53 |  |  |  |  |  |
| ✅ |  |  |  | `0x0036` | 54 |  |  |  |  |  |
| ✅ |  |  |  | `0x0037` | 55 |  |  |  |  |  |
| ✅ |  | ✅ | protocol_id_a | `0x0038` | 56 | Protocol Identifier_A | uint16_t |  | Read-only | Compatible Customers: 0x00: Reference Design 0x01: Reserved |
| ✅ | ✅ | ✅ | protocol_id_b | `0x0039` | 57 | Protocol Identifier_B | uint16_t |  | Read-only | Compatible models: 0x00: 6.5K 0x10: 6KU 0x20: 5KU |
| ✅ |  | ✅ | protocol_id_c | `0x003A` | 58 | Protocol Identifier_C |  |  | Read-only |  |
| ✅ |  | ✅ | protocol_id_d | `0x003B` | 59 | Protocol Identifier_D |  |  | Read-only |  |
| ✅ |  | ✅ | device_type | `0x003C` | 60 | Device Type_H |  |  | Read-only |  |
| ✅ |  | ✅ | device_type+1 | `0x003D` | 61 | Equipment type_L |  |  | Read-only |  |
| ✅ |  | ✅ | company_information | `0x003E` | 62 | Company Information_H |  |  | Read-only |  |
| ✅ |  | ✅ | company_information+1 | `0x003F` | 63 | Company Information_L |  |  | Read-only |  |

---

### WF_Simplify

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  | ✅ | sw_version | `0x0040` | 64 | Simplified information address set |  |  |  |  |
| ✅ |  | ✅ | sw_version | `0x0040` | 64 | Software version (major & minor) | uint16_t |  | Read-only | High 8-bit major version, low 8-bit minor version |
| ✅ |  | ✅ | bms_connection_status | `0x0041` | 65 | BMS connection status | uint16_t |  | Read-only | 0: ID search in progress; 1: ID locked - CAN; 2: ID locked - serial port; 3: ID remotely locked. |
| ✅ |  | ✅ | inverter_state | `0x0042` | 66 | State machine states | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | energy_terminal_status | `0x0043` | 67 | Energy terminal status | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | energy_flow | `0x0044` | 68 | Energy flow state | uint16_t |  | Read-only |  |
| ✅ |  | ✅ | parallel_operation_status | `0x0045` | 69 | Parallel operation | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | fault_code_1 | `0x0046` | 70 | Fault Code 1 | uint16_t |  | Read-only | BIT00: Mains soft start failure BIT01: Bus overvoltage BIT02: Bus undervoltage BIT03: Battery overcurrent BIT04: Overtemperatur... |
| ✅ | ✅ | ✅ | fault_code_2 | `0x0047` | 71 | Fault Code 2 | uint16_t |  | Read-only | BIT00: Programming in progress BIT01: Photovoltaic reverse connection BIT02: Parallel serial number abnormal BIT03: Parallel co... |
| ✅ | ✅ | ✅ | alarm_code_1 | `0x0048` | 72 | Alarm code 1 | uint16_t |  | Read-only | BIT00: Battery not connected BIT01: Battery undervoltage BIT02: Battery low voltage BIT03: Charger short circuit BIT04: Reserve... |
| ✅ | ✅ | ✅ | alarm_code_2 | `0x0049` | 73 | Alarm code 2 | uint16_t |  | Read-only | BIT00: Parallel communication error BIT01: Excessive voltage difference or frequency in parallel operation BIT02: Low SOC shutd... |
| ✅ |  |  |  | `0x004A` | 74 |  |  |  |  |  |
| ✅ |  |  |  | `0x004B` | 75 |  |  |  |  |  |
| ✅ |  |  |  | `0x004C` | 76 |  |  |  |  |  |
| ✅ |  |  |  | `0x004D` | 77 |  |  |  |  |  |
| ✅ |  |  |  | `0x004E` | 78 |  |  |  |  |  |
| ✅ |  |  |  | `0x004F` | 79 |  |  |  |  |  |
| ✅ | ✅ | ✅ | grid_voltage | `0x0050` | 80 | Phase A mains voltage | int16_t | 0.1V | Read-only |  |
| ✅ | ✅ | ✅ | grid_current | `0x0051` | 81 | Phase A mains current | int16_t | 0.01A | Read-only |  |
| ✅ | ✅ | ✅ | grid_frequency | `0x0052` | 82 | Phase A mains frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ | ✅ | ✅ | grid_power | `0x0053` | 83 | Phase A mains power | int16_t | 1W | Read-only |  |
| ✅ | ✅ | ✅ | load_voltage | `0x0058` | 88 | Phase A load voltage | int16_t | 0.1V | Read-only |  |
| ✅ | ✅ | ✅ | load_current | `0x0059` | 89 | Phase A load current | int16_t | 0.01A | Read-only |  |
| ✅ | ✅ | ✅ | load_frequency | `0x005A` | 90 | Phase A load frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ | ✅ | ✅ | load_active_power | `0x005B` | 91 | Phase A load active power | int16_t | 1W | Read-only |  |
| ✅ | ✅ | ✅ | load_apparent_power | `0x005C` | 92 | Apparent power of phase A load | int16_t | 1W | Read-only |  |
| ✅ | ✅ | ✅ | load_percentage | `0x005D` | 93 | Phase A load percentage | int16_t | 0.1% | Read-only |  |
| ✅ |  |  |  | `0x005E` | 94 |  |  |  |  |  |
| ✅ |  |  |  | `0x005F` | 95 |  |  |  |  |  |
| ✅ |  |  |  | `0x0060` | 96 | Phase B mains voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0061` | 97 | Phase B mains current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x0062` | 98 | Phase B mains frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x0063` | 99 | Phase B AC power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x0064` | 100 | B-phase generator voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0065` | 101 | B-phase generator current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x0066` | 102 | B-phase generator frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x0067` | 103 | B-phase generator power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x0068` | 104 | Phase B load voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0069` | 105 | B-phase load current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x006A` | 106 | Phase B load frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x006B` | 107 | B-phase load active power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x006C` | 108 | Apparent power of phase B load | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x006D` | 109 | Phase B load percentage | int16_t | 0.1% | Read-only |  |
| ✅ |  |  |  | `0x006E` | 110 |  |  |  |  |  |
| ✅ |  |  |  | `0x006F` | 111 |  |  |  |  |  |
| ✅ |  |  |  | `0x0070` | 112 | C-phase mains voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0071` | 113 | C-phase mains current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x0072` | 114 | C-phase mains frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x0073` | 115 | C-phase mains power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x0074` | 116 | C-phase generator voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0075` | 117 | C-phase generator current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x0076` | 118 | C-phase generator frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x0077` | 119 | C-phase generator power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x0078` | 120 | C-phase load voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0079` | 121 | C-phase load current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x007A` | 122 | C-phase load frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x007B` | 123 | C-phase load active power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x007C` | 124 | Apparent power of C-phase load | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x007D` | 125 | C-phase load percentage | int16_t | 0.1% | Read-only |  |
| ✅ |  |  |  | `0x007E` | 126 |  |  |  |  |  |
| ✅ |  |  |  | `0x007F` | 127 |  |  |  |  |  |
| ✅ | ✅ | ✅ | battery_voltage | `0x0080` | 128 | Positive terminal battery voltage | int16_t | 0.1V | Read-only |  |
| ✅ | ✅ | ✅ | battery_current | `0x0081` | 129 | Positive terminal battery current | int16_t | 0.1A | Read-only |  |
| ✅ |  | ✅ | battery_neg_voltage | `0x0082` | 130 | Negative battery voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  | ✅ | battery_neg_current | `0x0083` | 131 | Negative battery current | int16_t | 0.1A | Read-only |  |
| ✅ | ✅ | ✅ | battery_soc | `0x0084` | 132 | Battery capacity percentage | int16_t | 0.1% | Read-only |  |
| ✅ | ✅ | ✅ | battery_power | `0x0085` | 133 | Battery power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x0086` | 134 |  |  |  |  |  |
| ✅ |  |  |  | `0x0087` | 135 |  |  |  |  |  |
| ✅ |  | ✅ | bms_voltage | `0x0088` | 136 | BMS Battery Voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  | ✅ | bms_current | `0x0089` | 137 | BMS Battery Current | int16_t | 0.1A | Read-only |  |
| ✅ |  | ✅ | bms_soc | `0x008A` | 138 | BMS SOC | int16_t | % | Read-only |  |
| ✅ |  | ✅ | bms_temperature | `0x008B` | 139 | BMS Temperature | int16_t | ℃ | Read-only |  |
| ✅ |  | ✅ | bms_cv_point | `0x008C` | 140 | BMS constant pressure point (CV point) | uint16_t | 0.1V | Read-only |  |
| ✅ |  | ✅ | bms_rated_capacity | `0x008D` | 141 | Rated capacity | uint16_t | 100mAH | Read-only |  |
| ✅ |  | ✅ | bms_current_capacity | `0x008E` | 142 | Current capacity | uint16_t | 100mAH | Read-only |  |
| ✅ | ✅ | ✅ | bms_connected | `0x008F` | 143 | BMS communication status | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | bms_network_status | `0x0090` | 144 | Lithium battery network status | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | bms_failure_code | `0x0091` | 145 | BMS failure | uint16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | bms_alarm_code | `0x0092` | 146 | BMS Alarms | uint16_t |  | Read-only |  |
| ✅ |  |  |  | `0x0093` | 147 |  |  |  |  |  |
| ✅ |  |  |  | `0x0094` | 148 |  |  |  |  |  |
| ✅ |  |  |  | `0x0095` | 149 |  |  |  |  |  |
| ✅ | ✅ | ✅ | pv1_voltage | `0x0096` | 150 | Photovoltaic voltage 1 | int16_t | 0.1V | Read-only |  |
| ✅ | ✅ | ✅ | pv1_current | `0x0097` | 151 | Photovoltaic 1 current | int16_t | 0.01A | Read-only |  |
| ✅ | ✅ | ✅ | pv1_power | `0x0098` | 152 | Photovoltaic power | int16_t | 1W | Read-only |  |
| ✅ | ✅ | ✅ | pv2_voltage | `0x0099` | 153 | Photovoltaic 2 voltage | int16_t | 0.1V | Read-only |  |
| ✅ | ✅ | ✅ | pv2_current | `0x009A` | 154 | Photovoltaic 2 Current | int16_t | 0.01A | Read-only |  |
| ✅ | ✅ | ✅ | pv2_power | `0x009B` | 155 | Photovoltaic 2 power | int16_t | 1W | Read-only |  |
| ✅ |  | ✅ | pv_energy_today | `0x009C` | 156 | Photovoltaic power generation on that day | uint16_t | 100Wh | Read-only |  |
| ✅ |  | ✅ | pv_energy_total | `0x009D` | 157 | Total photovoltaic power generation | uint16_t | 100Wh | Read-only |  |
|  |  |  |  | `0x009E` | 158 |  |  |  |  |  |
|  |  |  |  | `0x009F` | 159 |  |  |  |  |  |

---

### WF_WorkMode

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ | ✅ |  |  | `0x0140` | 320 | Work mode |  |  | Read-only |  |
| ✅ | ✅ |  |  | `0x0140` | 320 | Output mode | uint16_t |  | Read-only | 0: APP Mode; 1: UPS Mode; 2: GEN Mode (supported by some models) |
| ✅ |  |  |  | `0x0141` | 321 | Parallel mode | uint16_t |  | Read-only | 0: Single-phase mode; 1: Single-phase parallel operation; 2: Three-phase parallel operation (phase A); 3: Three-phase parallel ... |
| ✅ |  |  |  | `0x0142` | 322 | Output priority | uint16_t |  | Read-only | 0: GBP 1: PGB 2: PBG 3: MKP (Supported by some models) |
| ✅ |  |  |  | `0x0143` | 323 | Charging priority | uint16_t |  | Read-only | 0: PNG 1: OPV 2: PVF (Supported by some models) |
| ✅ |  |  |  | `0x0144` | 324 | State machine states | uint16_t |  | Read-only | 0: Power On 1: Initialization 2: Standby Mode 3: AC Power Mode 4: Solar Power Mode 5: Battery Mode 6: Generator Mode 7: Fault M... |
|  |  |  |  | `0x0145` | 325 |  |  |  |  |  |
|  |  |  |  | `0x0146` | 326 |  |  |  |  |  |
|  |  |  |  | `0x0147` | 327 |  |  |  |  |  |
|  |  |  |  | `0x0148` | 328 |  |  |  |  |  |
|  |  |  |  | `0x0149` | 329 |  |  |  |  |  |
|  |  |  |  | `0x014A` | 330 |  |  |  |  |  |
|  |  |  |  | `0x014B` | 331 |  |  |  |  |  |
|  |  |  |  | `0x014C` | 332 |  |  |  |  |  |
|  |  |  |  | `0x014D` | 333 |  |  |  |  |  |
|  |  |  |  | `0x014E` | 334 |  |  |  |  |  |
|  |  |  |  | `0x014F` | 335 |  |  |  |  |  |

---

### WF_BAT

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x0150` | 336 | Battery information address set |  |  |  |  |
| ✅ |  |  |  | `0x0150` | 336 | Battery Type | uint16_t |  | Read-only | 0: Lead-acid battery; 1: Water-filled battery; 2: Ternary lithium battery; 3: Lithium iron phosphate battery; 4: Custom battery. |
| ✅ |  |  |  | `0x0151` | 337 |  |  |  | Read-only |  |
| ✅ |  |  |  | `0x0152` | 338 | Battery percentage | int16_t | 1% | Read-only |  |
| ✅ |  |  |  | `0x0153` | 339 |  |  |  | Read-only |  |
| ✅ |  |  |  | `0x0154` | 340 | Positive bus voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0155` | 341 | Positive terminal battery voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0156` | 342 | Negative battery discharge current | int16_t | 0.1A | Read-only |  |
| ✅ |  |  |  | `0x0157` | 343 | Positive terminal battery charging current | int16_t | 0.1A | Read-only |  |
| ✅ |  |  |  | `0x0158` | 344 | Positive overvoltage alarm voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0159` | 345 | Positive terminal low voltage alarm voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x015A` | 346 |  |  |  |  |  |
| ✅ |  |  |  | `0x015B` | 347 |  |  |  |  |  |
| ✅ |  |  |  | `0x015C` | 348 | Positive terminal dual-channel output cutoff voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x015D` | 349 | Positive dual-channel output cutoff time | uint16_t | 1H | Read-only |  |
| ✅ |  |  |  | `0x015E` | 350 | Positive battery power | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x015F` | 351 |  |  |  |  |  |
| ✅ |  |  |  | `0x0160` | 352 |  |  |  |  |  |
| ✅ |  |  |  | `0x0161` | 353 |  |  |  |  |  |
| ✅ |  |  |  | `0x0162` | 354 |  |  |  |  |  |
| ✅ |  |  |  | `0x0163` | 355 |  |  |  |  |  |
| ✅ |  |  |  | `0x0164` | 356 | Negative bus voltage | int16_t |  | Read-only |  |
| ✅ |  |  |  | `0x0165` | 357 | Negative battery voltage | int16_t |  | Read-only |  |
| ✅ |  |  |  | `0x0166` | 358 | Negative battery discharge current | int16_t | 0.1A | Read-only |  |
| ✅ |  |  |  | `0x0167` | 359 | Negative battery charging current | int16_t | 0.1A | Read-only |  |
| ✅ |  |  |  | `0x0168` | 360 | Overvoltage alarm voltage at negative terminal | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0169` | 361 | Negative terminal low voltage alarm voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x016A` | 362 |  |  |  |  |  |
| ✅ |  |  |  | `0x016B` | 363 |  |  |  |  |  |
| ✅ |  |  |  | `0x016C` | 364 | Negative terminal dual-channel output cutoff voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x016D` | 365 | Negative-end dual-channel output cutoff time | uint16_t | 1H | Read-only |  |
| ✅ |  |  |  | `0x016E` | 366 | Negative battery power | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x016F` | 367 |  |  |  |  |  |
| ✅ |  |  |  | `0x0170` | 368 |  |  |  |  |  |
| ✅ |  |  |  | `0x0171` | 369 |  |  |  |  |  |
| ✅ |  |  |  | `0x0172` | 370 |  |  |  |  |  |
| ✅ |  |  |  | `0x0173` | 371 |  |  |  |  |  |
| ✅ |  |  |  | `0x0174` | 372 |  |  |  |  |  |
| ✅ |  |  |  | `0x0175` | 373 |  |  |  |  |  |
| ✅ |  |  |  | `0x0176` | 374 | Charging status | uint16_t |  | Read-only | 0: No charging; 1: Constant voltage and constant current charging; 2: Float charging; 3: Balanced charging. |
| ✅ |  |  |  | `0x0177` | 375 | Constant voltage charging | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0178` | 376 | Float charging voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0179` | 377 | Constant voltage charging current | int16_t | 0.1A | Read-only |  |
| ✅ |  |  |  | `0x017A` | 378 | float charging current | int16_t | 0.1A | Read-only |  |
| ✅ |  |  |  | `0x017B` | 379 | Longest constant current charging time | uint16_t | 1H | Read-only |  |
| ✅ |  |  |  | `0x017C` | 380 | Longest constant voltage charging time | uint16_t | 1H | Read-only |  |
| ✅ |  |  |  | `0x017D` | 381 |  |  |  |  |  |
| ✅ |  |  |  | `0x017E` | 382 | Equalizing charging voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x017F` | 383 | Equalization charging time | uint16_t | 1H | Read-only |  |
| ✅ |  |  |  | `0x0180` | 384 | Equalization charging delay time | uint16_t | 1H | Read-only |  |
| ✅ |  |  |  | `0x0181` | 385 | Equalizing charging interval time | uint16_t | 1D | Read-only |  |
| ✅ |  |  |  | `0x0182` | 386 |  |  |  |  |  |
| ✅ |  |  |  | `0x0183` | 387 | Equalization Interval Time Counter | uint16_t | 1H | Read-only |  |
|  |  |  |  | `0x0184` | 388 |  |  |  |  |  |
|  |  |  |  | `0x0185` | 389 |  |  |  |  |  |
|  |  |  |  | `0x0186` | 390 |  |  |  |  |  |
|  |  |  |  | `0x0187` | 391 |  |  |  |  |  |
|  |  |  |  | `0x0188` | 392 |  |  |  |  |  |
|  |  |  |  | `0x0189` | 393 |  |  |  |  |  |
|  |  |  |  | `0x018A` | 394 |  |  |  |  |  |
|  |  |  |  | `0x018B` | 395 |  |  |  |  |  |
|  |  |  |  | `0x018C` | 396 |  |  |  |  |  |
|  |  |  |  | `0x018D` | 397 |  |  |  |  |  |
|  |  |  |  | `0x018E` | 398 |  |  |  |  |  |
|  |  |  |  | `0x018F` | 399 |  |  |  |  |  |

---

### WF_BMS

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x0190` | 400 | BMS Debug Address Set |  |  |  |  |
| ✅ |  |  |  | `0x0190` | 400 | Communication Protocol | uint16_t |  | Read-only | reserve |
| ✅ |  |  |  | `0x0191` | 401 | Communication status | uint16_t |  | Read-only | 0: ID search in progress 1: ID remote lock 2: ID lock |
| ✅ |  |  |  | `0x0192` | 402 | Package ID | uint16_t |  | Read-only |  |
| ✅ |  |  |  | `0x0193` | 403 | Voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0194` | 404 | Current | int16_t | 0.1A | Read-only |  |
| ✅ | ✅ |  |  | `0x0195` | 405 | temperature | int16_t | 1℃ | Read-only |  |
| ✅ | ✅ |  |  | `0x0196` | 406 | SOC | int16_t | % | Read-only |  |
| ✅ | ✅ |  |  | `0x0197` | 407 | SOH | int16_t | % | Read-only |  |
| ✅ |  |  |  | `0x0198` | 408 | Current capacity | uint16_t | 10mAH | Read-only |  |
| ✅ |  |  |  | `0x0199` | 409 | Full charge capacity | uint16_t | 10mAH | Read-only |  |
| ✅ |  |  |  | `0x019A` | 410 | CV points | int16_t | 0.1V | Read-only |  |
| ✅ | ✅ |  |  | `0x019B` | 411 | Maximum charging current | int16_t | 0.01A | Read-only |  |
| ✅ | ✅ |  |  | `0x019C` | 412 | Maximum discharge current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x019D` | 413 | Low SOC alarm points | int16_t | % | Read-only |  |
| ✅ |  |  |  | `0x019E` | 414 | Low SOC shutdown point | int16_t | % | Read-only |  |
| ✅ |  |  |  | `0x019F` | 415 | Low SOC switching point | int16_t | 0.1V | Read-only | reserve |
| ✅ |  |  |  | `0x01A0` | 416 | High SOC cut battery power | int16_t | 0.1V | Read-only | reserve |
| ✅ |  |  |  | `0x01A1` | 417 | Alarm | uint16_t |  | Read-only |  |
| ✅ |  |  |  | `0x01A2` | 418 | mistake | uint16_t |  | Read-only |  |
|  |  |  |  | `0x01A3` | 419 |  |  |  |  |  |
|  |  |  |  | `0x01A4` | 420 |  |  |  |  |  |
|  |  |  |  | `0x01A5` | 421 |  |  |  |  |  |
|  |  |  |  | `0x01A6` | 422 |  |  |  |  |  |
|  |  |  |  | `0x01A7` | 423 |  |  |  |  |  |
|  |  |  |  | `0x01A8` | 424 |  |  |  |  |  |
|  |  |  |  | `0x01A9` | 425 |  |  |  |  |  |
|  |  |  |  | `0x01AA` | 426 |  |  |  |  |  |
|  |  |  |  | `0x01AB` | 427 |  |  |  |  |  |
|  |  |  |  | `0x01AC` | 428 |  |  |  |  |  |
|  |  |  |  | `0x01AD` | 429 |  |  |  |  |  |
|  |  |  |  | `0x01AE` | 430 |  |  |  |  |  |
|  |  |  |  | `0x01AF` | 431 |  |  |  |  |  |

---

### WF_LINE

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  | ✅ | line_grid_voltage | `0x01B0` | 432 | Mains power status debugging address set |  |  |  |  |
| ✅ |  | ✅ | line_grid_voltage | `0x01B0` | 432 | Phase A mains voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  | ✅ | line_grid_current | `0x01B1` | 433 | Phase A mains current | int16_t | 0.01A | Read-only |  |
| ✅ |  | ✅ | line_grid_frequency | `0x01B2` | 434 | Phase A mains frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  | ✅ | line_grid_power | `0x01B3` | 435 | Phase A mains power | int16_t | 10W | Read-only |  |
| ✅ |  | ✅ | line_grid_consumption_power | `0x01B4` | 436 | Phase A AC power (electricity consumption only) | int16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x01B5` | 437 |  |  |  |  |  |
| ✅ |  |  |  | `0x01B6` | 438 |  |  |  |  |  |
| ✅ |  | ✅ | grid_feedin_today | `0x01B7` | 439 | A. Equivalent daily municipal power grid supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | grid_feedin_today+1 | `0x01B8` | 440 | A. Equivalent daily municipal power grid total L | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | grid_feedin_month | `0x01B9` | 441 | A is equivalent to the total monthly municipal power grid supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | grid_feedin_month+1 | `0x01BA` | 442 | A is equivalent to the total monthly power grid supply L | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | grid_feedin_year | `0x01BB` | 443 | A is equivalent to the total annual municipal power grid supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | grid_feedin_year+1 | `0x01BC` | 444 | A is equivalent to the total amount of municipal power grid feeder in a given year. | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | grid_feedin_total | `0x01BD` | 445 | The total power supply to the mains grid in phase A is H | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | grid_feedin_total+1 | `0x01BE` | 446 | Total A-phase mains power supply L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | grid_consumption_today | `0x01BF` | 447 | A. Equivalent daily electricity consumption H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | grid_consumption_today+1 | `0x01C0` | 448 | A is equivalent to the total daily electricity consumption L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | grid_consumption_month | `0x01C1` | 449 | A is equivalent to H, the total monthly electricity consumption. | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | grid_consumption_month+1 | `0x01C2` | 450 | A is equivalent to the total monthly electricity consumption L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | grid_consumption_year | `0x01C3` | 451 | A. Equivalent annual total municipal electricity consumption H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | grid_consumption_year+1 | `0x01C4` | 452 | A is equivalent to the total annual electricity consumption of the municipality. | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | grid_consumption_total | `0x01C5` | 453 | Total electricity consumption of phase A by the mains H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | grid_consumption_total+1 | `0x01C6` | 454 | Total electricity consumption of phase A (L) | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01C7` | 455 |  |  |  |  |  |
| ✅ |  |  |  | `0x01C8` | 456 |  |  |  |  |  |
| ✅ |  |  |  | `0x01C9` | 457 |  |  |  |  |  |
| ✅ |  |  |  | `0x01CA` | 458 |  |  |  |  |  |
| ✅ |  |  |  | `0x01CB` | 459 |  |  |  |  |  |
| ✅ |  |  |  | `0x01CC` | 460 |  |  |  |  |  |
| ✅ |  |  |  | `0x01CD` | 461 |  |  |  |  |  |
| ✅ |  |  |  | `0x01CE` | 462 |  |  |  |  |  |
| ✅ |  |  |  | `0x01CF` | 463 |  |  |  |  |  |
| ✅ |  |  |  | `0x01D0` | 464 | Phase B mains voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x01D1` | 465 | Phase B mains current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x01D2` | 466 | Phase B mains frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x01D3` | 467 | Phase B AC power | int16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x01D4` | 468 | Phase B AC power (power consumption only) | int16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x01D5` | 469 |  |  |  |  |  |
| ✅ |  |  |  | `0x01D6` | 470 |  |  |  |  |  |
| ✅ |  |  |  | `0x01D7` | 471 | B is equivalent to the total daily power supply to the municipal power grid. | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01D8` | 472 | B is equivalent to the total daily power supply to the municipal power grid. | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01D9` | 473 | B is equivalent to the total monthly power grid supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01DA` | 474 | B is equivalent to the total monthly power grid supply L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01DB` | 475 | B is equivalent to the total annual municipal power grid supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01DC` | 476 | B is equivalent to the total annual municipal power grid supply L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01DD` | 477 | Total B-phase mains power supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01DE` | 478 | Total B-phase mains power supply L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01DF` | 479 | B is equivalent to H's daily total electricity consumption. | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01E0` | 480 | B is equivalent to the daily total electricity consumption L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01E1` | 481 | B is equivalent to the total monthly electricity consumption H. | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01E2` | 482 | B is equivalent to the total monthly electricity consumption L. | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01E3` | 483 | B is equivalent to the total annual municipal electricity consumption H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01E4` | 484 | B is equivalent to the total annual electricity consumption of the municipality. | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01E5` | 485 | Total electricity consumption of phase B from the mains H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01E6` | 486 | Total electricity consumption of phase B (L) | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01E7` | 487 |  |  |  |  |  |
| ✅ |  |  |  | `0x01E8` | 488 |  |  |  |  |  |
| ✅ |  |  |  | `0x01E9` | 489 |  |  |  |  |  |
| ✅ |  |  |  | `0x01EA` | 490 |  |  |  |  |  |
| ✅ |  |  |  | `0x01EB` | 491 |  |  |  |  |  |
| ✅ |  |  |  | `0x01EC` | 492 |  |  |  |  |  |
| ✅ |  |  |  | `0x01ED` | 493 |  |  |  |  |  |
| ✅ |  |  |  | `0x01EE` | 494 |  |  |  |  |  |
| ✅ |  |  |  | `0x01EF` | 495 |  |  |  |  |  |
| ✅ |  |  |  | `0x01F0` | 496 | C-phase mains voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x01F1` | 497 | C-phase mains current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x01F2` | 498 | C-phase mains frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x01F3` | 499 | C-phase mains power | int16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x01F4` | 500 | C-phase AC power (power consumption only) | int16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x01F5` | 501 |  |  |  |  |  |
| ✅ |  |  |  | `0x01F6` | 502 |  |  |  |  |  |
| ✅ |  |  |  | `0x01F7` | 503 | C Equivalent daily municipal power grid total H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01F8` | 504 | C Equivalent daily municipal power grid total L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01F9` | 505 | C is equivalent to the total monthly municipal power grid supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01FA` | 506 | C is equivalent to the total monthly municipal power grid supply L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01FB` | 507 | C is equivalent to the total annual municipal power grid supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01FC` | 508 | is equivalent to the total annual municipal power grid supply L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01FD` | 509 | Total C-phase mains power supply H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01FE` | 510 | Total C-phase mains power supply L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x01FF` | 511 | C Equivalent daily electricity consumption H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0200` | 512 | C is equivalent to the total daily electricity consumption L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0201` | 513 | C is equivalent to the total monthly electricity consumption H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0202` | 514 | C is equivalent to the total monthly electricity consumption L | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0203` | 515 | C is equivalent to the total annual electricity consumption of the municipality. | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0204` | 516 | C is equivalent to the total annual electricity consumption of the municipality. | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0205` | 517 | Total C-phase mains power consumption H | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0206` | 518 | Total C-phase mains power consumption L | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0207` | 519 |  |  |  |  |  |
|  |  |  |  | `0x0208` | 520 |  |  |  |  |  |
|  |  |  |  | `0x0209` | 521 |  |  |  |  |  |
|  |  |  |  | `0x020A` | 522 |  |  |  |  |  |
|  |  |  |  | `0x020B` | 523 |  |  |  |  |  |
|  |  |  |  | `0x020C` | 524 |  |  |  |  |  |
|  |  |  |  | `0x020D` | 525 |  |  |  |  |  |
|  |  |  |  | `0x020E` | 526 |  |  |  |  |  |
|  |  |  |  | `0x020F` | 527 |  |  |  |  |  |

---

### WF_OP

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  | ✅ | output_priority | `0x0210` | 528 | Output debug address set |  |  |  |  |
| ✅ |  | ✅ | output_priority | `0x0210` | 528 | Output priority | uint16_t |  | Read-only | 0:GPB 1:PGB 2:PBG 3:MKS |
| ✅ |  | ✅ | operating_mode | `0x0211` | 529 | Operating mode | uint16_t |  | Read-only | 0:APP 1:UPS 2:GEN |
| ✅ |  |  |  | `0x0212` | 530 |  |  |  |  |  |
| ✅ |  |  |  | `0x0213` | 531 |  |  |  |  |  |
| ✅ |  |  |  | `0x0214` | 532 |  |  |  |  |  |
| ✅ |  |  |  | `0x0215` | 533 |  |  |  |  |  |
| ✅ |  |  |  | `0x0216` | 534 |  |  |  |  |  |
| ✅ |  |  |  | `0x0217` | 535 |  |  |  |  |  |
| ✅ |  | ✅ | output_voltage | `0x0218` | 536 | A-phase output voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  | ✅ | output_frequency | `0x0219` | 537 | Phase A output frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  | ✅ | output_current | `0x021A` | 538 | Phase A output current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x021B` | 539 | Phase A outputs a small current. | int16_t | 0.01A | Read-only | reserve |
| ✅ |  | ✅ | output_active_power | `0x021C` | 540 | Phase A output active power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x021D` | 541 | Apparent power output of phase A | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x021E` | 542 |  |  |  |  |  |
| ✅ |  |  |  | `0x021F` | 543 |  |  |  |  |  |
| ✅ |  | ✅ | output_load_pct | `0x0220` | 544 | Phase A load percentage | int16_t | 0.1% | Read-only |  |
| ✅ | ✅ | ✅ | output_energy_today | `0x0221` | 545 | A equivalent daily output power H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | output_energy_today+1 | `0x0222` | 546 | A equivalent daily output power L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | output_energy_month | `0x0223` | 547 | A is equivalent to monthly output power H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | output_energy_month+1 | `0x0224` | 548 | A is equivalent to monthly power output L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | output_energy_year | `0x0225` | 549 | A equivalent annual power output H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | output_energy_year+1 | `0x0226` | 550 | A equivalent annual power output L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | output_energy_total | `0x0227` | 551 | Phase A total output power H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | output_energy_total+1 | `0x0228` | 552 | Phase A total output power L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0229` | 553 |  |  |  |  |  |
| ✅ |  |  |  | `0x022A` | 554 |  |  |  |  |  |
| ✅ |  |  |  | `0x022B` | 555 |  |  |  |  |  |
| ✅ |  |  |  | `0x022C` | 556 |  |  |  |  |  |
| ✅ |  |  |  | `0x022D` | 557 |  |  |  |  |  |
| ✅ |  |  |  | `0x022E` | 558 |  |  |  |  |  |
| ✅ |  |  |  | `0x022F` | 559 |  |  |  |  |  |
| ✅ |  |  |  | `0x0230` | 560 | B-phase output voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0231` | 561 | B-phase output frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x0232` | 562 | B-phase output current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x0233` | 563 | B-phase outputs a small current. | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x0234` | 564 | Phase B output active power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x0235` | 565 | Phase B output apparent power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x0236` | 566 |  |  |  |  |  |
| ✅ |  |  |  | `0x0237` | 567 |  |  |  |  |  |
| ✅ |  |  |  | `0x0238` | 568 | Phase B load percentage | int16_t | 0.1% | Read-only |  |
| ✅ |  |  |  | `0x0239` | 569 | B is equivalent to daily output power H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x023A` | 570 | B is equivalent to daily output power L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x023B` | 571 | B is equivalent to monthly output power H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x023C` | 572 | B is equivalent to monthly output power L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x023D` | 573 | B is equivalent to annual power output H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x023E` | 574 | B is equivalent to annual power output L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x023F` | 575 | Phase B total output power H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0240` | 576 | Phase B total output power L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0241` | 577 |  |  |  |  |  |
| ✅ |  |  |  | `0x0242` | 578 |  |  |  |  |  |
| ✅ |  |  |  | `0x0243` | 579 |  |  |  |  |  |
| ✅ |  |  |  | `0x0244` | 580 |  |  |  |  |  |
| ✅ |  |  |  | `0x0245` | 581 |  |  |  |  |  |
| ✅ |  |  |  | `0x0246` | 582 |  |  |  |  |  |
| ✅ |  |  |  | `0x0247` | 583 |  |  |  |  |  |
| ✅ |  |  |  | `0x0248` | 584 | C-phase output voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0249` | 585 | C-phase output frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x024A` | 586 | C-phase output current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x024B` | 587 | C-phase outputs a small current. | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x024C` | 588 | C-phase output active power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x024D` | 589 | C-phase output apparent power | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x024E` | 590 |  |  |  |  |  |
| ✅ |  |  |  | `0x024F` | 591 |  |  |  |  |  |
| ✅ |  |  |  | `0x0250` | 592 | C-phase load percentage | int16_t | 0.1% | Read-only |  |
| ✅ |  |  |  | `0x0251` | 593 | C is equivalent to daily output power H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0252` | 594 | C Equivalent daily output power L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0253` | 595 | C is equivalent to monthly output power H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0254` | 596 | C is equivalent to monthly output power L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0255` | 597 | C equivalent annual power output H | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x0256` | 598 | C is equivalent to annual power output L | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0257` | 599 | C-phase total output power H | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0258` | 600 | C-phase total output power L | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0259` | 601 |  |  |  |  |  |
|  |  |  |  | `0x025A` | 602 |  |  |  |  |  |
|  |  |  |  | `0x025B` | 603 |  |  |  |  |  |
|  |  |  |  | `0x025C` | 604 |  |  |  |  |  |
|  |  |  |  | `0x025D` | 605 |  |  |  |  |  |
|  |  |  |  | `0x025E` | 606 |  |  |  |  |  |
|  |  |  |  | `0x025F` | 607 |  |  |  |  |  |

---

### WF_PV

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  | ✅ | pv_total_voltage | `0x0260` | 608 | Total photovoltaic address set |  |  |  |  |
| ✅ |  | ✅ | pv_total_voltage | `0x0260` | 608 | Total photovoltaic voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  | ✅ | pv_total_current | `0x0261` | 609 | Total photovoltaic current H | int16_t | 0.01A | Read-only |  |
| ✅ |  | ✅ | pv_total_current+1 | `0x0262` | 610 | Total photovoltaic current L | int16_t | 0.01A | Read-only |  |
| ✅ |  | ✅ | pv_total_power | `0x0263` | 611 | Total photovoltaic power H | int16_t | 1W | Read-only |  |
| ✅ |  |  |  | `0x0264` | 612 | Total photovoltaic power L | int16_t | 1W | Read-only |  |
| ✅ |  | ✅ | pv_total_tracking_status | `0x0265` | 613 | Total Solar Tracking Status | int16_t |  | Read-only |  |
| ✅ |  | ✅ | pv_total_rechargeable_state | `0x0266` | 614 | Total state of solar power rechargeability | int16_t |  | Read-only |  |
| ✅ | ✅ | ✅ | pv_energy_today_total | `0x0267` | 615 | Total photovoltaic power generation H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | pv_energy_today_total+1 | `0x0268` | 616 | Total photovoltaic power generation L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | pv_energy_month_total | `0x0269` | 617 | Total photovoltaic power generation H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | pv_energy_month_total+1 | `0x026A` | 618 | Total photovoltaic power generation L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | pv_energy_year_total | `0x026B` | 619 | Total photovoltaic power generation H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | pv_energy_year_total+1 | `0x026C` | 620 | Total photovoltaic power generation L | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | pv_energy_all_total | `0x026D` | 621 | Total photovoltaic power generation H | uint16_t | 10Wh | Read-only |  |
| ✅ | ✅ | ✅ | pv_energy_all_total+1 | `0x026E` | 622 | Total photovoltaic power generation L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x026F` | 623 |  |  |  |  |  |
| ✅ |  |  |  | `0x0270` | 624 | Photovoltaic voltage 1 | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0271` | 625 | Photovoltaic 1 current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x0272` | 626 | Photovoltaic power | int16_t | 1W | Read-only |  |
| ✅ |  | ✅ | pv1_tracking_status | `0x0273` | 627 | Photovoltaic 1 tracking status | int16_t |  | Read-only |  |
| ✅ |  | ✅ | pv1_rechargeable_state | `0x0274` | 628 | Photovoltaic 1 Rechargeable State | int16_t |  | Read-only |  |
| ✅ |  | ✅ | pv1_energy_today | `0x0275` | 629 | Photovoltaic power generation H on the day | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | pv1_energy_today+1 | `0x0276` | 630 | Photovoltaic power generation L on the day | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | pv1_energy_month | `0x0277` | 631 | Photovoltaic power generation H in the current month | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | pv1_energy_month+1 | `0x0278` | 632 | Photovoltaic power generation L in the current month | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | pv1_energy_year | `0x0279` | 633 | Photovoltaic power generation H in the current year | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | pv1_energy_year+1 | `0x027A` | 634 | Photovoltaic power generation L in the current year | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | pv1_energy_total | `0x027B` | 635 | Total power generation H of photovoltaic 1 | uint16_t | 10Wh | Read-only |  |
| ✅ |  | ✅ | pv1_energy_total+1 | `0x027C` | 636 | Photovoltaic 1 Total Power Generation L | uint16_t | 10Wh | Read-only |  |
| ✅ |  |  |  | `0x027D` | 637 |  |  |  |  |  |
| ✅ |  |  |  | `0x027E` | 638 |  |  |  |  |  |
| ✅ |  |  |  | `0x027F` | 639 |  |  |  |  |  |
| ✅ |  |  |  | `0x0280` | 640 | Photovoltaic 2 voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x0281` | 641 | Photovoltaic 2 Current | int16_t | 0.01A | Read-only |  |
|  |  |  |  | `0x0282` | 642 | Photovoltaic 2 power | int16_t | 1W | Read-only |  |
|  |  |  |  | `0x0283` | 643 | Photovoltaic 2 tracking status | int16_t |  | Read-only |  |
|  |  |  |  | `0x0284` | 644 | Photovoltaic 2 Rechargeable State | int16_t |  | Read-only |  |
|  |  |  |  | `0x0285` | 645 | Photovoltaic 2's daily power generation H | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0286` | 646 | Photovoltaic 2's daily power generation L | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0287` | 647 | Photovoltaic power generation H in the current month | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0288` | 648 | Photovoltaic power generation L in the current month | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x0289` | 649 | Photovoltaic 2's annual power generation H | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x028A` | 650 | Photovoltaic 2's annual power generation L | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x028B` | 651 | Photovoltaic 2 Total Power Generation H | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x028C` | 652 | Photovoltaic 2 Total Power Generation L | uint16_t | 10Wh | Read-only |  |
|  |  |  |  | `0x028D` | 653 |  |  |  |  |  |
|  |  |  |  | `0x028E` | 654 |  |  |  |  |  |
|  |  |  |  | `0x028F` | 655 |  |  |  |  |  |
|  |  |  |  | `0x0290` | 656 |  |  |  |  |  |
|  |  |  |  | `0x0291` | 657 |  |  |  |  |  |
|  |  |  |  | `0x0292` | 658 |  |  |  |  |  |
|  |  |  |  | `0x0293` | 659 |  |  |  |  |  |
|  |  |  |  | `0x0294` | 660 |  |  |  |  |  |
|  |  |  |  | `0x0295` | 661 |  |  |  |  |  |
|  |  |  |  | `0x0296` | 662 |  |  |  |  |  |
|  |  |  |  | `0x0297` | 663 |  |  |  |  |  |
|  |  |  |  | `0x0298` | 664 |  |  |  |  |  |
|  |  |  |  | `0x0299` | 665 |  |  |  |  |  |
|  |  |  |  | `0x029A` | 666 |  |  |  |  |  |
|  |  |  |  | `0x029B` | 667 |  |  |  |  |  |
|  |  |  |  | `0x029C` | 668 |  |  |  |  |  |
|  |  |  |  | `0x029D` | 669 |  |  |  |  |  |
|  |  |  |  | `0x029E` | 670 |  |  |  |  |  |
|  |  |  |  | `0x029F` | 671 |  |  |  |  |  |

---

### WF_INV

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x02A0` | 672 | Inverted address set |  |  |  |  |
| ✅ |  |  |  | `0x02A0` | 672 | Inverter voltage setting value | int16_t | 0.1Hz | Read-only |  |
| ✅ |  |  |  | `0x02A1` | 673 | Inverter frequency setting value | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x02A2` | 674 |  |  |  |  |  |
| ✅ |  |  |  | `0x02A3` | 675 |  |  |  |  |  |
| ✅ |  |  |  | `0x02A4` | 676 |  |  |  |  |  |
| ✅ |  |  |  | `0x02A5` | 677 |  |  |  |  |  |
| ✅ |  |  |  | `0x02A6` | 678 |  |  |  |  |  |
| ✅ |  |  |  | `0x02A7` | 679 |  |  |  |  |  |
| ✅ |  |  |  | `0x02A8` | 680 |  |  |  |  |  |
| ✅ |  |  |  | `0x02A9` | 681 |  |  |  |  |  |
| ✅ |  |  |  | `0x02AA` | 682 | A-phase inverter voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x02AB` | 683 | A-phase inverter frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x02AC` | 684 | A-phase inverter current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x02AD` | 685 | Phase A DC component | int16_t | 1mV | Read-only |  |
| ✅ |  |  |  | `0x02AE` | 686 | Phase A Daily Input Power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02AF` | 687 | Phase A Daily Input Power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B0` | 688 | Phase A Monthly Input Power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B1` | 689 | Phase A Monthly Input Power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B2` | 690 | Phase A total input power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B3` | 691 | Phase A total input power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B4` | 692 | Phase A daily output power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B5` | 693 | Phase A daily output power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B6` | 694 | Phase A output power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B7` | 695 | Phase A output power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B8` | 696 | Phase A total output power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02B9` | 697 | Phase A total output power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02BA` | 698 | B-phase inverter voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x02BB` | 699 | B-phase inverter frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x02BC` | 700 | B-phase inverter current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x02BD` | 701 | Phase B DC component | int16_t | 1mV | Read-only |  |
| ✅ |  |  |  | `0x02BE` | 702 |  |  |  |  |  |
| ✅ |  |  |  | `0x02BF` | 703 |  |  |  |  |  |
| ✅ |  |  |  | `0x02C0` | 704 | B-phase daily feeder power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02C1` | 705 | B-phase daily feeder power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02C2` | 706 | B-phase monthly feeder power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02C3` | 707 | B-phase monthly feeder power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02C4` | 708 | B-phase total grid power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02C5` | 709 | B-phase total power supply L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02C6` | 710 |  |  |  |  |  |
| ✅ |  |  |  | `0x02C7` | 711 |  |  |  |  |  |
| ✅ |  |  |  | `0x02C8` | 712 |  |  |  |  |  |
| ✅ |  |  |  | `0x02C9` | 713 |  |  |  |  |  |
| ✅ |  |  |  | `0x02CA` | 714 | C-phase inverter voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x02CB` | 715 | C-phase inverter frequency | int16_t | 0.01Hz | Read-only |  |
| ✅ |  |  |  | `0x02CC` | 716 | C-phase inverter current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x02CD` | 717 | C-phase DC component | int16_t | 1mV | Read-only |  |
| ✅ |  |  |  | `0x02CE` | 718 |  |  |  |  |  |
| ✅ |  |  |  | `0x02CF` | 719 |  |  |  |  |  |
| ✅ |  |  |  | `0x02D0` | 720 | C-phase daily feeder power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02D1` | 721 | C-phase daily feeder power L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02D2` | 722 | C-phase monthly feeder power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02D3` | 723 | C-phase monthly power supply L | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02D4` | 724 | C-phase total grid power H | uint16_t | 10W | Read-only |  |
| ✅ |  |  |  | `0x02D5` | 725 | C-phase total grid power L | uint16_t | 10W | Read-only |  |
|  |  |  |  | `0x02D6` | 726 |  |  |  |  |  |
|  |  |  |  | `0x02D7` | 727 |  |  |  |  |  |
|  |  |  |  | `0x02D8` | 728 |  |  |  |  |  |
|  |  |  |  | `0x02D9` | 729 |  |  |  |  |  |
|  |  |  |  | `0x02DA` | 730 |  |  |  |  |  |
|  |  |  |  | `0x02DB` | 731 |  |  |  |  |  |
|  |  |  |  | `0x02DC` | 732 |  |  |  |  |  |
|  |  |  |  | `0x02DD` | 733 |  |  |  |  |  |
|  |  |  |  | `0x02DE` | 734 |  |  |  |  |  |
|  |  |  |  | `0x02DF` | 735 |  |  |  |  |  |

---

### WF_NTC

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  | ✅ | temp_pv | `0x0330` | 816 | Temperature address set |  |  |  |  |
| ✅ |  | ✅ | temp_pv | `0x0330` | 816 | PV temperature |  | ℃ | Read-only |  |
| ✅ |  | ✅ | temp_inv | `0x0331` | 817 | INV temperature |  | ℃ | Read-only |  |
| ✅ |  | ✅ | temp_chg | `0x0332` | 818 | CHG temperature |  | ℃ | Read-only |  |
| ✅ |  | ✅ | temp_chg2 | `0x0333` | 819 | CHG2 temperature |  | ℃ | Read-only |  |
| ✅ |  | ✅ | temp_ambient | `0x0334` | 820 | Ambient temperature |  | ℃ | Read-only |  |
|  |  | ✅ | temp_dis_chg | `0x0335` | 821 | DIS_CHG temperature |  | ℃ | Read-only |  |
|  |  |  |  | `0x0336` | 822 |  |  |  |  |  |
|  |  |  |  | `0x0337` | 823 |  |  |  |  |  |
|  |  |  |  | `0x0338` | 824 |  |  |  |  |  |
|  |  |  |  | `0x0339` | 825 |  |  |  |  |  |
|  |  |  |  | `0x033A` | 826 |  |  |  |  |  |
|  |  |  |  | `0x033B` | 827 |  |  |  |  |  |
|  |  |  |  | `0x033C` | 828 |  |  |  |  |  |
|  |  |  |  | `0x033D` | 829 |  |  |  |  |  |
|  |  |  |  | `0x033E` | 830 |  |  |  |  |  |
|  |  |  |  | `0x033F` | 831 |  |  |  |  |  |

---

### WF_FAN

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  | ✅ | fan_speed | `0x0320` | 800 | Fan information address set |  |  |  |  |
| ✅ |  | ✅ | fan_speed | `0x0320` | 800 | Fan speed |  | % | Read-only |  |
| ✅ |  | ✅ | fan_fault | `0x0321` | 801 | Fan status |  |  | Read-only | A non-zero value indicates a stalled turn. |
|  |  |  |  | `0x0322` | 802 |  |  |  |  |  |
|  |  |  |  | `0x0323` | 803 |  |  |  |  |  |

---

### WF_FunctionSwitch

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x0350` | 848 | Special function switch address set |  |  |  |  |
| ✅ |  |  |  | `0x0350` | 848 | Factory reset function0 H |  | BIT00: Enable SOC... | Read-only |  |
| ✅ |  |  |  | `0x0351` | 849 | Factory reset function available. |  | BIT00: LCD timeou... | Read-only |  |
| ✅ |  |  |  | `0x0352` | 850 | Factory reset function1 H |  | Reserved | Read-only |  |
| ✅ |  |  |  | `0x0353` | 851 | Factory reset function 1 L |  | Reserved | Read-only |  |
| ✅ |  |  |  | `0x0354` | 852 | Factory reset function0 H |  | Reserved | Read-only |  |
| ✅ |  |  |  | `0x0355` | 853 | Factory reset function is not available. |  | Reserved | Read-only |  |
| ✅ |  |  |  | `0x0356` | 854 | Factory reset function1 H |  | Reserved | Read-only |  |
| ✅ |  |  |  | `0x0357` | 855 | Unrestored factory settings function 1 L |  | Reserved | Read-only |  |
|  |  |  |  | `0x0358` | 856 |  |  |  |  |  |
|  |  |  |  | `0x0359` | 857 |  |  |  |  |  |
|  |  |  |  | `0x035A` | 858 |  |  |  |  |  |
|  |  |  |  | `0x035B` | 859 |  |  |  |  |  |
|  |  |  |  | `0x035C` | 860 |  |  |  |  |  |
|  |  |  |  | `0x035D` | 861 |  |  |  |  |  |
|  |  |  |  | `0x035E` | 862 |  |  |  |  |  |
|  |  |  |  | `0x035F` | 863 |  |  |  |  |  |

---

### WF_Time

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x0360` | 864 | Time address set |  |  |  |  |
| ✅ |  |  |  | `0x0360` | 864 | Year |  |  | Read-only |  |
| ✅ |  |  |  | `0x0361` | 865 | moon |  |  | Read-only |  |
| ✅ |  |  |  | `0x0362` | 866 | day |  |  | Read-only |  |
| ✅ |  |  |  | `0x0363` | 867 | hour |  |  | Read-only |  |
| ✅ |  |  |  | `0x0364` | 868 | point |  |  | Read-only |  |
| ✅ |  |  |  | `0x0365` | 869 | Second |  |  | Read-only |  |
|  |  |  |  | `0x0366` | 870 |  |  |  |  |  |
|  |  |  |  | `0x0367` | 871 |  |  |  |  |  |

---

### WF_PARA

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
|  |  |  |  | `0x0400` | 1024 |  |  |  |  |  |
|  |  |  |  | `0x0400` | 1024 |  |  |  |  |  |

---

### WF_Generator

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x2000` | 8192 | Generator status debugging address set |  |  |  |  |
| ✅ |  |  |  | `0x2000` | 8192 | Phase A generator voltage | int16_t | 0.1V | Read-only |  |
| ✅ |  |  |  | `0x2001` | 8193 | Phase A generator current | int16_t | 0.01A | Read-only |  |
| ✅ |  |  |  | `0x2002` | 8194 | Phase A generator frequency | int16_t | 0.01Hz | Read-only |  |
|  |  |  |  | `0x2003` | 8195 | A-phase generator power | int16_t | 10W | Read-only |  |
|  |  |  |  | `0x2004` | 8196 |  |  |  |  |  |
|  |  |  |  | `0x2005` | 8197 |  |  |  |  |  |
|  |  |  |  | `0x2006` | 8198 |  |  |  |  |  |
|  |  |  |  | `0x2007` | 8199 |  |  |  |  |  |
|  |  |  |  | `0x2008` | 8200 |  |  |  |  |  |
|  |  |  |  | `0x2009` | 8201 |  |  |  |  |  |
|  |  |  |  | `0x200A` | 8202 |  |  |  |  |  |
|  |  |  |  | `0x200B` | 8203 |  |  |  |  |  |
|  |  |  |  | `0x200C` | 8204 |  |  |  |  |  |
|  |  |  |  | `0x200D` | 8205 |  |  |  |  |  |
|  |  |  |  | `0x200E` | 8206 |  |  |  |  |  |
|  |  |  |  | `0x200F` | 8207 |  |  |  |  |  |

---

### WF_Admin

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x1000` | 4096 | Settings & Configuration |  |  |  |  |
| ✅ |  |  |  | `0x1000` | 4096 | Factory reset |  |  | Reading and writing | Write 1 to restore to customer customization |
| ✅ |  |  |  | `0x1001` | 4097 | Factory reset |  |  | Reading and writing | Write 1 to clear customer customization |
| ✅ |  |  |  | `0x1002` | 4098 | Factory reset |  |  | Reading and writing | Write 1 to clear calibration information |
| ✅ |  |  |  | `0x1003` | 4099 | SN number written |  |  | Reading and writing | Write 1 to remember the SN number |
| ✅ |  |  |  | `0x1004` | 4100 |  |  |  |  |  |
| ✅ |  |  |  | `0x1005` | 4101 |  |  |  |  |  |
| ✅ |  |  |  | `0x1006` | 4102 |  |  |  |  |  |
| ✅ |  |  |  | `0x1007` | 4103 |  |  |  |  |  |
| ✅ |  |  |  | `0x1008` | 4104 |  |  |  |  |  |
| ✅ |  |  |  | `0x1009` | 4105 |  |  |  | Reading and writing | User mode: 0x0000 Administrator mode: 0x0001 |
| ✅ |  |  |  | `0x100A` | 4106 | Administrator account |  |  | Reading and writing | Without a default setting, users only have query and partial parameter setting permissions. Administrators can set calibration ... |
| ✅ |  |  |  | `0x100B` | 4107 | Administrator password |  |  | Reading and writing |  |
| ✅ |  |  |  | `0x100C` | 4108 | Authorization time |  | s | Reading and writing | 0xFFFF: Perpetual License |
|  |  |  |  | `0x100D` | 4109 |  |  |  |  |  |
|  |  |  |  | `0x100E` | 4110 |  |  |  |  |  |
|  |  |  |  | `0x100F` | 4111 |  |  |  |  |  |
|  |  |  |  | `0x1010` | 4112 |  |  |  |  |  |
|  |  |  |  | `0x1011` | 4113 |  |  |  |  |  |
|  |  |  |  | `0x1012` | 4114 |  |  |  |  |  |
|  |  |  |  | `0x1013` | 4115 |  |  |  |  |  |
|  |  |  |  | `0x1014` | 4116 |  |  |  |  |  |
|  |  |  |  | `0x1015` | 4117 |  |  |  |  |  |
|  |  |  |  | `0x1016` | 4118 |  |  |  |  |  |
|  |  |  |  | `0x1017` | 4119 |  |  |  |  |  |
|  |  |  |  | `0x1018` | 4120 |  |  |  |  |  |
|  |  |  |  | `0x1019` | 4121 |  |  |  |  |  |
|  |  |  |  | `0x101A` | 4122 |  |  |  |  |  |
|  |  |  |  | `0x101B` | 4123 |  |  |  |  |  |
|  |  |  |  | `0x101C` | 4124 |  |  |  |  |  |
|  |  |  |  | `0x101D` | 4125 |  |  |  |  |  |
|  |  |  |  | `0x101E` | 4126 |  |  |  |  |  |
|  |  |  |  | `0x101F` | 4127 |  |  |  |  |  |
|  |  |  |  | `0x1020` | 4128 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1021` | 4129 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1022` | 4130 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1023` | 4131 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1024` | 4132 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1025` | 4133 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1026` | 4134 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1027` | 4135 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1028` | 4136 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x1029` | 4137 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x102A` | 4138 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x102B` | 4139 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x102C` | 4140 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x102D` | 4141 | SN code | uint16_t |  | Read-only |  |
|  |  |  |  | `0x102E` | 4142 | SN code | uint16_t |  | Read-only |  |

---

### WF_FCT

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x1100` | 4352 |  |  |  |  |  |
| ✅ |  |  |  | `0x1100` | 4352 | FCT mode |  |  | Reading and writing | 0: Non-test mode; 1: Driver test mode |
| ✅ |  |  |  | `0x1101` | 4353 | Drive enable | Bit |  | Reading and writing | 0x0000: Off; 0x0001: Discharge; 0x0002: Charge; 0x0004: PFC Driver; 0x0008: Inverter Driver; 0x0010: PV Driver; 0x0020: L-line ... |
| ✅ |  |  |  | `0x1102` | 4354 | Discharge drive percentage |  | 0.0001 | Reading and writing |  |
| ✅ |  |  |  | `0x1103` | 4355 | Charging Drive Percentage |  | 0.0001 | Reading and writing |  |
| ✅ |  |  |  | `0x1104` | 4356 | Inverter drive percentage |  | 0.0001 | Reading and writing |  |
| ✅ |  |  |  | `0x1105` | 4357 | PV-driven percentage |  | 0.0001 | Reading and writing |  |
| ✅ |  |  |  | `0x1106` | 4358 | Relay status |  |  | Reading and writing | BIT0: BIT1: BIT2: |
| ✅ |  |  |  | `0x1107` | 4359 | SCR status |  |  | Reading and writing | BIT0: BIT1: BIT2: |
| ✅ |  |  |  | `0x1108` | 4360 | Fan drive percentage |  | % | Reading and writing |  |
| ✅ |  |  |  | `0x1109` | 4361 | dry contact switch |  |  | Reading and writing |  |
|  |  |  |  | `0x110A` | 4362 | Buzzer switch |  |  | Reading and writing |  |
|  |  |  |  | `0x110B` | 4363 | Factory testing accelerates the transition to charging state. |  |  | Reading and writing | 0: Normal Mode; 1: Factory Test Mode, skips the battery disconnection detection process and accelerates the transition to AC ch... |
|  |  |  |  | `0x110C` | 4364 | Button status |  |  | Reading and writing | BIT0: Up key triggered; BIT1: Down key triggered; BIT2: Confirm key triggered; BIT3: Back key triggered. This bit is reset to z... |
|  |  |  |  | `0x110D` | 4365 |  |  |  |  |  |
|  |  |  |  | `0x110E` | 4366 |  |  |  |  |  |
|  |  |  |  | `0x110F` | 4367 |  |  |  |  |  |
|  |  |  |  | `0x1110` | 4368 |  |  |  |  |  |
|  |  |  |  | `0x1111` | 4369 |  |  |  |  |  |
|  |  |  |  | `0x1112` | 4370 |  |  |  |  |  |

---

### WF_Calibration

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  |  |  | `0x1200` | 4608 | Calibration information |  |  |  |  |
| ✅ |  |  |  | `0x1200` | 4608 | object |  | uint16 | Reading and writing |  |
| ✅ |  |  |  | `0x1201` | 4609 | Calibration method |  | uint16 | Reading and writing | 0: Single-point calibration; 1: Two-point calibration; 2: Factory reset. |
| ✅ |  |  |  | `0x1202` | 4610 | External measurement value 1 |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x1203` | 4611 | Internal measurement value 1 |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x1204` | 4612 | External measurement value 2 |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x1205` | 4613 | Internal measurement value 2 |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x1206` | 4614 | reserve |  |  |  |  |
| ✅ |  |  |  | `0x1207` | 4615 | reserve |  |  |  |  |
| ✅ |  |  |  | `0x1208` | 4616 | Time calibration enabled |  | int16_t | Reading and writing | 0: Waiting/Completed 1: Calibration 2: Reset |
| ✅ |  |  |  | `0x1209` | 4617 | Annual calibration |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x120A` | 4618 | Monthly calibration |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x120B` | 4619 | Weekly calibration |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x120C` | 4620 | Daily Calibration |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x120D` | 4621 | Time calibration |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x120E` | 4622 | Partial calibration |  | int16_t | Reading and writing |  |
| ✅ |  |  |  | `0x120F` | 4623 | Second calibration |  | int16_t | Reading and writing |  |
|  |  |  |  | `0x1210` | 4624 |  |  |  |  |  |
|  |  |  |  | `0x1211` | 4625 |  |  |  |  |  |
|  |  |  |  | `0x1212` | 4626 |  |  |  |  |  |
|  |  |  |  | `0x1213` | 4627 |  |  |  |  |  |
|  |  |  |  | `0x1214` | 4628 |  |  |  |  |  |
|  |  |  |  | `0x1215` | 4629 |  |  |  |  |  |
|  |  |  |  | `0x1216` | 4630 |  |  |  |  |  |
|  |  |  |  | `0x1217` | 4631 |  |  |  |  |  |
|  |  |  |  | `0x1218` | 4632 |  |  |  |  |  |
|  |  |  |  | `0x1219` | 4633 |  |  |  |  |  |
|  |  |  |  | `0x121A` | 4634 |  |  |  |  |  |
|  |  |  |  | `0x121B` | 4635 |  |  |  |  |  |
|  |  |  |  | `0x121C` | 4636 |  |  |  |  |  |
|  |  |  |  | `0x121D` | 4637 |  |  |  |  |  |
|  |  |  |  | `0x121E` | 4638 |  |  |  |  |  |
|  |  |  |  | `0x121F` | 4639 |  |  |  |  |  |

---

### WF_OTA

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
|  |  |  |  | `0x4000` | 16384 | Upgrade commands and data |  |  |  |  |
|  |  |  |  | `0x4000` | 16384 | Upgrade command code | uint16_t |  |  | Command Type / Bit0-Bit7 Software Type / Bit8-Bit15 Command Type: ID Value Description 0x00 Activation command, used to instruc... |
|  |  |  |  | `0x4001` | 16385 | Upgrade data | uint16_t |  |  | Package ID |
|  |  |  |  | `0x4002` | 16386 | Upgrade data | uint16_t |  |  | Upgrade data must be 32-bit aligned! Otherwise, writing to Flash will result in an error. |
|  |  |  |  | `0x4003` | 16387 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4004` | 16388 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4005` | 16389 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4006` | 16390 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4007` | 16391 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4008` | 16392 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4009` | 16393 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x400A` | 16394 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x400B` | 16395 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x400C` | 16396 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x400D` | 16397 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x400E` | 16398 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x400F` | 16399 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4010` | 16400 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4011` | 16401 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4012` | 16402 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4013` | 16403 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4014` | 16404 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4015` | 16405 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4016` | 16406 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4017` | 16407 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4018` | 16408 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4019` | 16409 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x401A` | 16410 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x401B` | 16411 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x401C` | 16412 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x401D` | 16413 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x401E` | 16414 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x401F` | 16415 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4020` | 16416 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4021` | 16417 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4022` | 16418 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4023` | 16419 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4024` | 16420 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4025` | 16421 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4026` | 16422 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4027` | 16423 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4028` | 16424 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4029` | 16425 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x402A` | 16426 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x402B` | 16427 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x402C` | 16428 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x402D` | 16429 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x402E` | 16430 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x402F` | 16431 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4030` | 16432 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4031` | 16433 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4032` | 16434 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4033` | 16435 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4034` | 16436 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4035` | 16437 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4036` | 16438 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4037` | 16439 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4038` | 16440 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4039` | 16441 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x403A` | 16442 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x403B` | 16443 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x403C` | 16444 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x403D` | 16445 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x403E` | 16446 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x403F` | 16447 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4040` | 16448 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4041` | 16449 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4042` | 16450 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4043` | 16451 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4044` | 16452 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4045` | 16453 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4046` | 16454 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4047` | 16455 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4048` | 16456 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4049` | 16457 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x404A` | 16458 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x404B` | 16459 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x404C` | 16460 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x404D` | 16461 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x404E` | 16462 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x404F` | 16463 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4050` | 16464 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4051` | 16465 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4052` | 16466 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4053` | 16467 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4054` | 16468 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4055` | 16469 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4056` | 16470 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4057` | 16471 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4058` | 16472 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4059` | 16473 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x405A` | 16474 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x405B` | 16475 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x405C` | 16476 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x405D` | 16477 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x405E` | 16478 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x405F` | 16479 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4060` | 16480 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4061` | 16481 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4062` | 16482 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4063` | 16483 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4064` | 16484 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4065` | 16485 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4066` | 16486 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4067` | 16487 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4068` | 16488 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4069` | 16489 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x406A` | 16490 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x406B` | 16491 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x406C` | 16492 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x406D` | 16493 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x406E` | 16494 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x406F` | 16495 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4070` | 16496 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4071` | 16497 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4072` | 16498 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4073` | 16499 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4074` | 16500 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4075` | 16501 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4076` | 16502 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4077` | 16503 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4078` | 16504 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4079` | 16505 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x407A` | 16506 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x407B` | 16507 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x407C` | 16508 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x407D` | 16509 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x407E` | 16510 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x407F` | 16511 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4080` | 16512 | Upgrade data | uint16_t |  |  |  |
|  |  |  |  | `0x4081` | 16513 |  |  |  |  |  |
|  |  |  |  | `0x4082` | 16514 |  |  |  |  |  |
|  |  |  |  | `0x4083` | 16515 |  |  |  |  |  |
|  |  |  |  | `0x4084` | 16516 |  |  |  |  |  |
|  |  |  |  | `0x4085` | 16517 |  |  |  |  |  |
|  |  |  |  | `0x4086` | 16518 |  |  |  |  |  |
|  |  |  |  | `0x4087` | 16519 |  |  |  |  |  |
|  |  |  |  | `0x4088` | 16520 |  |  |  |  |  |
|  |  |  |  | `0x4089` | 16521 |  |  |  |  |  |
|  |  |  |  | `0x408A` | 16522 |  |  |  |  |  |
|  |  |  |  | `0x408B` | 16523 |  |  |  |  |  |
|  |  |  |  | `0x408C` | 16524 |  |  |  |  |  |
|  |  |  |  | `0x408D` | 16525 |  |  |  |  |  |
|  |  |  |  | `0x408E` | 16526 |  |  |  |  |  |
|  |  |  |  | `0x408F` | 16527 |  |  |  |  |  |
|  |  |  |  | `0x4090` | 16528 | Upgrade status | uint16_t |  |  | Bit0-Bit3 EMS Upgrade Status; Bit4-Bit7 PCS Upgrade Status; Bit8-Bit11 BMS Upgrade Status (Reserved); Bit12-Bit15 MCU Upgrade S... |
|  |  |  |  | `0x4091` | 16529 |  |  |  |  |  |
|  |  |  |  | `0x4092` | 16530 | Running status | uint16_t |  |  | Bit0-Bit3 EMS running status; Bit4-Bit7 PCS running status; Bit8-Bit11 BMS running status (reserved); Bit12-Bit15 MCU running s... |
|  |  |  |  | `0x4093` | 16531 |  |  |  |  |  |
|  |  |  |  | `0x4094` | 16532 | Host computer settings for burning status | uint16_t |  |  | 0x00: Idle; 0x01: Burning in progress; 0x02: Burning completed. |
|  |  |  |  | `0x4095` | 16533 | Equipment type in this package | uint16_t |  |  | BIT0:PCS BIT1:EMS BIT2:BMS BIT3:COM |
|  |  |  |  | `0x4096` | 16534 | Programmable type | uint16_t |  |  | BIT0:PCS BIT1:EMS BIT2:BMS BIT3:COM |
|  |  |  |  | `0x4097` | 16535 | model | uint16_t |  |  | 0x00:NULL 0x01:3K 0x02:5K 0x03:6K 0x04:11K |
|  |  |  |  | `0x4098` | 16536 | Software type | uint16_t |  |  | 0x00: ERROR 0x01: APP 0x02: BOOT |
|  |  |  |  | `0x4099` | 16537 | Erasure time | uint16_t |  |  | unit ms |
|  |  |  |  | `0x409A` | 16538 | Reserved | uint16_t |  |  |  |
|  |  |  |  | `0x409B` | 16539 | Version number _H | uint16_t |  |  |  |
|  |  |  |  | `0x409C` | 16540 | Version number _L | uint16_t |  |  |  |
|  |  |  |  | `0x409D` | 16541 | Footprint_A | uint16_t |  |  |  |
|  |  |  |  | `0x409E` | 16542 | Footprint_B | uint16_t |  |  |  |
|  |  |  |  | `0x409F` | 16543 | Footprint_C | uint16_t |  |  |  |
|  |  |  |  | `0x40A0` | 16544 | Footprint_D | uint16_t |  |  |  |
|  |  |  |  | `0x40A1` | 16545 | Burn package length_H |  |  |  |  |
|  |  |  |  | `0x40A2` | 16546 | Burn package length_L |  |  |  |  |
|  |  |  |  | `0x40A3` | 16547 |  |  |  |  |  |
|  |  |  |  | `0x40A4` | 16548 |  |  |  |  |  |
|  |  |  |  | `0x40A5` | 16549 |  |  |  |  |  |
|  |  |  |  | `0x40A6` | 16550 |  |  |  |  |  |
|  |  |  |  | `0x40A7` | 16551 |  |  |  |  |  |
|  |  |  |  | `0x40A8` | 16552 |  |  |  |  |  |
|  |  |  |  | `0x40A9` | 16553 |  |  |  |  |  |
|  |  |  |  | `0x40AA` | 16554 |  |  |  |  |  |
|  |  |  |  | `0x40AB` | 16555 |  |  |  |  |  |
|  |  |  |  | `0x40AC` | 16556 |  |  |  |  |  |
|  |  |  |  | `0x40AD` | 16557 |  |  |  |  |  |
|  |  |  |  | `0x40AE` | 16558 |  |  |  |  |  |
|  |  |  |  | `0x40AF` | 16559 |  |  |  |  |  |
|  |  |  |  | `0x40B0` | 16560 |  |  |  |  |  |
|  |  |  |  | `0x40B1` | 16561 |  |  |  |  |  |
|  |  |  |  | `0x40B2` | 16562 |  |  |  |  |  |
|  |  |  |  | `0x40B3` | 16563 |  |  |  |  |  |
|  |  |  |  | `0x40B4` | 16564 |  |  |  |  |  |
|  |  |  |  | `0x40B5` | 16565 |  |  |  |  |  |
|  |  |  |  | `0x40B6` | 16566 |  |  |  |  |  |
|  |  |  |  | `0x40B7` | 16567 |  |  |  |  |  |
|  |  |  |  | `0x40B8` | 16568 |  |  |  |  |  |
|  |  |  |  | `0x40B9` | 16569 |  |  |  |  |  |
|  |  |  |  | `0x40BA` | 16570 |  |  |  |  |  |
|  |  |  |  | `0x40BB` | 16571 |  |  |  |  |  |
|  |  |  |  | `0x40BC` | 16572 |  |  |  |  |  |
|  |  |  |  | `0x40BD` | 16573 |  |  |  |  |  |
|  |  |  |  | `0x40BE` | 16574 |  |  |  |  |  |
|  |  |  |  | `0x40BF` | 16575 |  |  |  |  |  |
|  |  |  |  | `0x40C0` | 16576 |  |  |  |  |  |
|  |  |  |  | `0x40C1` | 16577 |  |  |  |  |  |
|  |  |  |  | `0x40C2` | 16578 |  |  |  |  |  |
|  |  |  |  | `0x40C3` | 16579 |  |  |  |  |  |
|  |  |  |  | `0x40C4` | 16580 |  |  |  |  |  |
|  |  |  |  | `0x40C5` | 16581 |  |  |  |  |  |
|  |  |  |  | `0x40C6` | 16582 |  |  |  |  |  |
|  |  |  |  | `0x40C7` | 16583 |  |  |  |  |  |
|  |  |  |  | `0x40C8` | 16584 |  |  |  |  |  |
|  |  |  |  | `0x40C9` | 16585 |  |  |  |  |  |
|  |  |  |  | `0x40CA` | 16586 |  |  |  |  |  |
|  |  |  |  | `0x40CB` | 16587 |  |  |  |  |  |
|  |  |  |  | `0x40CC` | 16588 |  |  |  |  |  |
|  |  |  |  | `0x40CD` | 16589 |  |  |  |  |  |
|  |  |  |  | `0x40CE` | 16590 |  |  |  |  |  |
|  |  |  |  | `0x40CF` | 16591 |  |  |  |  |  |
|  |  |  |  | `0x40D0` | 16592 |  |  |  |  |  |
|  |  |  |  | `0x40D1` | 16593 |  |  |  |  |  |
|  |  |  |  | `0x40D2` | 16594 |  |  |  |  |  |
|  |  |  |  | `0x40D3` | 16595 |  |  |  |  |  |
|  |  |  |  | `0x40D4` | 16596 |  |  |  |  |  |
|  |  |  |  | `0x40D5` | 16597 |  |  |  |  |  |
|  |  |  |  | `0x40D6` | 16598 |  |  |  |  |  |
|  |  |  |  | `0x40D7` | 16599 |  |  |  |  |  |
|  |  |  |  | `0x40D8` | 16600 |  |  |  |  |  |
|  |  |  |  | `0x40D9` | 16601 |  |  |  |  |  |

---

### WF_UserSet

| Initial Logger query | Regular Logger query | My Logger query | ESPHome id | Hex | Dec | Name | Type | Unit | Permission | Notes |
|---|---|---|---|-----|-----|------|------|------|------------|-------|
| ✅ |  | ✅ | set_output_voltage | `0x4100` | 16640 | User Settings |  |  |  | Note: This setting field can only be set with one parameter at a time. The host computer must ensure the accuracy of the data r... |
| ✅ |  | ✅ | set_output_voltage | `0x4100` | 16640 | Output voltage | uint16_t | / | Reading and writing | 0:208V 1:220V 2:230V 3:240V |
| ✅ |  | ✅ | set_output_freq | `0x4101` | 16641 | Output frequency | uint16_t | / | Reading and writing | 0:50Hz 1:60Hz |
| ✅ |  | ✅ | set_output_priority | `0x4102` | 16642 | Output priority | uint16_t | / | Reading and writing | 0:GPB 1:PGB 2:PBG 3:MKS |
| ✅ |  | ✅ | set_operating_mode | `0x4103` | 16643 | Operating mode | uint16_t | / | Reading and writing | 0:APP 1:UPS |
| ✅ |  | ✅ | set_charging_priority | `0x4104` | 16644 | Charging priority | uint16_t | / | Reading and writing | 0:PNG 1:OPV 2:PVF |
| ✅ |  | ✅ | set_ac_char_curr | `0x4105` | 16645 | AC charging current | uint16_t | 1A | Reading and writing | 2-120A continuously adjustable [VMH6KU only supports 0x02:2A, 0x0A:10A, 0x14:20A, 0x1E:30A, 0x28:40A, 0x32:50A, 0x3C:60A, 0x46:... |
| ✅ |  | ✅ | set_max_char_curr | `0x4106` | 16646 | Maximum charging current | uint16_t | / | Reading and writing | 0:2A 1:10A 2:20A 3:30A 4:40A 5:50A 6:60A 7:70A 8:80A 9:90A 10:100A 11:110A 12:120A |
| ✅ |  | ✅ | set_bat_type | `0x4107` | 16647 | Battery Type | uint16_t | / | Reading and writing | 0: Lead-acid battery; 1: Water-filled battery; 2: Ternary lithium battery; 3: Lithium iron phosphate battery; 4: User-defined b... |
| ✅ |  | ✅ | set_bat_low_volt | `0x4108` | 16648 | Battery low voltage point | uint16_t | 0.1V | Reading and writing | Lead-acid/Water-filled: 44V; Non-adjustable Ternary Lithium/Lithium Iron: 41.2V-50V; Customizable: 42V - 54V |
| ✅ |  | ✅ | set_bat_shutdown_volt | `0x4109` | 16649 | Battery low voltage point (battery shutdown point) | uint16_t | 0.1V | Reading and writing | Lead-acid/Water-filled: 42V Non-adjustable ternary lithium/lithium iron phosphate/Custom: 40V-48V |
| ✅ |  | ✅ | set_bat_bulk_volt | `0x410A` | 16650 | constant pressure point | uint16_t | 0.1V | Reading and writing | Non-adjustable Lead-acid: 56.4V; Non-adjustable water-filled: 58V; ternary lithium 48V-60V/lithium iron phosphate/custom: 50V-58V |
| ✅ |  | ✅ | set_bat_float_volt | `0x410B` | 16651 | float point | uint16_t | 0.1V | Reading and writing | Lead-acid/Water-filled: 54V; Non-adjustable Ternary Lithium/Lithium Iron: 50V-58V; Customizable: 48V-60V |
| ✅ |  |  |  | `0x410C` | 16652 | Battery to AC voltage point | uint16_t | 0.1V | Reading and writing | Lead-acid/Water-filled: 44V - 52V; Ternary lithium/Lithium iron phosphate/Custom: 40V-50V |
| ✅ |  |  |  | `0x410D` | 16653 | Return to battery mode voltage point | uint16_t | 0.1V | Reading and writing | Lead-acid/Water-filled: 48V - 58V; Ternary lithium/Lithium iron phosphate/Custom: 46V-58V |
| ✅ |  | ✅ | set_grid_low_voltage | `0x410E` | 16654 | Low voltage point of mains power | uint16_t | 1V | Reading and writing | APP: 90V-154V UPS: 170V-200V |
| ✅ |  | ✅ | set_grid_high_voltage | `0x410F` | 16655 | High voltage point of mains power | uint16_t | 1V | Reading and writing | APP: 264V-280V UPS: 264V |
| ✅ |  |  |  | `0x4110` | 16656 | Parallel mode | uint16_t | / | Reading and writing | 0: Single-phase mode; 1: Single-phase parallel mode; 2: Three-phase parallel mode (phase A); 3: Three-phase parallel mode (phas... |
| ✅ |  |  |  | `0x4111` | 16657 | Parallel serial number | uint16_t | / | Reading and writing | 0-14 |
| ✅ |  |  |  | `0x4112` | 16658 | Enable equalization mode for charging | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  |  |  | `0x4113` | 16659 | Equalization voltage point | uint16_t | 0.1V | Reading and writing | 48V-60V |
| ✅ |  |  |  | `0x4114` | 16660 | Equalization charging time | uint16_t | 1min | Reading and writing | 5-900 step size 5 |
| ✅ |  |  |  | `0x4115` | 16661 | Equalization delay time | uint16_t | 1min | Reading and writing | 5-900 step size 5 |
| ✅ |  |  |  | `0x4116` | 16662 | Equalization interval time | uint16_t | day | Reading and writing | 1-90 |
| ✅ |  |  |  | `0x4117` | 16663 | Enable Balance Now | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | set_dual_output_cutoff_voltage | `0x4118` | 16664 | Dual-channel output cutoff voltage | uint16_t | 0.1V | Reading and writing | 440-600: 44V-60V |
| ✅ |  | ✅ | set_dual_output_mode | `0x4119` | 16665 | Dual-channel output time | uint16_t | 1min | Reading and writing | 5-900: 5min-900min 0xFFF1: Dual output disabled 0xFFF2: Dual output unlimited time |
| ✅ |  |  |  | `0x411A` | 16666 | Generator enable | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  |  |  | `0x411B` | 16667 | Generator rated power | uint16_t | 0.1KW | Reading and writing | 0-65:0-6.5KW |
| ✅ |  |  |  | `0x411C` | 16668 | Generator maximum power | uint16_t | 0.1KW | Reading and writing | 0-65:0-6.5KW |
| ✅ |  |  |  | `0x411D` | 16669 | Generator alarm clearing | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | set_bms_protocol | `0x411E` | 16670 | BMS Protocol Selection | uint16_t | / | Reading and writing | 0: Disable BMS function; 1: CVTE protocol; 2: Growatt protocol; 3: Sun & Moon protocol; 4: Power protocol; 5: Tower protocol; 6... |
| ✅ |  | ✅ | set_bms_id | `0x411F` | 16671 | BMS ID Selection | uint16_t | / | Reading and writing | 0-15 0xFFF1: ID self-search |
| ✅ |  | ✅ | set_bms_shutdown_soc | `0x4120` | 16672 | Low SOC shutdown SOC settings | uint16_t | 0.01 | Reading and writing | 5-50 0xFFF1: Low SOC shutdown function for disabled users |
| ✅ |  | ✅ | set_bms_power_off_soc | `0x4121` | 16673 | Battery SOC settings | uint16_t | 0.01 | Reading and writing | 10-90 0xFFF1: Power-off SOC to Battery Function |
| ✅ |  | ✅ | set_bms_switch_to_ac_soc | `0x4122` | 16674 | SOC settings for switching to AC power | uint16_t | 0.01 | Reading and writing | 10-100 0xFFF1: Disabled SOC to AC power function |
| ✅ |  | ✅ | set_remote_power_control | `0x4123` | 16675 | Remote power on/off enable | uint16_t | / | Reading and writing | 0: Disable remote control; 1: Enable remote control and power on; 2: Enable remote control and power off. |
| ✅ |  | ✅ | sel_turn_off_charging | `0x4124` | 16676 | Turn off charging | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_backlight_self_ext | `0x4125` | 16677 | Self-extinguishing backlight | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  |  |  | `0x4126` | 16678 | Reserved | / | / | Reading and writing | / |
| ✅ |  | ✅ | sel_overheating_restart | `0x4127` | 16679 | Overheating restart | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_overload_restart | `0x4128` | 16680 | Overload restart | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_overload_bypass | `0x4129` | 16681 | Overload bypass | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_low_power_saving | `0x412A` | 16682 | Low power consumption and energy saving | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_auto_mains_freq_detect | `0x412B` | 16683 | Automatic detection of mains frequency | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_soft_starter_active | `0x412C` | 16684 | After the output relay is closed, the inverter soft starter is activated. | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_bat_open_circuit_warning | `0x412D` | 16685 | Battery open circuit warning | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | set_feeder_function | `0x412E` | 16686 | Feeder Function Enable | uint16_t | / | Reading and writing | 0: OFF 1: INT internal sampling grid connection 2: CT external current transformer sampling grid connection 3: MET external met... |
| ✅ |  | ✅ | set_feeder_power_limit | `0x412F` | 16687 | Feeder power | uint16_t | 0.1KW | Reading and writing | 0-65:0-6.5KW |
| ✅ |  | ✅ | sel_buzzer_muted | `0x4130` | 16688 | Buzzer muted | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_fault_return_main | `0x4131` | 16689 | Default return to main interface settings | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_warning_main_input_change | `0x4132` | 16690 | Warning of main input change | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | sel_restore_default_settings | `0x4133` | 16691 | Restore default settings | uint16_t | / | Reading and writing | 0:OFF 1:ON |
| ✅ |  | ✅ | inv_read_sec | `0x4134` | 16692 | Seconds setting | uint16_t | 1 sec | Reading and writing | 0-59 |
| ✅ |  | ✅ | inv_read_min | `0x4135` | 16693 | point | uint16_t | 1min | Reading and writing | 0-59 |
| ✅ |  | ✅ | inv_read_hour | `0x4136` | 16694 | hour | uint16_t | 1 hour | Reading and writing | 0-23 |
| ✅ |  | ✅ | inv_read_day | `0x4137` | 16695 | day | uint16_t | / | Reading and writing | 0-31 |
| ✅ |  | ✅ | inv_read_month | `0x4138` | 16696 | moon | uint16_t | / | Reading and writing | 0-12 |
| ✅ |  | ✅ | inv_read_year | `0x4139` | 16697 | Year | uint16_t | / | Reading and writing | 0-99 |
| ✅ |  |  |  | `0x413A` | 16698 | Power Supply 1 | uint16_t | H | Reading and writing | 0-23 |
| ✅ |  |  |  | `0x413B` | 16699 | Selling electricity 1 | uint16_t | H | Reading and writing | 0-23 |
| ✅ |  |  |  | `0x413C` | 16700 | Power Supply 2 | uint16_t | H | Reading and writing | 0-23 |
| ✅ |  |  |  | `0x413D` | 16701 | Selling Electricity 2 | uint16_t | H | Reading and writing | 0-23 |
| ✅ |  |  |  | `0x413E` | 16702 | Power on | uint16_t | H | Reading and writing | 0-23 |
| ✅ |  |  |  | `0x413F` | 16703 | Power off | uint16_t | H | Reading and writing | 0-23 |
| ✅ |  |  |  | `0x4140` | 16704 | Model Configuration | uint16_t |  | Reading and writing | 0: Automatic recognition (effective after next power-on) 1: Low-end model 2: Mid-range model 3: High-end model |
| ✅ |  |  |  | `0x4141` | 16705 | Screen type | uint16_t |  | Reading and writing | 0: TRB8131 1: B00346 2: CNKD0601/CNKD0602 |
| ✅ |  | ✅ | set_max_discharge_current | `0x4142` | 16706 | Maximum discharge current | uint16_t | A | Reading and writing | 0-30:10-160A (step size 5A) 0xFFF1: OFF [Effective for VMH5KU/VMH6KU and VML1K2; VMH5KU supports up to 160A, VMH6KU supports up... |
| ✅ |  | ✅ | inverter_wifi_status | `0x4143` | 16707 | Wi-Fi connection status | uint16_t |  | Reading and writing | The following settings are used for the Wi-Fi module: 1: Wi-Fi not connected to a hotspot; 2: Wi-Fi connecting to a hotspot; 3:... |
| ✅ |  |  |  | `0x4144` | 16708 | Automatic switching of feeder power time 1 | uint16_t | H | Reading and writing | 0-23 |
| ✅ |  |  |  | `0x4145` | 16709 | Automatic switching of feeder power time 2 | uint16_t | H | Reading and writing | 0-23 |
| ✅ |  |  |  | `0x4146` | 16710 | Automatic switching of feeder power1 | uint16_t | 0.1KW | Reading and writing | 0-65:0-6.5KW |
| ✅ |  |  |  | `0x4147` | 16711 | Automatic switching of feeder power 2 | uint16_t | 0.1KW | Reading and writing | 0-65:0-6.5KW |
| ✅ |  |  |  | `0x4148` | 16712 | Set the fan speed to 100 before shutting down. | uint16_t |  | Reading and writing | 0: Normal operation 1: Set the fan speed to 100 before shutdown to address the issue of low-power fans not being able to shut d... |
| ✅ |  |  |  | `0x4149` | 16713 | Set the reference value for inverter current when the output power is less than 50W. | uint16_t | 0.01A | Reading and writing | The default value is 26, and the setting range is 0-200. [Effective on VMH5KU/VMH6KU] |
| ✅ |  |  |  | `0x414A` | 16714 | Set button reverse | uint16_t |  | Reading and writing | 0: Down arrow key increments the page number; 1: Down arrow key decrements the page number. [Available in VMH5KU/VMH6KU] |
| ✅ |  |  |  | `0x414B` | 16715 | Set dual-output cutoff SOC | uint16_t |  | Reading and writing | 5-90: Dual output cutoff SOC 0xFFF1: Disable this function [Affected on VMH5KU/VMH6KU] |
|  |  | ✅ | ??? | `0x414C` | 16715 | Do not let the power go out | uint16_t |  | Reading and writing | 0: Invalid; 1: Disabled. Even if the machine is in a power-off state after setting a timeout, it will not enter shutdown mode. ... |

---

*Total registers: **1046** | Implemented sensors in YAML: **207***