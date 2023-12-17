from ncclient import manager
#from virl_router_info import router

config_template = open('/Users/mark/DevNet/gitcbt/ios_config.xml').read()

router = {'host':'10.32.1.210', 'port':'830', 'username':'cisco', 'password': 'cisco'}

netconf_config = config_template.format(
    interface_name="GigabitEthernet1", interface_desc="Mark was here")

with manager.connect(host=router['host'], port=router['port'], username=router['username'], password=router['password'], hostkey_verify=False) as m:
    device_reply = m.edit_config(netconf_config, target="running")
    print(device_reply)