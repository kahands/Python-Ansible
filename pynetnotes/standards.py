#standards

#NTP#
ntpconfig = {
	'ntp server 130.126.24.25',
	'ntp server 152.2.21.2',
}
config_commands = ntpconfig
output = pynet_rtr1.send_config_set(config_commands)

output = pynet_rtr1.send_command("show run | inc ntp")
print output

nontpconfig = {
	'no ntp server 130.126.24.25',
	'no ntp server 152.2.21.2',
}

config_commands = nontpconfig
output = pynet_rtr1.send_config_set(config_commands)

#snmp#

output = pynet_rtr1.send_command("show run | inc snmp")
print output

snmpconfig = {
	'snmp-server group READONLY v3 priv read VIEWSTD access 98',
	'snmp-server view VIEWSTD iso included',
	'snmp-server community galileo RO 98',
	'snmp-server ifindex persist',
	'snmp-server location Freemont, CA',
	'snmp-server contact Kirk Byers',
}

config_commands = snmpconfig
output = pynet_rtr1.send_config_set(config_commands)

#DNS#

output = pynet_rtr1.send_command("show run | inc dns")
print output

dnsconfig = {
	'nameserver ',
	'nameserver ',
}

config_commands = dnsconfig
output = pynet_rtr1.send_config_set(config_commands)

#aaa#

output = pynet_rtr1.send_command("show run | inc aaa")
print output

aaaconfig = {
	'aaa new-model',
	'aaa authentication password-prompt Fallback_Passwd',
	'aaa authentication login default group tacacs+ local',
}

config_commands = aaaconfig
output = pynet_rtr1.send_config_set(config_commands)

#tacacs#

output = pynet_rtr1.send_command("show run | inc tacacs")
print output

tacacsconfig = {
	'tacacs-server host 10.1.2.3',
	'tacacs-server key goaway',
}

config_commands = tacacsconfig
output = pynet_rtr1.send_config_set(config_commands)

#logging#

output = pynet_rtr1.send_command("show run | inc logging")
print output

loggingconfig = {
	'no logging console ',
	'logging buffered informational',
	'terminal no monitor',
}

config_commands = loggingconfig
output = pynet_rtr1.send_config_set(config_commands)