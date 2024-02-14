from tkinter import *
from customtkinter import *
from PIL import Image
import speedtest
import pyttsx3

speed = speedtest.Speedtest()
servernames =[]  
speed.get_servers(servernames)

assist = pyttsx3.init()
def speak(audio):
    assist.say(audio)
    assist.runAndWait()

def submit_btn_cmd():
    global down_speed, up_speed, ping_latency
    down_speed = (speed.download()/(1024000))
    up_speed = (speed.upload()/(1024000))
    ping_latency = speed.results.ping
    down_speed_lbl.configure(text = f'{down_speed:.2f} Mbps')
    up_speed_lbl.configure(text = f'{up_speed:.2f} Mbps')
    ping_latency_lbl.configure(text = f'{ping_latency} ms')

def speak_btn_cmd():
    speak(f'The download speed is {down_speed:.2f} mega bytes per second')
    speak(f'The upload speed is {up_speed:.2f} mega bytes per second')
    speak(f'The ping latency is {ping_latency} milly seconds')

window = CTk()
window.title('Internet Speed Testing')
window.geometry('700x400')
window.resizable(False, False)

img_frame = CTkFrame(window, corner_radius = 0)
img_frame.place(relwidth = 0.5, relheight = 1, relx = 0)

data_frame = CTkFrame(window, fg_color = '#ed644e', corner_radius = 0)
data_frame.place(relwidth = 0.52, relheight = 1, relx = 0.5)

main_img = CTkImage(Image.open('main_img_icon.png'), size = (280, 280))
main_img_lbl = CTkLabel(img_frame, text = '', image = main_img)
main_img_lbl.place(relx = 0.5, rely = 0.5, anchor = CENTER)

title_lbl = CTkLabel(img_frame, text = 'Internet Speed Testing', font = ('Arial', 28))
title_lbl.place(relx = 0.5, rely = 0.15, anchor = CENTER)

submit_btn = CTkButton(img_frame, text = 'Start', fg_color = '#ed644e', height = 40, font = ('Arial', 20), command = submit_btn_cmd)
submit_btn.place(relx = 0.5, rely = 0.85, anchor = CENTER)

down_lbl = CTkLabel(data_frame, text = 'Download Speed', font = ('Arial', 16))
down_speed_lbl = CTkLabel(data_frame, text = '0.0 Mbps', font = ('Arial', 20))
down_lbl.place(relx = 0.5, rely = 0.2, anchor = CENTER)
down_speed_lbl.place(relx = 0.5, rely = 0.26, anchor = CENTER)

up_lbl = CTkLabel(data_frame, text = 'Upload Speed', font = ('Arial', 16))
up_speed_lbl = CTkLabel(data_frame, text = '0.0 Mbps', font = ('Arial', 20))
up_lbl.place(relx = 0.5, rely = 0.4, anchor = CENTER)
up_speed_lbl.place(relx = 0.5, rely = 0.46, anchor = CENTER)

ping_lbl = CTkLabel(data_frame, text = 'Ping', font = ('Arial', 16))
ping_latency_lbl = CTkLabel(data_frame, text = '0.0 ms', font = ('Arial', 20))
ping_lbl.place(relx = 0.5, rely = 0.6, anchor = CENTER)
ping_latency_lbl.place(relx = 0.5, rely = 0.66, anchor = CENTER)

speak_btn = CTkButton(data_frame, text = 'Speak', fg_color = '#dbdbdb', text_color = 'black', height = 40, font = ('Arial', 20), command = speak_btn_cmd)
speak_btn.place(relx = 0.5, rely = 0.85, anchor = CENTER)

window.mainloop()