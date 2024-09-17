#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyautogui
import time
import keyboard

print("=================================================")
print("Program auto scroll individual dan auto click rata")
print("Pastikan posisi windows 640x320 jika ukuran layar 1920x1080 dan posisi tampilan ada di pojok kanan bawah")
print("=================================================")

# Inisialisasi variabel global
interrupt = False
interrupt_2 = False
repetition_times = 0

# Fungsi untuk menghentikan otomatisasi bagian pertama
def stop_actions():
    global interrupt
    interrupt = True
    print("Perintah berhenti diterima!")

# Fungsi untuk menjalankan aksi di bagian pertama
def perform_actions():
    global interrupt, repetition_times
    interrupt = False
    
    print("Memulai aksi dalam 5 detik...")
    time.sleep(5)  # Tambahkan jeda 5 detik di sini
    
    for cycle in range(repetition_times):
        for window in action_windows:
            if interrupt:
                print("Berhenti...")
                return
            for action in window:
                if interrupt:
                    return
                if action["type"] == "click":
                    x, y = action["pos"]
                    if action.get("double_click"):
                        pyautogui.doubleClick(x, y)
                    else:
                        pyautogui.click(x, y)
                elif action["type"] == "key":
                    pyautogui.press(action["key"])
                time.sleep(action["interval"])
        print(f"Siklus ke {cycle + 1}")

# Menanyakan pengguna jumlah klik tambahan untuk setiap jendela
def get_click_input():
    window_clicks = {}
    print("0 berarti tidak gerak")
    window_names = [
        "atas kiri", 
        "atas tengah", 
        "atas kanan", 
        "bawah kiri", 
        "bawah tengah", 
        "bawah kanan"
    ]
    for i, name in enumerate(window_names, 1):
        while True:
            try:
                clicks = int(input(f"Masukkan jumlah klik tambahan untuk Jendela {name}: "))
                if clicks >= 0:
                    break
                else:
                    print("Silakan masukkan bilangan bulat positif.")
            except ValueError:
                print("Input tidak valid. Silakan masukkan angka.")
        window_clicks[i] = clicks  # Simpan klik tambahan untuk setiap jendela
    return window_clicks

# Dapatkan jumlah klik tambahan untuk setiap jendela
window_clicks = get_click_input()

# Posisi klik yang telah ditentukan sebelumnya untuk setiap jendela
action_windows = []

# Aksi jendela atas kiri
actions_window_atas_kiri = [{"type": "click", "pos": (320, 120), "interval": 0.5}]
actions_window_atas_kiri += [{"type": "click", "pos": (595, 205), "interval": 0.2} for _ in range(window_clicks[1])]
action_windows.append(actions_window_atas_kiri)

# Aksi jendela atas tengah
actions_window_atas_tengah = [{"type": "click", "pos": (960, 120), "interval": 0.5}]
actions_window_atas_tengah += [{"type": "click", "pos": (1235, 205), "interval": 0.2} for _ in range(window_clicks[2])]
action_windows.append(actions_window_atas_tengah)

# Aksi jendela atas kanan
actions_window_atas_kanan = [{"type": "click", "pos": (1600, 120), "interval": 0.5}]
actions_window_atas_kanan += [{"type": "click", "pos": (1875, 205), "interval": 0.2} for _ in range(window_clicks[3])]
action_windows.append(actions_window_atas_kanan)

# Aksi jendela bawah kiri
actions_window_bawah_kiri = [{"type": "click", "pos": (320, 450), "interval": 0.5}]
actions_window_bawah_kiri += [{"type": "click", "pos": (595, 525), "interval": 0.2} for _ in range(window_clicks[4])]
action_windows.append(actions_window_bawah_kiri)

# Aksi jendela bawah tengah
actions_window_bawah_tengah = [{"type": "click", "pos": (960, 450), "interval": 0.5}]
actions_window_bawah_tengah += [{"type": "click", "pos": (1235, 525), "interval": 0.2} for _ in range(window_clicks[5])]
action_windows.append(actions_window_bawah_tengah)

# Aksi jendela bawah kanan
actions_window_bawah_kanan = [{"type": "click", "pos": (1600, 450), "interval": 0.5}]
actions_window_bawah_kanan += [{"type": "click", "pos": (1875, 525), "interval": 0.2} for _ in range(window_clicks[6])]
action_windows.append(actions_window_bawah_kanan)

# Menanyakan pengguna jumlah pengulangan
while True:
    try:
        repetition_times = int(input("Masukkan jumlah pengulangan: "))
        if repetition_times > 0:
            break
        else:
            print("Silakan masukkan bilangan bulat positif.")
    except ValueError:
        print("Input tidak valid. Silakan masukkan angka.")

# Tombol Mulai/Berhenti untuk bagian pertama
start_key = 'f1'
stop_key = 'f2'

# Memantau tombol mulai untuk bagian pertama
keyboard.add_hotkey(start_key, perform_actions)

# Memantau tombol berhenti untuk bagian pertama
keyboard.add_hotkey(stop_key, stop_actions)

# Fungsi untuk menghentikan otomatisasi bagian kedua
def stop_actions_2():
    global interrupt_2
    interrupt_2 = True
    print("Perintah berhenti diterima!")

# Fungsi untuk menjalankan aksi di bagian kedua
def perform_actions_2():
    global interrupt_2
    interrupt_2 = False
    
    print("Memulai aksi dalam 5 detik...")
    time.sleep(5)  # Tambahkan jeda 5 detik di sini
    
    for cycle in range(repetition_times):
        for action in actions_windows_2:
            if interrupt_2:
                print("Berhenti...")
                return
            if action["type"] == "click":
                x, y = action["pos"]
                if action.get("double_click"):
                    pyautogui.doubleClick(x, y)
                else:
                    pyautogui.click(x, y)
            elif action["type"] == "key":
                pyautogui.press(action["key"])
            time.sleep(action["interval"])
        print(f"Siklus ke {cycle + 1}")  # Correct cycle count

# Definisikan urutan aksi untuk bagian kedua
actions_windows_2 = [
    {"type": "click", "pos": (320, 256), "interval": 1},{"type": "click", "pos": (480, 256), "interval": 1},
    {"type": "click", "pos": (960, 256), "interval": 1},{"type": "click", "pos": (1120, 256),"interval": 1},
    {"type": "click", "pos": (1600, 256),"interval": 1},{"type": "click", "pos": (1760, 256),"interval": 1},    
    
    {"type": "click", "pos": (320, 578), "interval": 1},{"type": "click", "pos": (480, 578), "interval": 1},    
    {"type": "click", "pos": (960, 578), "interval": 1},{"type": "click", "pos": (1120, 578),"interval": 1},
    {"type": "click", "pos": (1600, 578),"interval": 1},{"type": "click", "pos": (1760, 578),"interval": 1},
        
    {"type": "click", "pos": (320, 200), "interval": 1},{"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},     {"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},     {"type": "key", "key": "enter", "interval": 1},
    {"type": "key", "key": "tab", "interval": 0.5},     {"type": "key", "key": "enter", "interval": 1},
    {"type": "click", "pos": (595, 200), "interval": 1},{"type": "click", "pos": (595, 200), "interval": 1},
    
    {"type": "click", "pos": (960, 200), "interval": 1}, {"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "enter", "interval": 1},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "enter", "interval": 1},
    {"type": "click", "pos": (1235, 200), "interval": 1},{"type": "click", "pos": (1235, 200), "interval": 1},
    
    {"type": "click", "pos": (1600, 200), "interval": 1},{"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "enter", "interval": 1},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "enter", "interval": 1},
    {"type": "click", "pos": (1875, 200), "interval": 1},{"type": "click", "pos": (1875, 200), "interval": 1},
    
    {"type": "click", "pos": (320, 520), "interval": 1},{"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},     {"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},     {"type": "key", "key": "enter", "interval": 1},
    {"type": "key", "key": "tab", "interval": 0.5},     {"type": "key", "key": "enter", "interval": 1},
    {"type": "click", "pos": (595, 520), "interval": 1},{"type": "click", "pos": (595, 520), "interval": 1},
    
    {"type": "click", "pos": (960, 520), "interval": 1}, {"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "enter", "interval": 1},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "enter", "interval": 1},
    {"type": "click", "pos": (1235, 520), "interval": 1},{"type": "click", "pos": (1235, 520), "interval": 1},
    
    {"type": "click", "pos": (1600, 520), "interval": 1},{"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "tab", "interval": 0.5},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "enter", "interval": 1},
    {"type": "key", "key": "tab", "interval": 0.5},      {"type": "key", "key": "enter", "interval": 1},
    {"type": "click", "pos": (1875, 520), "interval": 1},{"type": "click", "pos": (1875, 520), "interval": 1},
    #=================================================================================================#
]

# Tombol Mulai/Berhenti untuk bagian kedua
start_key_2 = 'f3'
stop_key_2 = 'f4'

# Memantau tombol mulai untuk bagian kedua
keyboard.add_hotkey(start_key_2, perform_actions_2)

# Memantau tombol berhenti untuk bagian kedua
keyboard.add_hotkey(stop_key_2, stop_actions_2)

# Menjalankan script
print(f"Tekan {start_key} untuk memulai set pertama dan {stop_key} untuk menghentikannya.")
print(f"Tekan {start_key_2} untuk memulai set kedua dan {stop_key_2} untuk menghentikannya.")
keyboard.wait()

