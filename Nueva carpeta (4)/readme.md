# Pruebas Automatizadas en Instagram con Selenium

#Esta prueba automatizada está diseñada para verificar el proceso de inicio de sesión en Instagram utilizando Selenium y pytest. A continuación te doy una explicación rápida de la prueba:

#Objetivo de la prueba:
#Verificar que el proceso de login en Instagram funciona correctamente, tanto para credenciales correctas como incorrectas.
#Pasos de la prueba:
#Acceder a la página de login de Instagram: La prueba comienza con la apertura de la página de login de Instagram (https://www.instagram.com/accounts/login/).

#Ingresar credenciales:

#Si las credenciales son correctas, el sistema debe permitir el acceso.
#Si las credenciales son incorrectas, el sistema debe mostrar un mensaje de error (por ejemplo, "Tu contraseña no es correcta").
#Validación:

#Se valida si el título de la página contiene "Instagram", lo que indica que el login fue exitoso.
#Si se detecta un mensaje de error, se registra un fallo indicando que las credenciales son incorrectas.
#Generación de Reporte:
#El resultado de la prueba se guarda en un reporte en formato HTML, lo que permite ver si la prueba pasó o falló. El reporte se genera con un nombre único para cada ejecución de la prueba, basado en la fecha y hora.

#¿Cómo se realiza la verificación de credenciales incorrectas?
#Si al ingresar credenciales incorrectas aparece un mensaje de error en la página (por ejemplo, indicando que la contraseña es incorrecta), la prueba detecta este error y marca el test como fallido. Esto asegura que el sistema está validando correctamente los datos de #acceso.
#Herramientas utilizadas:
#Selenium: Para interactuar con el navegador (en este caso, Chrome) y automatizar las acciones del usuario.
#pytest: Para gestionar las pruebas, ejecutar el script y generar los reportes de resultados.
#Resultado esperado:
#Si las credenciales son correctas, el test pasa.
#Si las credenciales son incorrectas, el test también pasa al detectar el error, pero la prueba debe reflejar el fallo en el reporte.

