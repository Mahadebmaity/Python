# import time

# def stopwatch(duration):
#     for elapsed in range(duration + 1):
#         mins, secs = divmod(elapsed, 60)
#         timer = f"{mins:02d}:{secs:02d}"
#         print(timer, end="\r")
#         time.sleep(1)
#     print("Stopwatch ended! ⏱️")

# # Example: run stopwatch for 10 seconds
# stopwatch(10)

# --------------------------------------------------------
# GUI formate 

# import tkinter as tk
# import time

# class CountdownApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Countdown Timer ⏳")
#         self.time_left = 10   # default countdown 10s
#         self.running = False

#         self.label = tk.Label(root, text="00:00", font=("Helvetica", 40))
#         self.label.pack(pady=20)

#         self.start_btn = tk.Button(root, text="Start ▶️", command=self.start)
#         self.start_btn.pack(side="left", padx=10)

#         self.pause_btn = tk.Button(root, text="Pause ⏸️", command=self.pause)
#         self.pause_btn.pack(side="left", padx=10)

#         self.reset_btn = tk.Button(root, text="Reset 🔄", command=self.reset)
#         self.reset_btn.pack(side="left", padx=10)

#     def update_timer(self):
#         if self.running and self.time_left > 0:
#             mins, secs = divmod(self.time_left, 60)
#             self.label.config(text=f"{mins:02d}:{secs:02d}")
#             self.time_left -= 1
#             self.root.after(1000, self.update_timer)
#         elif self.time_left == 0:
#             self.label.config(text="Time's up! ⏰")

#     def start(self):
#         if not self.running:
#             self.running = True
#             self.update_timer()

#     def pause(self):
#         self.running = False

#     def reset(self):
#         self.running = False
#         self.time_left = 10
#         self.label.config(text="00:10")

# root = tk.Tk()
# app = CountdownApp(root)
# root.mainloop()

#---------------------------------------------------------

import time

def countdown(seconds):
    paused = False
    while seconds >= 0:
        if not paused:
            mins, secs = divmod(seconds, 60)
            print(f"{mins:02d}:{secs:02d}", end="\r")
            time.sleep(1)
            seconds -= 1
        else:
            print("⏸️ Paused", end="\r")
            time.sleep(1)

        # check user input
        if seconds >= 0:
            cmd = input("Enter command (p=pause, r=resume, q=quit): ").strip().lower()
            if cmd == "p":
                paused = True
            elif cmd == "r":
                paused = False
            elif cmd == "q":
                print("⏹️ Stopped by user.")
                break

    print("\n✅ Countdown Finished!")

# Example: user starts with 10 seconds
countdown(10)
