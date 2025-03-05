# netbox-tools
A few Tools to improve NetBox usage

See below a selection on NetBox plugins and tools with version compatibility

|Plugin                   |3.7.8 |4.0.11|4.1.11|4.2.3 |Status       |Pip Package                   |configuration.py         |URL                                                             |
|-------------------------|------|------|------|------|-------------|------------------------------|-------------------------|----------------------------------------------------------------|
|Topology Views           |3.9.1 |4.0.0 |4.1.0 |4.2.0 |Active       |netbox-topology-views         |netbox_topology_views    |[Topology Views](https://github.com/netbox-community/netbox-topology-views)|
|NeXtbox UI Plugin        |0.14.0|0.15.0|1.0.3 |1.0.7 |Active       |nextbox-ui-plugin             |nextbox_ui_plugin        |[NeXtbox UI](https://github.com/iDebugAll/nextbox-ui-plugin)|
|Netbox Plugin DNS        |0.22.9|1.0.7 |1.1.7 |1.2.4 |Active       |netbox-plugin-dns             |netbox_dns               |[Plugin DNS](https://github.com/peteeckel/netbox-plugin-dns)|
|BGP                      |0.12.1|0.13.3|0.14.0|0.15.0|Active       |netbox-bgp                    |netbox_bgp               |[Plugin RPKI](https://github.com/menckend/netbox_rpki)|
|RPKI                     |???   |???   |???   |???   |???          |netbox_rpki                   |netbox_rpki              |[Plugin BGP](https://github.com/netbox-community/netbox-bgp)|
|Floorplan                |0.3.6 |0.4.0 |0.5.0 |0.6.0 |Active       |netbox-floorplan-plugin       |netbox_floorplan         |[Floorplan](https://github.com/netbox-community/netbox-floorplan-plugin)|
|Reorder Rack             |1.0.0 |1.1.1 |1.1.3 |1.1.3 |Active       |netbox-reorder-rack           |netbox_reorder_rack      |[Secrets](https://github.com/Onemind-Services-LLC/netbox-secrets)|
|Netbox Secrets           |1.10.2|2.0.3 |2.1.2 |2.2.0 |Active       |netbox-secrets                |netbox_secrets           |[NetBox Secretstore](https://github.com/DanSheps/netbox-secretstore)|
|ACLs                     |1.5.0 |1.6.1 |1.7.0 |1.8.1 |Active       |netbox-acls                   |netbox_acls              |[ACLs](https://github.com/ryanmerolle/netbox-acls)|
|NAPALM                   |0.1.9 |0.2.1 |0.3.0 |0.3.1 |Active       |netbox-napalm-plugin          |netbox_napalm_plugin     |[NAPALM Plugin](https://github.com/netbox-community/netbox-napalm)|
|Qrcode                   |0.0.13|0.0.14|0.0.15|0.0.16|Active       |netbox-qrcode                 |netbox_qrcode            |[QR code](https://github.com/netbox-community/netbox-qrcode)|
|Attachments              |4.0.2 |5.1.3 |6.0.0 |7.0.0 |Active       |netbox-attachments            |netbox_attachment        |[NetBox Attachments](https://github.com/Kani999/netbox-attachments)|
|Documents                |0.6.4 |0.7.0 |0.7.0 |0.7.1 |Active       |netbox-documents              |netbox_documents         |[Documents Plugin](https://github.com/jasonyates/netbox-documents)|
|Inventory                |1.6.0 |2.0.2 |2.2.1 |2.3.0 |Active       |netbox-inventory              |netbox_inventory         |[Inventory Plugin](https://github.com/ArnesSI/netbox-inventory)|
|Contracts                |2.0.14|2.1.2 |2.2.11|2.3.2 |Active       |netbox-contract               |netbox_contract          |[Contract](https://github.com/mlebreuil/netbox-contract)|
|(Hardware)Lifecycle (EOL)|1.0.2 |1.0.4 |1.1.3 |1.1.5 |Active       |netbox-lifecycle              |netbox_lifecycle         |[Lifecycle](https://github.com/DanSheps/netbox-lifecycle/releases)|
|Software Lifecycle       |1.6.0 |1.7.0 |1.7.0 |1.8.0 |Active       |netbox-slm                    |netbox_slm               |[Software Lifecycle](https://github.com/ICTU/netbox_slm)|
|Netbox-zabbix            |???   |2.0.0 |???   |2.0.3 |---          |netbox-zabbix                 |                         |[Plugin NetBox Zabbix](https://github.com/DanSheps/netbox-zabbix)|
|Data Flows               |0.8.0 |1.0.0 |1.0.6 |1.1.0 |Active       |netbox-data-flows             |netbox_data_flows        |[Data Flows](https://github.com/Alef-Burzmali/netbox-data-flows)|
|Validity                 |3.0.5 |3.1.1 |3.1.1 |3.1.1 |Active       |netbox-validity               |validity                 |[Validity](https://github.com/amyasnikov/validity)|
Config Diff               |0.1.0 |2.6.x |2.7.x |2.9.0 |Active       |netbox-config-diff            |netbox_config_diff       |[Config Diff](https://github.com/miaow2/netbox-config-diff)|
|nmap Scan                |      |      |      |0.3.2 |Active       |---                           |---                      |[NetBox nmap Scan](https://github.com/LoH-lu/netbox-nmap-scan)|
|NetBox IPAM(scanning)    |---   |---   |---   |---   |---          |---                           |---                      |[Netbox-IPAM](https://github.com/hrleinonen/netbox-ipam)|
|LibreNMS Plugin          |---   |---   |0.3.5 |0.3.6 |Active       |netbox-librenms-plugin        |netbox_librenms_plugin   |[LibreNMS Plugin](https://github.com/bonzo81/netbox-librenms-plugin)|
|Config Backup            |2.0.14|???   |2.1.1 |2.1.8 |Active       |netbox-config-backup          |netbox_config_backup     |[Config Backup](https://github.com/DanSheps/netbox-config-backup)|
|Promox (ProxBox)         |---   |---   |---   |---   |---          |netbox-proxbox                |netbox_proxbox           |[ProxBox](https://github.com/netdevopsbr/netbox-proxbox)|
|Windows DHCP Sync        |???   |???   |???   |???   |???          |---                           |---                      |[Win DHCP](https://github.com/scsitteam/netbox-windhcp)|
|Storage                  |---   |0.7.0 |0.7.0 |???   |???          |netbox-storage-plugin         |netbox_storage           |[Storage](https://github.com/viroge/netbox-storage)|
|NAS                      |1.0.3 |---   |???   |---   |???          |netbox-nas                    |netbox_nas               |[NAS](https://github.com/wutcat/netbox-nas)|
|Tunnels 2                |0.2.9 |---   |---   |---   |Active       |netbox-tunnels2               |netbox_tunnels2          |[Tunnels 2](https://github.com/robertlynch3/netbox-tunnels2?tab=readme-ov-file)|
|Circuit Mainten.         |---   |0.4.2 |???   |---   |???          |netbox-circuitmaintenance     |netbox_circuitmaintenance|[Circuit Maintenance](https://github.com/jasonyates/netbox-circuitmaintenance)|
|Phonebox Plugin          |0.0.8 |0.0.9 |0.0.10|0.0.11|---          |phonebox-plugin               |phonebox_plugin          |[Phonebox](https://github.com/iDebugAll/phonebox_plugin)|
|IP calculator            |1.1   |1.4.5 |1.4.9 |---   |---          |netbox-ipcalculator           |netbox_ipcalculator      |[IP calculator](https://github.com/PieterL75/netbox_ipcalculator)|
|MetaType Importer        |0.3.2 |0.4.1 |0.5.0 |0.6.0 |Active       |netbox-metatype-importer      |netbox_metatype_importer |[Metatype Importer](https://github.com/Onemind-Services-LLC/netbox-metatype-importer)|
|Software Manager(Cisco)  |---   |---   |---   |---   |---          |netbox-plugin-software-manager|software_manager         |[Software manager](https://github.com/alsigna/netbox-software-manager)|
|NetBox Geo               |---   |---   |---   |---   |---          |---                           |geo                      |[NetBox Geo](https://github.com/wholesailnetworks/netbox-geo)|
|Device Map               |---   |---   |---   |---   |Indeterminado|netbox-plugin-device-map      |netbox_device_map        |[Device Map](https://github.com/drygdryg/netbox-plugin-device-map)|
|Circuit Map              |---   |---   |---   |---   |Indeterminado|netbox-plugin-circuit-map     |netbox_circuit_map       |[Circuit Map](https://github.com/pv2b/netbox-plugin-circuit-map)|
|Device view              |---   |0.1.5 |0.1.7 |0.1.9 |Indeterminado|netbox-device-view            |netbox_device_view       |[Device View](https://github.com/peterbaumert/netbox-device-view)|
|Netbox_DNS               |---   |---   |---   |---   |Discontinued |netbox-dns                    |netbox_dns               |[DNS(archive)](https://github.com/auroraresearchlab/netbox-dns)|
|Secretstore              |---   |---   |---   |---   |Discontinued |netbox-secretstore            |netbox_secretstore       ||
|Device Type Importer     |---   |---   |---   |---   |Discontinued |---                           |---                      ||
