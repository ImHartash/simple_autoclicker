import sys

import threading

from time import sleep

import keyboard
import mouse

from pynput.keyboard import Key, Listener

from PySide6.QtWidgets import QApplication, QMainWindow

from ui_main import Ui_MainWindow


class SimpleAutoClicker(QMainWindow):
    def __init__(self):
        super(SimpleAutoClicker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # My needs
        self.version = 'v0.31'
        self.start_thread = None
        self.click_thread = None
        
        self.accept_letters = 'qwertyuiopasdfghjklzxcvbnm1234567890'
        
        self.stop_thread = False
        self.is_active = True
        
        # Functions
        # self.set_settings()
        
        self.ui.lbl_version.setText(self.version)
        
        self.ui.btn_status.clicked.connect(self.status_clicked)
    
    
    def status_clicked(self) -> None:
        status = self.ui.btn_status
        
        if status.isChecked():
            try:
                
                time_sleep = float(self.ui.le_timesleep.text())
                key_code = self.ui.le_keycode.text().lower()
                is_mouse_enabled = self.ui.cb_mouseenable.isChecked()
                
            except ValueError:
                
                status.setChecked(False)
                self.ui.le_keycode.clear()
                self.ui.le_timesleep.clear()
                
                return
                
            if 100 > time_sleep > 0.01 and key_code in self.accept_letters:
                print("Good")
                
                # Functions
                if not self.click_thread or not self.click_thread.is_alive():
                    self.click_thread = threading.Thread(target=self.run_loop, daemon=True, args=(key_code, is_mouse_enabled, time_sleep))
                    self.click_thread.start()
                
                
            else:
                status.setChecked(False)
                self.ui.le_keycode.clear()
                self.ui.le_timesleep.clear()
        
        else:
            self.click_thread = None
    
    
    def run_loop(self, key_code: str, is_mouse_enabled: bool, timesleep: float) -> None:
        print("Starting Loop.")
        
        if not is_mouse_enabled:
            while self.ui.btn_status.isChecked():
                sleep(timesleep)
                keyboard.press_and_release(key_code)
        else:
            while self.ui.btn_status.isChecked():
                sleep(timesleep)
                keyboard.press_and_release(key_code)
                mouse.click(button='left')
                
    
    def pressed_hotkey(self, key) -> None:
        if key == Key.f6:
            self.ui.btn_status.click()
    
    
    def listen(self):
            with Listener(on_press=self.pressed_hotkey) as listener:
                listener.join()
    
    
    def check_mouse(self) -> bool:
        return self.ui.cb_mouseenable.isCheckable

    def set_settings(self) -> str:
        with open('settings.txt', 'r') as file:
            TimeSleep = file.readline(1)
            KeyCode = file.readline(2)
            MouseIsUsed = file.readline(3)
            
            print(f'TimeSleep: {TimeSleep}, KeyCode: {KeyCode}, Mouse: {MouseIsUsed}')
            print(type(KeyCode))
    


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SimpleAutoClicker()
    window.show()
    print("Window showed.")
    
    new_thread = threading.Thread(target=window.listen, daemon=True)
    new_thread.start()
    print("Thread started.")

    sys.exit(app.exec())