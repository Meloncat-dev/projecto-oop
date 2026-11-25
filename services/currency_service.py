from typing import Optional, Tuple

import requests

from config.settings import Settings

class currency_service:
    
    @staticmethod
    def obtener_tipo_cambio(
        moneda_base: str,
        moneda_destino: str
    ) -> Tuple[Optional[dict], str]:
        
        moneda_base = moneda_base.strip().upper()
        moneda_destino = moneda_destino.strip().upper()
        
        if not moneda_base or not moneda_destino:
            return none, "Debe ingresar ambas monedas"
        
        if len(moneda_base) != 3 or len(moneda_destino) != 3:
            return None, "las monedas deben usar codigos de 3 letras"
        
        if moneda_base == moneda_destino:
            return {
                "moneda_base": moneda_base,
                "moneda_destino": moneda_destino,
                "tasa": 1.0
            }, "ambas monedas son iguales"
        
        params = {
            "base": moneda_base,
            "symbols": moneda_destino
        }
        
        try:
            responce = requests.get(Settings.CURRENCY_API_URL,
                params, timeout= Settings.REQUEST_TIMEOUT
            )
            
            responce.raise_for_status()
            data = responce.json()
            
            tasas = data.get("rates", {})
            tasa = tasas.get(moneda_destino)
            
            if tasa is None:
                return None, "no se encontro una tasa para la moneda solicitada"
            
            resultado = {
                "moneda_base": moneda_base,
                "moneda_destino": moneda_destino,
                "tasa": tasa,
                "fecha": data.get("date")
            }
            
            return resultado, "Tipo de cambio obtenido correctamente"
        
        except requests.exceptions.Timeout:
            return None, "tiempod e espera agotado, intente mas tarde"
        except requests.exceptions.ConnectionError:
            return None, "no se pudo conectar con el servicio de cambio"
        except requests.exceptions.HTTPError:
            return None, f"Error {responce.status_code}"
        except (ValueError, requests.exceptions.JSONDecodeError):
            return None, "la api devolvio una respuesta Json invalida"
        except requests.exceptions.RequestException:
            return None, "ocurrio un error al consultar el servicio de cambio"
        