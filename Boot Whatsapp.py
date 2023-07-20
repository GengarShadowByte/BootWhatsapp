from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time
import tkinter as tk
from tkinter import ttk

# Ruta del chromedriver (descargar de https://sites.google.com/a/chromium.org/chromedriver/downloads)
PATH_CHROMEDRIVER = 'chromedriver.exe'

# ...

def enviar_mensaje_whatsapp(contactos, mensaje):
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(executable_path=PATH_CHROMEDRIVER, options=options)
    
    driver.get('https://web.whatsapp.com/')
    input("Escanee el código QR de WhatsApp y luego presione Enter para continuar...")
    
    for contacto in contactos:
        try:
            WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, '[title="WhatsApp"]')))
            search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))
            search_box.clear()
            search_box.send_keys(contacto)
            search_box.send_keys(Keys.ENTER)
            time.sleep(3)

            try:
                message_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')))
                message_box.send_keys(mensaje)
                message_box.send_keys(Keys.ENTER)
                time.sleep(2)
            except TimeoutException:
                print(f"No se pudo enviar mensaje a {contacto}. No se encontró el cuadro de mensaje.")
            except Exception as e:
                print(f"No se pudo enviar mensaje a {contacto}. Error: {str(e)}")
        except TimeoutException:
            print(f"No se pudo enviar mensaje a {contacto}. No se encontró el cuadro de búsqueda.")
        except NoSuchElementException:
            print(f"No se pudo enviar mensaje a {contacto}. Elemento no encontrado.")
        except Exception as e:
            print(f"No se pudo enviar mensaje a {contacto}. Error: {str(e)}")
    
    driver.quit()

def enviar_mensajes():
    contactos = entrada_contactos.get("1.0", tk.END).strip().split("\n")
    mensaje = entrada_mensaje.get("1.0", tk.END).strip()
    
    enviar_mensaje_whatsapp(contactos, mensaje)

# Crear la ventana
ventana = tk.Tk()
ventana.title("Enviar Mensajes de WhatsApp")

# Crear una etiqueta y una caja de texto para ingresar los contactos
etiqueta_contactos = tk.Label(ventana, text="Ingrese los números de teléfono (uno por línea):")
etiqueta_contactos.pack(pady=5)

entrada_contactos = tk.Text(ventana, height=5, width=40)
entrada_contactos.pack()

# Crear una etiqueta y una caja de texto para ingresar el mensaje
etiqueta_mensaje = tk.Label(ventana, text="Ingrese el mensaje:")
etiqueta_mensaje.pack(pady=5)

entrada_mensaje = tk.Text(ventana, height=5, width=40)
entrada_mensaje.pack()

# Crear un botón para enviar los mensajes
boton_enviar = tk.Button(ventana, text="Enviar Mensajes", command=enviar_mensajes)
boton_enviar.pack(pady=10)

# Ejecutar el bucle de eventos
ventana.mainloop()
