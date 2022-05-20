from firebaseAdmin import pushData
from pycomm3 import LogixDriver

plc = LogixDriver('172.18.8.90')
plc.open()

tag = plc.read('tag')
pushData('/plcData', { 'tagName': tag.name, 'value': tag.value })
