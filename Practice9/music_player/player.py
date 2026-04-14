import pygame
import os

class MusicPlayer:
    def __init__(self):
        pygame.mixer.init()

        BASE_DIR = os.path.dirname(__file__)

        self.tracks = [
            os.path.join(BASE_DIR, "music", "sample_tracks", "Radio.mp3"),
            os.path.join(BASE_DIR, "music", "sample_tracks", "Yrban.mp3"),
            os.path.join(BASE_DIR, "music", "sample_tracks", "Shum.mp3"),
        ]
        self.current = 0

        self.font = pygame.font.SysFont(None, 36)
        self.small_font = pygame.font.SysFont(None, 28)

    def play(self):
        pygame.mixer.music.load(self.tracks[self.current])
        pygame.mixer.music.play()

    def stop(self):
        pygame.mixer.music.stop()

    def next(self):
        self.current = (self.current + 1) % len(self.tracks)
        self.play()

    def prev(self):
        self.current = (self.current - 1) % len(self.tracks)
        self.play()

    def draw(self, screen):
        # Заголовок
        title = self.font.render("Playlist:", True, (255, 255, 255))
        screen.blit(title, (50, 80))

        # Список треков
        for i, track in enumerate(self.tracks):
            name = os.path.basename(track)

            # текущий трек выделяем
            if i == self.current:
                text = self.small_font.render(f"> {name}", True, (0, 255, 0))
            else:
                text = self.small_font.render(name, True, (200, 200, 200))

            screen.blit(text, (70, 120 + i * 40))

        # Подсказки управления
        controls = self.small_font.render("P-Play S-Stop N-Next B-Back Q-Quit", True, (180, 180, 180))
        screen.blit(controls, (50, 300))