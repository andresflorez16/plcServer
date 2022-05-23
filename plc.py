from firebaseAdmin import pushData
from pycomm3 import LogixDriver

# plc = LogixDriver('172.18.8.90')
# plc.open()

# tag = plc.read('tag').tag
# value = plc.read('tag').value



pushData('/estacionCalidad', { 'tagName': 'variable1', 'value': 2 })
