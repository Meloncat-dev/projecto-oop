from typing import Optional, Tuple

import requests

from config.settings import Settings

class weather_service:
    
    WEATHER_CODES = {
        0: "Despejado",
        1: "Mayormente despejado",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Niebla",
        48: "Niebla con escarcha",
        51: "Llovizna ligera",
        53: "Llovizna moderada",
        55: "Llovizna intensa",
        61: "Lluvia ligera",
        63: "Lluvia moderada",
        65: "Lluvia intensa",
        71: "Nieve ligera",
        73: "Nieve moderada",
        75: "Nieve intensa",
        80: "Chubascos ligeros",
        81: "Chubascos moderados",
        82: "Chubascos violentos",
        95: "Tormenta eléctrica"
    }
    
    @classmethod
    def obtener_clima(cls, latitud: float, longitud: float) -> Tuple[Optional[dict], str]:
        params = {
            "latitude": latitud,
            "longitude": longitud,
            "current": "temperature_2m,weather_code",
            "timezone": "auto"
        }
        
        try:
            response = requests.get(
                Settings.WEATHER_API_URL,
                params,
                timeout=Settings.REQUEST_TIMEOUT
            )
            
            response.raise_for_status()
            data = response.json()
            
            current = data.get("current", {})
            
            temperatura = current.get("temperature_2m")
            codigo = current.get("weather_code")
            
            if temperatura is None or codigo is None:
                return None, "la respuesta no contiene los datos esperados"
            
            resultado = {
                "temperatura": temperatura,
                "condicion": cls.WEATHER_CODES.get(codigo, "condicion desconosida")
            }
            return resultado, "informacion obtenida correctamente"
        except requests.exceptions.Timeout:
            return None, "tiempo de espera agotado, intente mas tarde"
        except requests.exceptions.ConnectionError:
            return None, "error en la coneccion"
        except requests.exceptions.HTTPError:
            return None, f"Error {response.status_code}"
        except (ValueError, requests.exceptions.JSONDecodeError):
            return None, "la api devolvio una respuesta Json invalida"
        except requests.exceptions.RequestException:
            return None, "ocurrio un error al consultar el servicio metereologico"