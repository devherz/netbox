import pynetbox

NETBOX_URL = "http://localhost:8000"
API_TOKEN = "e5f29ba85d8ecf7b40c12b8f8b93a7074e715cbe"

nb = pynetbox.api(NETBOX_URL, token=API_TOKEN)

try:
    print("Test de connexion...")
    print(f"Version NetBox: {nb.version}")
    
    print("\nTest de listage des préfixes...")
    prefixes = nb.ipam.prefixes.all()
    print(f"Nombre de préfixes: {len(list(prefixes))}")
    
    print("\n✓ API fonctionne correctement !")
    
except Exception as e:
    print(f"✗ Erreur: {e}")
    import traceback
    traceback.print_exc()
