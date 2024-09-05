import itertools
import string
import random

caracteres = string.ascii_letters + string.digits

contraseñas_generadas = set()

with open('diccionario_wifi_formato.txt', 'w') as f:
    while len(contraseñas_generadas) < 30:
        # Longitud aleatoria entre 6 y 15
        longitud_aleatoria = random.randint(6, 15)

        # Generar contraseña con longitud aleatoria
        password = ''.join(random.choices(caracteres, k=longitud_aleatoria))

        # Verificar que cumple con las condiciones de seguridad
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            password not in contraseñas_generadas):

            contraseñas_generadas.add(password)
            f.write(password + '\n')
            print(f"Contraseña {len(contraseñas_generadas)}: {password}")

print("Generación completa.")
