import tkinter as tk
import script

def GUI():
    #create the root window
    root = tk.Tk()

    #set the title
    root.title("Image-Analysis-Detecting-car-models")

    #set the size
    root_width = 800
    root_height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - root_width / 2)
    center_y = int(screen_height/2 - root_height / 2)
    root.geometry(f'{root_width}x{root_height}+{center_x}+{center_y}')
    root.resizable(False, False)

    #learning frame
    frame_learning = tk.Frame(master=root, width=800, height=70)
    frame_learning.pack(fill=tk.BOTH, expand=True)

    label_output_learning = tk.Label(master=frame_learning, text="", width=95, height=4, borderwidth=1, relief="solid")
    label_output_learning.place(x=200, y=10)

    button_initalize = tk.Button(master=frame_learning, text="Initialize model", width=10, height=3)
    button_initalize.place(x=10, y=10)
    button_initalize.bind("<Button-1>", script.button_initalize)

    #image load frame
    frame_image = tk.Frame(master=root, width=800, height=460)
    frame_image.pack(fill=tk.BOTH, expand=True)

    frame_image_loaded = tk.Frame(master=frame_image, width=600, height=400, borderwidth=1, relief="solid")
    frame_image_loaded.place(x=30, y=30)

    button_load_image = tk.Button(master=frame_image, text="Load image", width=10, height=3)
    button_load_image.place(x=670, y=50)
    button_load_image.bind("<Button-1>", script.button_load_image)

    button_detect = tk.Button(master=frame_image, text="Detect image", width=10, height=3)
    button_detect.place(x=670, y=120)
    button_detect.bind("<Button-1>", script.button_detect)

    #output frame
    frame_output = tk.Frame(master=root, width=800, height=70)
    frame_output.pack(fill=tk.BOTH, expand=True)

    label_output_detect = tk.Label(master=frame_output, text="", width=130, height=4, borderwidth=1, relief="solid")
    label_output_detect.place(x=10, y=10)

    root.mainloop()