import pynetbox

NETBOX_URL = "http://localhost:8000"
API_TOKEN = "e5f29ba85d8ecf7b40c12b8f8b93a7074e715cbe"

nb = pynetbox.api(NETBOX_URL, token=API_TOKEN)

# Créer 10 IPs dans un préfixe
prefix = "192.168.100.0/24"
prefixe_obj = nb.ipam.prefixes.get(prefix=prefix)

for i in range(1, 11):
    available_ips = prefixe_obj.available_ips.list()
    if available_ips:
        ip_address = available_ips[0]['address']
        nb.ipam.ip_addresses.create(
            address=ip_address,
            status="active",
            dns_name=f"serveur{i}.exemple.com",
            description=f"Serveur automatique {i}"
        )
        print(f"✓ Créé : {ip_address} - serveur{i}.exemple.com")
