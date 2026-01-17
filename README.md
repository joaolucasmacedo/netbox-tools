# netbox-tools
A few Tools to improve NetBox usage

See below a selection on NetBox plugins and tools with version compatibility

|Plugin                   |4.2.9 |4.3.7 |4.4.2  |4.5.0  |Status       |Pip Package                   |configuration.py         |URL                                                             |
|-------------------------|------|------|-------|-----  |-------------|------------------------------|-------------------------|----------------------------------------------------------------|
|Topology Views           |4.2.0 |4.3.0 |4.4.0  |-----  |Active       |netbox-topology-views         |netbox_topology_views    |[Topology Views](https://github.com/netbox-community/netbox-topology-views)|
|NeXtbox UI Plugin        |1.0.7 |---   |------ |-----  |Active       |nextbox-ui-plugin             |nextbox_ui_plugin        |[NeXtbox UI](https://github.com/iDebugAll/nextbox-ui-plugin)|
|NetBox Ninja Plugin      |0.1.12|0.1.12|???    |-----  |Active       |netbox-ninja-plugin           |netbox_ninja_plugin      |[Ninja plugin](https://github.com/rautanen-io/netbox-ninja-plugin)|
|Qrcode                   |0.0.17|0.0.18|0.0.19 |-----  |Active       |netbox-qrcode                 |netbox_qrcode            |[QR code](https://github.com/netbox-community/netbox-qrcode)|
|Netbox Plugin DNS        |1.2.14|1.3.2 |1.4.2  |-----  |Active       |netbox-plugin-dns             |netbox_dns               |[Plugin DNS](https://github.com/peteeckel/netbox-plugin-dns)|
|BGP                      |0.15.0|0.16.0|0.17.0 |-----  |Active       |netbox-bgp                    |netbox_bgp               |[Plugin BGP](https://github.com/netbox-community/netbox-bgp)|
|RPKI                     |0.1.5 |---   |------ |-----  |???          |netbox-rpki                   |netbox_rpki              |[Plugin RPKI](https://github.com/menckend/netbox_rpki)|
|Security(NAT)            |1.0.2 |1.2.14|1.3.0  |-----  |Active       |netbox-security               |netbox_security          |[NetBox Security](https://github.com/andy-shady-org/netbox-security)|
|Floorplan                |0.6.0 |0.7.0 |0.8.0  |-----  |Active       |netbox-floorplan-plugin       |netbox_floorplan         |[Floorplan](https://github.com/netbox-community/netbox-floorplan-plugin)|
|Reorder Rack             |1.1.3 |1.1.4 |------ |-----  |Active       |netbox-reorder-rack           |netbox_reorder_rack      |[Reorder Rack](https://github.com/netbox-community/netbox-reorder-rack))|
|Netbox Secrets           |2.2.1 |2.3.4 |2.4.1  |-----  |Active       |netbox-secrets                |netbox_secrets           |[NetBox Secrets](https://github.com/Onemind-Services-LLC/netbox-secrets)|
|ACLs                     |1.8.1 |1.9.1 |1.9.1  |-----  |Active       |netbox-acls                   |netbox_acls              |[ACLs](https://github.com/ryanmerolle/netbox-acls)|
|NAPALM                   |0.3.1 |0.3.2 |0.3.3  |-----  |Active       |netbox-napalm-plugin          |netbox_napalm_plugin     |[NAPALM Plugin](https://github.com/netbox-community/netbox-napalm)|
|Toolkit(run commands)    |???   |???   |???    |-----  |Active       |netbox-toolkit-plugin         |netbox_toolkit_plugin    |[NetBox Toolkit Plugin](https://github.com/bonzo81/netbox-toolkit-plugin)|
|Service Path (Maps)      |4.0.? |5.0.x |5.1.2  |-----  |Active       |cesnet_service_path_plugin    |cesnet_service_path_plugin|[cesnet_service_path_plugin](https://github.com/CESNET/cesnet_service_path_plugin)|
|Attachments              |7.2.0 |8.0.4 |9.0.0  |-----  |Active       |netbox-attachments            |netbox_attachment        |[NetBox Attachments](https://github.com/Kani999/netbox-attachments)|
|Documents                |0.7.2 |0.7.4 |0.7.4  |-----  |Active       |netbox-documents              |netbox_documents         |[Documents Plugin](https://github.com/jasonyates/netbox-documents)|
|Inventory                |2.3.1 |2.4.0 |2.4.1  |-----  |Active       |netbox-inventory              |netbox_inventory         |[Inventory Plugin](https://github.com/ArnesSI/netbox-inventory)|
|Contracts                |2.3.2 |2.4.2 |------ |-----  |Active       |netbox-contract               |netbox_contract          |[Contract](https://github.com/mlebreuil/netbox-contract)|
|(Hardware)Lifecycle (EOL)|1.1.5 |1.1.6 |  ???  |-----  |Active       |netbox-lifecycle              |netbox_lifecycle         |[Lifecycle](https://github.com/DanSheps/netbox-lifecycle/releases)|
|Software Lifecycle       |1.8.2 |----  |------ |-----  |Active       |netbox-slm                    |netbox_slm               |[Software Lifecycle](https://github.com/ICTU/netbox_slm)|
|Inventory Monitor Plugin |---   |---   |11.0.2 |-----  |Active       |inventory-monitor             |inventory_monitor        |[Inventory Monitor](https://github.com/CESNET/inventory-monitor-plugin)|
|nbxSync(Zabbix integr.)  |1.0.0 |1.0.0 |1.0.0  |-----  |Active       |nbxsync                       |nbxsync                  |[nbxSync Zabbix integration](https://github.com/OpensourceICTSolutions/nbxsync)|
|Netbox-Zabbix-Sync       |???   |3.2.0 |  ???  |-----  |---          |---                           |---                      |[Script NetBox Zabbix Sync](https://github.com/TheNetworkGuy/netbox-zabbix-sync)|
|Netbox-zabbix            |2.0.3 |---   |------ |-----  |---          |netbox-zabbix                 |                         |[Plugin NetBox Zabbix](https://github.com/DanSheps/netbox-zabbix)|
|Routing Plugin           |0.3.0 |0.3.1 |------ |-----  |Active       |netbox-routing                |                         |[Routing Plugin](https://github.com/DanSheps/netbox-routing)|
|Data Flows               |1.1.0 |1.1.1 |1.4.0  |-----  |Active       |netbox-data-flows             |netbox_data_flows        |[Data Flows](https://github.com/Alef-Burzmali/netbox-data-flows)|
|Config Backup            |2.1.8 |2.1.9 |2.1.9  |-----  |Active       |netbox-config-backup          |netbox_config_backup     |[Config Backup](https://github.com/DanSheps/netbox-config-backup)|
|Validity                 |3.1.3 |3.2.0 |3.3.1  |-----  |Active       |netbox-validity               |validity                 |[Validity](https://github.com/amyasnikov/validity)|
|Config Diff              |2.9.0 |2.10.0|2.11.0 |-----  |Active       |netbox-config-diff            |netbox_config_diff       |[Config Diff](https://github.com/miaow2/netbox-config-diff)|
|nmap Scan                |0.3.2 |0.3.5 |------ |-----  |Active       |---                           |---                      |[NetBox nmap Scan](https://github.com/LoH-lu/netbox-nmap-scan)|
|NetBox IPAM(scanning)    |---   |---   |------ |-----  |---          |---                           |---                      |[Netbox-IPAM](https://github.com/hrleinonen/netbox-ipam)|
|LibreNMS Plugin          |0.3.12|???   |------ |-----  |Active       |netbox-librenms-plugin        |netbox_librenms_plugin   |[LibreNMS Plugin](https://github.com/bonzo81/netbox-librenms-plugin)|
|Promox (ProxBox)         |---   |---   |------ |-----  |---          |netbox-proxbox                |netbox_proxbox           |[ProxBox](https://github.com/netdevopsbr/netbox-proxbox)|
|Windows DHCP Sync        |???   |???   |------ |-----  |???          |---                           |---                      |[Win DHCP](https://github.com/scsitteam/netbox-windhcp)|
|Storage                  |---   |---   |------ |-----  |???          |netbox-storage-plugin         |netbox_storage           |[Storage](https://github.com/viroge/netbox-storage)|
|NAS                      |---   |---   |------ |-----  |???          |netbox-nas                    |netbox_nas               |[NAS](https://github.com/wutcat/netbox-nas)|
|Tunnels 2                |---   |---   |------ |-----  |Discontinued |netbox-tunnels2               |netbox_tunnels2          |[Tunnels 2](https://github.com/robertlynch3/netbox-tunnels2?tab=readme-ov-file)|
|Circuit Mainten.         |0.5.0 |0.5.0 |0.6.0  |-----  |???          |netbox-circuitmaintenance     |netbox_circuitmaintenance|[Circuit Maintenance](https://github.com/jasonyates/netbox-circuitmaintenance)|
|Phonebox Plugin          |---   |---   |------ |-----  |---          |phonebox-plugin               |phonebox_plugin          |[Phonebox](https://github.com/iDebugAll/phonebox_plugin)|
|IP calculator            |1.4.9 |1.4.10|------ |-----  |Active       |netbox-ipcalculator           |netbox_ipcalculator      |[IP calculator](https://github.com/PieterL75/netbox_ipcalculator)|
|MetaType Importer        |0.6.0 |0.7.1 |0.8.0  |-----  |Active       |netbox-metatype-importer      |netbox_metatype_importer |[Metatype Importer](https://github.com/Onemind-Services-LLC/netbox-metatype-importer)|
|Software Manager(Cisco)  |---   |---   |------ |-----  |---          |netbox-plugin-software-manager|software_manager         |[Software manager](https://github.com/alsigna/netbox-software-manager)|
|OS Manager(Cisco)        |---   |---   |------ |-----  |---          |netbox-os-manager             |???                      |[OS manager](https://github.com/jonasnieberle/netbox-os-manager)|
|NetBox Geo               |---   |---   |------ |-----  |---          |---                           |geo                      |[NetBox Geo](https://github.com/wholesailnetworks/netbox-geo)|
|Device Map               |---   |---   |------ |-----  |Unknown      |netbox-plugin-device-map      |netbox_device_map        |[Device Map](https://github.com/drygdryg/netbox-plugin-device-map)|
|Circuit Map              |---   |---   |------ |-----  |Unknown      |netbox-plugin-circuit-map     |netbox_circuit_map       |[Circuit Map](https://github.com/pv2b/netbox-plugin-circuit-map)|
|Device view              |0.1.9 |---   |------ |-----  |Unknown      |netbox-device-view            |netbox_device_view       |[Device View](https://github.com/peterbaumert/netbox-device-view)|
|Netbox_DNS               |---   |---   |------ |-----  |Discontinued |netbox-dns                    |netbox_dns               |[DNS(archive)](https://github.com/auroraresearchlab/netbox-dns)|
|Secretstore              |----- |---   |---    |------ |Discontinued |netbox-secretstore            |netbox_secretstore       |[Secretstore](https://github.com/DanSheps/netbox-secretstore)|
|Device Type Importer     |----- |---   |---    |------ |Discontinued |---                           |---                      |[Device type import](https://github.com/k01ek/netbox-devicetype-importer)|
