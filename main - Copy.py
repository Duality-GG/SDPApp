import cv2
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.graphics.texture import Texture


# Define your Screen classes first
class MainScreen(Screen):
    pass

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    pass

# class ThirdScreen(Screen):
#     pass

# class ThirdScreen(Screen):
    # cap = cv2.VideoCapture(1)
    # while True:
    # # Capture frame-by-frame
    #     ret, frame = cap.read()
    #     if ret:
    #         # Display the resulting frame
    #         cv2.imshow('USB Webcam', frame)

    #         # Press 'q' to exit the video stream
    #         if cv2.waitKey(1) & 0xFF == ord('q'):
    #             break
    #     else:
    #         print("Unable to read frame. Exiting...")
    #         break

    #     # When everything done, release the capture
    #     cap.release()
    #     cv2.destroyAllWindows()

class ThirdScreen(Screen):
    capture = None

    def start_camera(self):
        # This is the URL you might use for a USB connection through DroidCam
        
        # Start the camera capture
        self.capture = cv2.VideoCapture(1)
        
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # Schedule for 30 FPS
    def stop_camera(self):
        # Stop the camera capture
        if self.capture:
            Clock.unschedule(self.update)
            self.capture.release()
            self.capture = None

    def update(self, dt):
        ret, frame = self.capture.read()
        if ret:
            # Convert it to texture
            buf = cv2.flip(frame, 0).tostring()
            texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            texture.blit_buffer(buf, colorfmt='bgr', bufferfmt='ubyte')
            self.ids.camera_image.texture = texture
        else:
            self.stop_camera()


            

class SettingsScreen(Screen):
    settings = {}
    def save_settings(self):
        # This method would collect data from the UI and store it
        ip = self.ids.camera_ip.text
        port = self.ids.camera_port.text
        self.settings['camera_ip'] = ip
        self.settings['camera_port'] = port

        # Here you would add the code to send the settings to the back-end
        print(f"Settings saved: IP={ip}, Port={port}")

    def load_settings(self):
        # This method would load data from the back-end or file
        # For now, it just prints the stored settings
        print(f"Settings loaded: {self.settings}")

# After the classes, load the kv file
Builder.load_file('myapp.kv')

class MyApp(App):
    def build(self):
        # Create the screen manager
        sm = ScreenManager()
        sm.add_widget(MainScreen(name='main'))
        sm.add_widget(FirstScreen(name='first'))
        sm.add_widget(SecondScreen(name='second'))
        sm.add_widget(ThirdScreen(name='third'))
        sm.add_widget(SettingsScreen(name='settings'))
        return sm
    
if __name__ == '__main__':
    MyApp().run()