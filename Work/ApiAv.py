import requests
import json

# 1. Configuración de tus credenciales
CLIENT_ID = '8ad78a91-0a0e-40df-90c6-25e48e3dd0a7'
CLIENT_SECRET = '5cL3Re63ELZGAaWOMEiG2HcsMddrCtA2WSnQ6Od2AhJU98h62rfkA_RTGmzTBkJuics7tQm5WQq5Otcv61D1TQ'

# URLs de Availity
TOKEN_URL = "https://api.availity.com/v1/token"
CLAIM_URL = "https://api.availity.com/availity/v1/claim-statuses"

def get_access_token():
    """Paso 1: Intercambia tus llaves por un token de acceso temporal."""
    payload = {
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'scope': 'healthcare-hipaa-transactions-demo'
    }
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    
    response = requests.post(TOKEN_URL, data=payload, headers=headers)
    print(f"Token Response Status: {response.status_code}")
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        print(f"Error al obtener token: {response.status_code}")
        print(response.text)
        return None

def check_claim_status(token):
    """Paso 2: Usa el token para consultar el estado de un reclamo (Demo)."""
    # ESCRUTINIO DE ENCABEZADOS (Asegúrate de tener estos exactos)
    
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-HTTP-Method-Override': 'GET',          # ¡Crucial!
        'X-Api-Mock-ID': '400',  # ¡Crucial!
        'accept': 'application/json'
    }

    # DATOS MÁS COMPLETOS PARA EL ESCENARIO 200_FOUND
    data = {
        'payer.id': 'PAYER001',        # ID exacto del pagador demo
        'providers.npi': '1234567890', # NPI exacto del proveedor demo
        'subscriber.memberId': 'ABC12345', # ID exacto del miembro demo
        'patient.lastName': 'DOE',      # Apellido del paciente (mayúsculas)
        'patient.firstName': 'JOHN',    # Nombre del paciente (mayúsculas)
        'patient.birthDate': '1980-01-01',
        'fromDate': '2023-01-01',
        'toDate': '2023-01-01'
    }

    response = requests.post(CLAIM_URL, headers=headers, data=data)

    if response.status_code == 200:
        print("¡Éxito! Respuesta de Availity:")
        print(json.dumps(response.json(), indent=4))
    else:
        print(f"Error en la consulta: {response.status_code}")
        print(response.text)

# Ejecución del script
if __name__ == "__main__":
    access_token = get_access_token()
    if access_token:
       
        check_claim_status(access_token)