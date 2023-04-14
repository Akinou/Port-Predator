import socket

# Entrez l'adresse IP ou le nom d'hôte du réseau à analyser
remote_host = input("Entrez l'adresse IP ou le nom d'hôte : ")
# Entrez la plage de ports à analyser
start_port = int(input("Entrez le port de départ : "))
end_port = int(input("Entrez le port de fin : "))

# Fonction pour scanner les ports
def scan_port(remote_host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((remote_host, port))
        if result == 0:
            print(f"Le port {port} est ouvert")
        sock.close()
    except Exception as e:
        print(f"Erreur : {e}")

# Parcourir chaque port de la plage et appeler la fonction de scan de port
for port in range(start_port, end_port + 1):
    scan_port(remote_host, port)
