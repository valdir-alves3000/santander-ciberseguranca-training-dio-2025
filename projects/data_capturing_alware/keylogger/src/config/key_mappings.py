from pynput import keyboard

class KeyMappings:
    
    IGNORED_KEYS = [
        keyboard.Key.shift,
        keyboard.Key.shift_r,
        keyboard.Key.ctrl_l,
        keyboard.Key.ctrl_r,
        keyboard.Key.alt_l,
        keyboard.Key.alt_r,
        keyboard.Key.alt_gr,
        keyboard.Key.caps_lock,
        keyboard.Key.cmd,
        keyboard.Key.cmd_r,
        keyboard.Key.num_lock,
        keyboard.Key.scroll_lock,
        keyboard.Key.print_screen,
        keyboard.Key.pause,
    ]

    SPECIAL_KEYS = {
        keyboard.Key.space: ' ',
        keyboard.Key.enter: '\n',
        keyboard.Key.backspace: '[<]',
        keyboard.Key.tab: '\t',
        keyboard.Key.esc: '[ESC]',
        
        keyboard.Key.up: '[UP]',
        keyboard.Key.down: '[DOWN]',
        keyboard.Key.left: '[LEFT]',
        keyboard.Key.right: '[RIGHT]',
        keyboard.Key.page_up: '[PG_UP]',
        keyboard.Key.page_down: '[PG_DOWN]',
        keyboard.Key.home: '[HOME]',
        keyboard.Key.end: '[END]',
        
        keyboard.Key.f1: '[F1]',
        keyboard.Key.f2: '[F2]',
        keyboard.Key.f3: '[F3]',
        keyboard.Key.f4: '[F4]',
        keyboard.Key.f5: '[F5]',
        keyboard.Key.f6: '[F6]',
        keyboard.Key.f7: '[F7]',
        keyboard.Key.f8: '[F8]',
        keyboard.Key.f9: '[F9]',
        keyboard.Key.f10: '[F10]',
        keyboard.Key.f11: '[F11]',
        keyboard.Key.f12: '[F12]',
        keyboard.Key.f13: '[F13]',
        keyboard.Key.f14: '[F14]',
        keyboard.Key.f15: '[F15]',
        keyboard.Key.f16: '[F16]',
        keyboard.Key.f17: '[F17]',
        keyboard.Key.f18: '[F18]',
        keyboard.Key.f19: '[F19]',
        keyboard.Key.f20: '[F20]',
        
        keyboard.Key.insert: '[INSERT]',
        keyboard.Key.delete: '[DELETE]',
        
        keyboard.Key.num_lock: '[NUM_LOCK]',
    }

    KEYPAD_MAP = {
    '<65027>': '[KP_/]',      
    '<65028>': '[KP_*]',        
    '<65029>': '[KP_-]',      
    '<65030>': '[KP_+]',      
    '<65031>': '[KP_ENTER]',  
    '<65032>': '[KP_.]',      
    }

    KEYPAD_NUMBERS = {
        '<65438>': '0',
        '<65436>': '1', 
        '<65433>': '2',
        '<65435>': '3',
        '<65430>': '4',
        '<65437>': '5',
        '<65432>': '6',
        '<65429>': '7',
        '<65431>': '8',
        '<65434>': '9',
        '<65032>': '.',  
    }