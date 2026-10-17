import random, pygame
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("resources/themes/black-and-white.json")

app = ctk.CTk()
app.title("Surprise")
app.geometry("500x300")

pygame.mixer.init()
pygame.mixer.set_num_channels(5)
beep = pygame.mixer.Sound("resources/beep.ogg")
beep.set_volume(0.5)

img = ctk.CTkImage(
    light_image=Image.open("resources/error.png"),
    dark_image=Image.open("resources/error.png"),
    size=(30, 30)
)

def surprise():
    if surprise.is_running:
        return
    surprise.is_running = True

    def pop_one(i):
        if i >= 200:
            for window in app.winfo_children():
                if isinstance(window, ctk.CTkToplevel):
                    window.destroy()
            surprise.is_running = False
            return

        surprise_app = ctk.CTkToplevel(master=app)
        surprise_app.title("Warning")
        surprise_app.attributes("-topmost", True)

        width, height = 210, 50
        screen_width = surprise_app.winfo_screenwidth()
        screen_height = surprise_app.winfo_screenheight()

        x = random.randint(0, screen_width - width)
        y = random.randint(0, screen_height - height)

        surprise_app.geometry(f"{width}x{height}+{x}+{y}")

        ctk.CTkLabel(
            master=surprise_app,
            text=" Unknow Error",
            image=img,
            compound="left",
            font=("JetBrains Mono Medium", 20)
        ).pack(expand=True)

        beep.play()
        app.after(200, pop_one, i + 1)

    pop_one(0)

surprise.is_running = False

def close_app():
    if surprise.is_running:
        return
    pygame.mixer.stop()
    pygame.mixer.quit()
    app.destroy()

surprise_button = ctk.CTkButton(
    master=app,
    text="点击有惊喜",
    command=surprise,
    width=300,
    height=150,
    corner_radius=8,
    font=("Noto Sans CJK SC Medium", 45)
)
surprise_button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.protocol("WM_DELETE_WINDOW", close_app)

app.mainloop()