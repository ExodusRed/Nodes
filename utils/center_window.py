def center_window(root):
        root.update_idletasks()
        sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
        ww, wh = root.winfo_width(), root.winfo_height()

        nw, nh = (sw // 2) - (ww // 2), (sh // 2) - (wh // 2)

        root.geometry(f"+{nw}+{nh - 30}") # -30 accomandation for taskbar

