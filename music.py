import tkinter as tk
from tkinter import messagebox
import pygame


class Song:
    def __init__(self, title, artist, duration, filepath):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.filepath = filepath

    def __str__(self):
        return f"{self.title} by {self.artist} ({self.duration} mins)"


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def search_song(self, title):
        for song in self.songs:
            if song.title.lower() == title.lower():
                return song
        return None


# ---------- GUI Music Player ----------
class MusicPlayer:
    def __init__(self, root, playlist):
        self.root = root
        self.playlist = playlist
        self.current_song = None

        # Initialize pygame mixer
        pygame.mixer.init()

        self.root.title("🎵 My Music Player")
        self.root.geometry("400x300")

        # Search entry
        self.search_entry = tk.Entry(root, font=("Arial", 12))
        self.search_entry.pack(pady=10)

        # Buttons
        self.search_btn = tk.Button(root, text="🔍 Search & Play", command=self.search_and_play)
        self.search_btn.pack(pady=5)

        self.stop_btn = tk.Button(root, text="⏹ Stop", command=self.stop_music)
        self.stop_btn.pack(pady=5)

        # Label
        self.now_playing = tk.Label(root, text="No song playing", font=("Arial", 12))
        self.now_playing.pack(pady=20)

    def search_and_play(self):
        title = self.search_entry.get()
        song = self.playlist.search_song(title)
        if song:
            self.current_song = song
            self.now_playing.config(text=f"▶️ Now Playing: {song.title} by {song.artist}")
            pygame.mixer.music.load(song.filepath)
            pygame.mixer.music.play()
        else:
            messagebox.showerror("Not Found", "⚠️ Song not found in playlist")

    def stop_music(self):
        pygame.mixer.music.stop()
        self.now_playing.config(text="⏹ Music Stopped")


# ---------- Example Usage ----------
if __name__ == "__main__":
    root = tk.Tk()

    # Create playlist
    my_playlist = Playlist("My Favorites")
    my_playlist.add_song(Song("Shape of You", "Ed Sheeran", 4, "songs/shape_of_you.mp3"))
    my_playlist.add_song(Song("Blinding Lights", "The Weeknd", 3, "songs/blinding_lights.mp3"))
    my_playlist.add_song(Song("Naatu Naatu", "RRR", 5, "songs/naatu_naatu.mp3"))

    app = MusicPlayer(root, my_playlist)
    root.mainloop()
