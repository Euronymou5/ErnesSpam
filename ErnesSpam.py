import webbrowser
import time
import pyautogui

def init():
    mensaje = pyautogui.password(text='Ingresa el mensaje que quieres enviar', title='ErnesSpam', default='', mask='')
    cantidad = int(pyautogui.password(text='¿Cuantas veces quieres enviar el mensaje? Ingresa un numero entero', title='ErnesSpam', default='', mask=''))
    pyautogui.alert(text='Antes de mandar el spam debes de entrar al chat donde quieres mandar el spam.', title='Advertencia', button='OK')
    pyautogui.alert(text='Se abrira whatsapp web donde tendras que entrar a tu whatsapp escanenado el codigo qr', title='Advertencia', button='OK')
    a = pyautogui.confirm(text='Confirmar abrir whatsapp?', title='', buttons=['OK', 'Cancel'])
    if a == "OK":
        webbrowser.open_new_tab('https://web.whatsapp.com/')
        confirmar = pyautogui.confirm(text='Una vez ya estes dentro del chat presiona el boton Aceptar para empezar el spam.', title='ErnesSpam', buttons=['OK', 'Cancel'])
        if confirmar == "OK":
            pyautogui.alert(text='Comenzando el ataque en 10 segundos...', title='ErnesSpam', button='OK')
            time.sleep(10)
            for _ in range(cantidad):
                pyautogui.typewrite(mensaje)
                pyautogui.keyDown('enter')
                time.sleep(0.5)
                pyautogui.keyDown('enter')
        else:
          pyautogui.alert(text='Spam Cancelado.', title='', button='OK')
          exit()
    else:
        pyautogui.alert(text='Spam Cancelado.', title='Spam cancelado', button='OK')
        exit()
        
init()
