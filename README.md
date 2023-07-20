# WhatsApp Message Sender BETA NO TERMINADA

Esta es una aplicación de escritorio desarrollada en Python utilizando Tkinter y Selenium que te permite enviar mensajes de WhatsApp a varios contactos a través de WhatsApp Web.

## Requisitos

- Python 3.x
- Paquete `selenium` (`pip install selenium`)
- ChromeDriver (descargar de https://sites.google.com/a/chromium.org/chromedriver/downloads)

## Configuración

1. Asegúrate de tener instalado Python 3.x en tu sistema.
2. Instala el paquete `selenium` ejecutando el siguiente comando:
   ```
   pip install selenium
   ```
3. Descarga ChromeDriver desde el sitio web oficial: https://sites.google.com/a/chromium.org/chromedriver/downloads
4. Coloca el archivo descargado `chromedriver.exe` en el mismo directorio que el script de Python o proporciona la ruta correcta en la variable `PATH_CHROMEDRIVER` en el código.

## Uso

1. Ejecuta el script de Python `whatsapp_message_sender.py`.
2. Se abrirá la ventana de la aplicación.
3. Ingresa los números de teléfono de los contactos a los que deseas enviar mensajes (uno por línea) en el primer cuadro de texto.
4. Escribe el mensaje que deseas enviar en el segundo cuadro de texto.
5. Haz clic en el botón "Enviar Mensajes".
6. La aplicación abrirá WhatsApp Web en el navegador Chrome.
7. Escanea el código QR para iniciar sesión en tu cuenta de WhatsApp.
8. La aplicación buscará automáticamente a cada contacto y les enviará el mensaje uno por uno.

**Nota:** WhatsApp Web generalmente requiere que escanees un código QR para iniciar sesión en tu cuenta antes de usar esta aplicación. El código incluye una instrucción `input()` para esperar hasta que hayas escaneado el código QR antes de continuar con el envío de mensajes.

## Descargo de responsabilidad

El envío de mensajes a través de WhatsApp Web utilizando métodos automatizados puede estar sujeto a limitaciones o restricciones impuestas por WhatsApp. Esta aplicación se proporciona únicamente con fines educativos y debe utilizarse de manera responsable y cumpliendo con los términos de servicio de WhatsApp.

## Importante

Por favor, asegúrate de tener los permisos necesarios para enviar mensajes a los contactos seleccionados. El envío de mensajes no solicitados o no autorizados puede violar las políticas de WhatsApp.
