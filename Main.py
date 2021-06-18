from pygame import mixer
from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import filedialog
#Master
master = Tk()
master.title("Musiqa Playeri")
master.configure(background = "gray")
master.iconbitmap("Data/Icon/Music.ico")


current_valume = float(0.5)

def play_song():
	filename = filedialog.askopenfilename(initialdir="C:/",title="Musiqa Fayl Tanlang")
	current_song = filename
	song_title = filename.split("/")
	song_title = song_title[-1]

	try:
		mixer.init()
		mixer.music.load(current_song)
		mixer.music.set_volume(current_valume)
		mixer.music.play()
		song_title_label.config(fg='green',text="" +  str(song_title))
		volume_label.config(fg="green",text="Volume : " + str(current_valume))
	except Exception as a:
		print(a)
		song_title_label.config(fg = "red",text="Error Playing Track")	





def reduce_valume():
	try:
		global current_valume
		if current_valume <=0:
			volume_label.config(fg = "red", text = "Volume : Muted")
			return
		current_valume = current_valume - float(0.1)
		current_valume = round(current_valume,1)
		mixer.music.set_volume(current_valume)
		volume_label.config(fg = "green",text="Volume : " + str(current_valume))
	except Exception as e:
		print(e)
		song_title_label.config(fg = "red",text="Track hasn't been selected yet")	 	
def increase_valume():
	try:
		global current_valume
		if current_valume >=1:
			volume_label.config(fg = "green", text = "Volume : Max")
			return
		current_valume = current_valume + float(0.1)
		current_valume = round(current_valume,1)
		mixer.music.set_volume(current_valume)
		volume_label.config(fg = "green",text="Volume : " + str(current_valume))
	except Exception as e:
		print(e)
		song_title_label.config(fg = "red",text="Track hasn't been selected yet")	 	


def Pause():
	try:
		mixer.music.pause()
	except Exception as e:
		print(e)
		song_title_label.config(fg = "red",text="Track hasn't been selected yet")	
def Resume():
	try:
		mixer.music.unpause()
	except Exception as e:
		print(e)
		song_title_label.config(fg = "red",text="Track hasn't been selected yet")	


#Label
Label(master, text = "Musiqa Playeri",font=("Calibre",15),bg="gray").grid(sticky="N",row=0,padx=120)
#Label(master, text = "please select a music track you would like to play",font=("Calibre",12),fg = "blue").grid(sticky="N",row=1)
Label(master, text = "Valume",font=("Calibre",12),fg = "red",bg="gray").grid(sticky="N",row=4)

song_title_label = Label(master,font=("Calibre",12),bg="gray")
song_title_label.grid(sticky="N",row=3)

volume_label = Label(master,font=("Calibre",12),bg="gray")
volume_label.grid(sticky="N",row=5)

#Button
Button(master,text="Musiqa Tanlang", font=("Calibre", 12),bg="blue",command = play_song).grid(row=2,sticky="N")
Button(master,text="Pause",font=("Calibre",12),bg="gray",command = Pause).grid(row=3,sticky="E")
Button(master,text="Resume",font=("Calibre",12),bg="gray",command = Resume).grid(row=3,sticky="W")
Button(master,text="-",font=("Calibre",12),bg="gray",width=5,command = reduce_valume).grid(row=5,sticky="W")
Button(master,text="+",font=("Calibre",12),bg="gray",width=5,command = increase_valume).grid(row=5,sticky="E")


master.mainloop()