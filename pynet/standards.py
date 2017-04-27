#standards

#NTP#
ntpconfig = {
	'ntp server 130.126.24.25',
	'ntp server 152.2.21.2',
}

nontpconfig = {
	'no ntp server 130.126.24.25',
	'no ntp server 152.2.21.2',
}


#snmp#

snmpconfig = {
	'snmp-server group READONLY v3 priv read VIEWSTD access 98',
	'snmp-server view VIEWSTD iso included',
	'snmp-server community galileo RO 98',
	'snmp-server ifindex persist',
	'snmp-server location Freemont, CA',
	'snmp-server contact Kirk Byers',
}


#DNS#

dnsconfig = {
	'nameserver ',
	'nameserver ',
}


#aaa#

aaaconfig = {
	'aaa new-model',
	'aaa authentication password-prompt Fallback_Passwd',
	'aaa authentication login default group tacacs+ local',
}

#tacacs#

tacacsconfig = {
	'tacacs-server host 10.1.2.3',
	'tacacs-server key goaway',
}

#logging#

loggingconfig = {
	'no logging console ',
	'logging buffered informational',
	'terminal no monitor',
}
