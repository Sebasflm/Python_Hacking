import socket
import requests
from urllib.parse import urljoin
import sys

def escanear_dominio(dominio):
    """
    Función principal que escanea un dominio y obtiene el código HTTP
    
    Args:
        dominio (str): Dominio a escanear (ej: google.com)
    """
    
    # Validar que el dominio no esté vacío
    if not dominio:
        print("[-] Error: Ingresa un dominio válido")
        return
    
    # Agregar protocolo si no lo tiene
    if not dominio.startswith(('http://', 'https://')):
        dominio = 'https://' + dominio
    
    try:
        # Paso 1: Realizar resolución DNS
        # Extraer el nombre del dominio sin el protocolo
        dominio_sin_protocolo = dominio.replace('https://', '').replace('http://', '').split('/')[0]
        
        print(f"\n[*] Resolviendo DNS para: {dominio_sin_protocolo}")
        
        # Obtener la dirección IP del dominio
        ip = socket.gethostbyname(dominio_sin_protocolo)
        print(f"[+] IP encontrada: {ip}")
        
        # Paso 2: Realizar petición HTTP/HTTPS
        print(f"[*] Enviando petición HTTP a: {dominio}")
        
        # Configurar timeout y headers para simular navegador
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
        
        # Realizar la petición GET con timeout de 10 segundos
        respuesta = requests.get(dominio, headers=headers, timeout=10, verify=False)
        
        # Paso 3: Mostrar resultados
        print(f"\n[+] ========== RESULTADOS ==========")
        print(f"[+] Dominio: {dominio_sin_protocolo}")
        print(f"[+] IP: {ip}")
        print(f"[+] Código HTTP: {respuesta.status_code}")
        print(f"[+] Razón: {respuesta.reason}")
        print(f"[+] URL Final: {respuesta.url}")
        print(f"[+] Longitud del contenido: {len(respuesta.content)} bytes")
        print(f"[+] ==================================\n")
        
        # Interpretación del código de estado
        if 200 <= respuesta.status_code < 300:
            print("[✓] Dominio activo y accesible")
        elif 300 <= respuesta.status_code < 400:
            print("[⚠] Redirección detectada")
        elif 400 <= respuesta.status_code < 500:
            print("[!] Error del cliente (página no encontrada o acceso denegado)")
        elif respuesta.status_code >= 500:
            print("[!] Error del servidor")
            
    except socket.gaierror:
        # Error si no se puede resolver el DNS
        print(f"[-] Error: No se pudo resolver el dominio '{dominio_sin_protocolo}'")
        print("[-] Verifica que el dominio sea correcto")
        
    except requests.exceptions.Timeout:
        # Error si la petición tarda demasiado
        print(f"[-] Error: Timeout - El servidor tardó demasiado en responder")
        
    except requests.exceptions.ConnectionError:
        # Error de conexión
        print(f"[-] Error: No se pudo conectar al dominio")
        
    except Exception as e:
        # Capturar cualquier otro error
        print(f"[-] Error inesperado: {str(e)}")

# Función para escanear múltiples dominios
def escanear_multiples(dominios_lista):
    """
    Escanea varios dominios de una lista
    
    Args:
        dominios_lista (list): Lista de dominios a escanear
    """
    print("[*] Iniciando escaneo de múltiples dominios...\n")
    for dominio in dominios_lista:
        escanear_dominio(dominio)
        print("-" * 50)

# Entrada del programa
if __name__ == "__main__":
    print("=" * 50)
    print("   ESCÁNER DE DOMINIOS - DNS & HTTP")
    print("=" * 50)
    
    # Opción 1: Escanear un dominio individual
    if len(sys.argv) > 1:
        # Si se pasa dominio por línea de comandos
        escanear_dominio(sys.argv[1])
    else:
        # Si se ejecuta sin argumentos, pedir entrada
        dominio = input("\n[?] Ingresa el dominio a escanear (ej: google.com): ").strip()
        escanear_dominio(dominio)
        
        # Preguntar si desea escanear más dominios
        while input("\n[?] ¿Deseas escanear otro dominio? (s/n): ").lower() == 's':
            dominio = input("[?] Ingresa el dominio: ").strip()
            escanear_dominio(dominio)