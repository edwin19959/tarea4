# Pruebas Automatizadas en Instagram con Selenium

Este proyecto contiene las pruebas automatizadas para la página de Instagram usando la librería Selenium en Python. El objetivo es validar el proceso de login y otros aspectos de la interfaz de Instagram.

## Historias de Usuario

### Historia 1: Login exitoso
**Como** usuario de Instagram  
**Quiero** iniciar sesión en la página  
**Para** poder acceder a mi perfil y ver mi feed.

- **Criterios de aceptación**:  
  - El usuario puede ingresar su nombre de usuario y contraseña.  
  - Después de hacer login, se debe redirigir a la página de perfil.

- **Criterios de rechazo**:  
  - Si las credenciales son incorrectas, se debe mostrar un mensaje de error.

### Historia 2: Mensaje de error al ingresar credenciales incorrectas
**Como** usuario de Instagram  
**Quiero** que se me notifique si las credenciales son incorrectas  
**Para** poder corregirlas y volver a intentar.

- **Criterios de aceptación**:  
  - Si el usuario ingresa un nombre de usuario o contraseña incorrectos, debe ver un mensaje de error.

- **Criterios de rechazo**:  
  - Si se ingresa correctamente el nombre de usuario y la contraseña, no debe aparecer el mensaje de error.

## Requisitos

- Python 3.6 o superior.
- Selenium y WebDriver (ChromeDriver).
  
## Cómo ejecutar las pruebas

1. Instala los requisitos:
   ```bash
   pip install selenium
