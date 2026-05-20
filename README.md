# My ESPHome PowMr Hybrid Inverter
ESPHome configuration for JSD Solar Inverter – Modbus RTU logger
Register source: docs\INV-Modbus地址表3KU（外发）V1.20.xlsx or docs\registers-map.md


## Compatibility



### Tested models

## Connection
use 


## Usage
1) Create new ESPHome device, within your ESPHome (let it be `my-inverter`, for example) 
2) Copy the contents of the `jsd-solar-inverter.yaml`  to a config file of newly created deivce.
3) Please be sure that all secret variables defined in `jsd-solar-inverter.yaml` are present in your `secrets.yaml`. if something is missed, it should be added. Please use `secrets.yaml.template` as an example of `secrets.yaml`
4) chose proper TX, RX pins for your UART, Review and comment sensors that are not needed.
5) Flash firmware to your ESP32-S3


## Inverter card
For easy integration into Home Assistant, you can use the examples of inverter cards. 
The following custom plugins are required: [sunsynk-power-flow-card](https://github.com/slipx06/sunsynk-power-flow-card), [stack-in-card](https://github.com/custom-cards/stack-in-card).

## Optimize modbus communications
ESPHome reads sequential Modbus registers in one batch. If you have gaps in register addresses, you need to use the `register_count` parameter to skip N registers and continue the batch.
[Details in ESPHome docs](https://esphome.io/components/sensor/modbus_controller#modbus-register-count).

You can debug your register ranges by setting the global log level to `VERBOSE` and muting all "noisy" components except the `modbus_controller`.
```yaml
logger:
  level: VERBOSE
  logs:
    component: ERROR # Fix for issue #4717 "Component xxxxxx took a long time for an operation"
    modbus_controller: VERBOSE
    modbus_controller.text_sensor: WARN
    modbus_controller.sensor: WARN
    modbus_controller.binary_sensor: WARN
    modbus_controller.select: WARN
```
After this, the ranges map will be printed in the logs:
```text
[15:55:14][C][modbus_controller:307]: ranges
[18:41:21][C][modbus_controller:307]: ranges
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x1196 count=37 skip_updates=0
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x11BC count=16 skip_updates=0
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x138A count=1 skip_updates=2
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x138F count=1 skip_updates=2
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x1391 count=1 skip_updates=2
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x1399 count=1 skip_updates=2
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x139A count=1 skip_updates=2
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x139E count=1 skip_updates=2
[18:41:21][C][modbus_controller:310]:   Range type=3 start=0x13A0 count=1 skip_updates=2
```
> *In the example above, the sensor registers batches starts from `0x1196` & `0x11BC` (one large batch causes data errors). Select registers starts from `0x138A`.*
> *Using batches for selects triggers `Modbus device set offline` warning messages, so you need to read them separately.*

You will see gaps in register ranges map. To calculate `register_count`, you need to convert HEX addresses to decimal and subtract them.

## UART debugging
- Uncomment debug section in [modules/inverter.yaml](/src/modules/inverter.yaml) or [modules/pzem.yaml](/src/modules/pzem.yaml) to enable the debug output of the UART component 
  ```
    # debug:
    #   direction: BOTH
    #   dummy_receiver: false
  ```
- Increase the log level to `DEBUG` or `VERBOSE`
  ```
  logger:
    level: WARN
  ```

## Notes
- Registers map: [registers-map.md](docs\INV-Modbus地址表3KU（外发）V1.20.xlsx)