import pynetbox

# Configuration
NETBOX_URL = "http://localhost:8000"
API_TOKEN = "e5f29ba85d8ecf7b40c12b8f8b93a7074e715cbe"  # Remplacez par votre token

# Connexion à NetBox
nb = pynetbox.api(NETBOX_URL, token=API_TOKEN)

def lister_toutes_les_ips():
    """Liste toutes les adresses IP"""
    print("\n=== Liste des adresses IP ===")
    ips = nb.ipam.ip_addresses.all()
    for ip in ips:
        print(f"- {ip.address} | Status: {ip.status} | DNS: {ip.dns_name or 'N/A'}")

def creer_ip(adresse, status="active", dns_name=None, description=None):
    """Crée une nouvelle adresse IP"""
    try:
        nouvelle_ip = nb.ipam.ip_addresses.create(
            address=adresse,
            status=status,
            dns_name=dns_name,
            description=description
        )
        print(f"✓ IP créée avec succès : {nouvelle_ip.address}")
        return nouvelle_ip
    except Exception as e:
        print(f"✗ Erreur lors de la création : {e}")
        return None

def obtenir_prochaine_ip_disponible(prefix):
    """Obtient la prochaine IP disponible dans un préfixe"""
    try:
        prefixe = nb.ipam.prefixes.get(prefix=prefix)
        if prefixe:
            # Obtient la prochaine IP disponible
            available_ips = prefixe.available_ips.list()
            if available_ips:
                prochaine_ip = available_ips[0]['address']
                print(f"✓ Prochaine IP disponible dans {prefix} : {prochaine_ip}")
                return prochaine_ip
            else:
                print(f"✗ Aucune IP disponible dans {prefix}")
                return None
        else:
            print(f"✗ Préfixe {prefix} non trouvé")
            return None
    except Exception as e:
        print(f"✗ Erreur : {e}")
        return None

def rechercher_ip(adresse):
    """Recherche une adresse IP spécifique"""
    try:
        ip = nb.ipam.ip_addresses.get(address=adresse)
        if ip:
            print(f"\n=== Informations sur {adresse} ===")
            print(f"ID: {ip.id}")
            print(f"Status: {ip.status}")
            print(f"DNS: {ip.dns_name or 'N/A'}")
            print(f"Description: {ip.description or 'N/A'}")
            return ip
        else:
            print(f"✗ IP {adresse} non trouvée")
            return None
    except Exception as e:
        print(f"✗ Erreur : {e}")
        return None

def supprimer_ip(adresse):
    """Supprime une adresse IP"""
    try:
        ip = nb.ipam.ip_addresses.get(address=adresse)
        if ip:
            ip.delete()
            print(f"✓ IP {adresse} supprimée avec succès")
            return True
        else:
            print(f"✗ IP {adresse} non trouvée")
            return False
    except Exception as e:
        print(f"✗ Erreur lors de la suppression : {e}")
        return False

def creer_prefix(prefix, status="active", description=None):
    """Crée un nouveau préfixe/réseau"""
    try:
        nouveau_prefix = nb.ipam.prefixes.create(
            prefix=prefix,
            status=status,
            description=description
        )
        print(f"✓ Préfixe créé avec succès : {nouveau_prefix.prefix}")
        return nouveau_prefix
    except Exception as e:
        print(f"✗ Erreur lors de la création du préfixe : {e}")
        return None

# Menu principal
def menu():
    print("\n" + "="*50)
    print("    GESTION AUTOMATISÉE DES IP - NETBOX")
    print("="*50)
    print("1. Lister toutes les IPs")
    print("2. Créer une nouvelle IP")
    print("3. Rechercher une IP")
    print("4. Supprimer une IP")
    print("5. Créer un préfixe/réseau")
    print("6. Obtenir la prochaine IP disponible")
    print("0. Quitter")
    print("="*50)

if __name__ == "__main__":
    while True:
        menu()
        choix = input("\nVotre choix : ").strip()
        
        if choix == "1":
            lister_toutes_les_ips()
        
        elif choix == "2":
            adresse = input("Adresse IP (ex: 192.168.1.10/24) : ").strip()
            dns = input("Nom DNS (optionnel) : ").strip() or None
            desc = input("Description (optionnel) : ").strip() or None
            creer_ip(adresse, dns_name=dns, description=desc)
        
        elif choix == "3":
            adresse = input("Adresse IP à rechercher : ").strip()
            rechercher_ip(adresse)
        
        elif choix == "4":
            adresse = input("Adresse IP à supprimer : ").strip()
            confirmation = input(f"Confirmer la suppression de {adresse}? (oui/non) : ").strip().lower()
            if confirmation == "oui":
                supprimer_ip(adresse)
        
        elif choix == "5":
            prefix = input("Préfixe (ex: 192.168.1.0/24) : ").strip()
            desc = input("Description (optionnel) : ").strip() or None
            creer_prefix(prefix, description=desc)
        
        elif choix == "6":
            prefix = input("Préfixe (ex: 192.168.1.0/24) : ").strip()
            obtenir_prochaine_ip_disponible(prefix)
        
        elif choix == "0":
            print("Au revoir !")
            break
        
        else:
            print("✗ Choix invalide")
        
        input("\nAppuyez sur Entrée pour continuer...")
