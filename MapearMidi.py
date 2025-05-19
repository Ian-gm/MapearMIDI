from xml.etree.ElementTree import tostring
import mido

try:
    mid = mido.MidiFile('20250407_musica_victoria perdida.mid')
    for i, track in enumerate(mid.tracks):
        print(f'Track {i}: {track.name}')
        for message in track:
            with open('A.txt', 'a') as the_file:
                the_file.write(str(message))
                the_file.write('\n')
            #print(message)
except FileNotFoundError:
    print("Error: MIDI file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
