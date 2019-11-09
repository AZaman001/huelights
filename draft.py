from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.0.100'}, user={'name':'pxkuGTBuWvmmCt1fZBQCoo7nrArEoSP-NV4aG4am'})

# Get light number 2.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.0.100'}, user={'name':'pxkuGTBuWvmmCt1fZBQCoo7nrArEoSP-NV4aG4am'})
resource = {'which':2}
bridge.light.get(resource)

# Update light #2's state.
from beautifulhue.api import Bridge

bridge = Bridge(device={'ip':'192.168.0.100'}, user={'name':'pxkuGTBuWvmmCt1fZBQCoo7nrArEoSP-NV4aG4am'})
resource = {
    'which':2,
    'data':{
        'state':{'on':false}
    }
}
bridge.light.update(resource)