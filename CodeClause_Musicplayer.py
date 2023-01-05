import pygame

# Initialize pygame
pygame.init()

# Prompt the user to enter a song name
song_name = input("Enter the name of a song: ")

try:
    # Load the song
    pygame.mixer.music.load(song_name)

    # Play the song
    pygame.mixer.music.play()

    # Run the game loop
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

except pygame.error as e:
    # There was an error loading or playing the song
    print("Error:", e)
