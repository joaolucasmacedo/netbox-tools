# netbox-tools
A few Tools to improve NetBox usage

See below a selection on NetBox plugins and tools with version compatibility

|Plugin                   |3.7.8 |4.0.11|4.1.11|4.2.3 |Status       |Pip Package                   |configuration.py         |URL                                                             |
|-------------------------|------|------|------|------|-------------|------------------------------|-------------------------|----------------------------------------------------------------|
|Topology Views           |3.9.1 |4.0.0 |4.1.0 |4.2.0 |Active       |netbox-topology-views         |netbox_topology_views    |                                                      |
|NeXtbox UI Plugin        |0.14.0|0.15.0|1.0.3 |1.0.7 |Active       |nextbox-ui-plugin             |nextbox_ui_plugin        |                                                      |
|Netbox Plugin DNS        |0.22.9|1.0.7 |1.1.7 |1.2.1 |Active       |netbox-plugin-dns             |netbox_dns               |                                                      |
|BGP                      |0.12.1|0.13.3|0.14.0|0.15.0|Active       |netbox-bgp                    |netbox_bgp               |                                                      |
|Floorplan                |0.3.6 |0.4.0 |0.5.0 |0.6.0 |Active       |netbox-floorplan-plugin       |netbox_floorplan         |                                                      |
|Reorder Rack             |1.0.0 |1.1.1 |1.1.3 |1.1.3 |Active       |netbox-reorder-rack           |netbox_reorder_rack      |                                                      |
|Netbox Secrets           |1.10.2|2.0.3 |2.1.2 |2.2.0 |Active       |netbox-secrets                |netbox_secrets           |[NetBox Secretstore](https://github.com/DanSheps/netbox-secretstore)|
|ACLs                     |1.5.0 |1.6.1 |1.7.0 |1.8.1 |Active       |netbox-acls                   |netbox_acls              |                                                      |
|NAPALM                   |0.1.9 |0.2.1 |0.3.0 |0.3.1 |Active       |netbox-napalm-plugin          |netbox_napalm_plugin     |                                                      |
|Qrcode                   |0.0.13|0.0.14|0.0.15|0.0.16|Active       |netbox-qrcode                 |netbox_qrcode            |                                                      |
|Attachments              |4.0.2 |5.1.3 |6.0.0 |7.0.0 |Active       |netbox-attachments            |netbox_attachment        |                                                      |
|Documents                |0.6.4 |0.7.0 |0.7.0 |0.7.1 |Active       |netbox-documents              |netbox_documents         |                                                      |
|Inventory                |1.6.0 |2.0.2 |2.2.1 |2.3.0 |Active       |netbox-inventory              |netbox_inventory         |                                                      |
|Contracts                |2.0.14|2.1.2 |2.2.11|2.3.1 |Active       |netbox-contract               |netbox_contract          |                                                      |
|(Hardware)Lifecycle (EOL)|1.0.2 |1.0.4 |1.1.3 |1.1.5 |Active       |netbox-lifecycle              |netbox_lifecycle         |                                                      |
|Software Lifecycle       |1.6.0 |1.7.0 |1.7.0 |1.8.0 |---          |netbox-slm                    |netbox_slm               |                                                      |
|Netbox-zabbix            |???   |2.0.0 |???   |2.0.3 |---          |---                           |---                      |                                                      |
|Data Flows               |0.8.0 |1.0.0 |1.0.6 |1.1.0 |Active       |netbox-data-flows             |netbox_data_flows        |                                                      |
|Validity                 |3.0.5 |3.1.1 |3.1.1 |3.1.1 |Active       |netbox-validity               |validity                 |                                                      |
|nmap Scan                |      |      |      |0.3.2 |Active       |                              |                         |                                                      |
|LibreNMS Plugin          |---   |---   |0.3.5 |0.3.6 |Active       |netbox-librenms-plugin        |netbox_librenms_plugin   |                                                      |
|Config Backup            |2.0.14|???   |2.1.1 |2.1.2 |Active       |netbox-config-backup          |netbox_config_backup     |                                                      |
|Promox (ProxBox)         |---   |---   |---   |---   |---          |netbox-proxbox                |netbox_proxbox           |                                                      |
|Storage                  |---   |---   |0.7.0 |???   |???          |netbox-storage-plugin         |netbox_storage           |                                                      |
|NAS                      |1.0.3 |---   |???   |---   |???          |netbox-nas                    |netbox_nas               |                                                      |
|Tunnels 2                |0.2.9 |---   |---   |---   |Active       |netbox-tunnels2               |netbox_tunnels2          |                                                      |
|Circuit Mainten.         |---   |0.4.2 |???   |---   |???          |netbox-circuitmaintenance     |netbox_circuitmaintenance|                                                      |
|Phonebox Plugin          |0.0.8 |0.0.9 |0.0.10|0.0.11|---          |phonebox-plugin               |phonebox_plugin          |                                                      |
|IP calculator            |1.1   |1.4.5 |1.4.9 |---   |---          |netbox-ipcalculator           |netbox_ipcalculator      |                                                      |
|MetaType Importer        |0.3.2 |0.4.1 |0.5.0 |---   |---          |netbox-metatype-importer      |netbox_metatype_importer |                                                      |
|Software Manager(Cisco)  |---   |---   |---   |---   |---          |netbox-plugin-software-manager|software_manager         |                                                      |
|NetBox Geo               |---   |---   |---   |---   |---          |---                           |geo                      |                                                      |
|Device Map               |---   |---   |---   |---   |Indeterminado|netbox-plugin-device-map      |netbox_device_map        |                                                      |
|Circuit Map              |---   |---   |---   |---   |Indeterminado|netbox-plugin-circuit-map     |netbox_circuit_map       |                                                      |
|Device view              |---   |0.1.5 |0.1.7 |0.1.9 |Indeterminado|netbox-device-view            |netbox_device_view       |                                                      |
|Netbox Topology Plugin   |0.14.2|0.14.3|???   |---   |Indeterminado|netbox-topology-plugin-plugin |netbox_topology_plugin   |                                                      |
|Netbox_DNS               |---   |---   |---   |---   |Discontinued |netbox-dns                    |netbox_dns               |                                                      |
|Secretstore              |---   |---   |---   |---   |Discontinued |netbox-secretstore            |netbox_secretstore       |                                                      |
|Device Type Importer     |---   |---   |---   |---   |Discontinued |---                           |---                      |                                                      |
