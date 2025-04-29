import mido

try:
    mid = mido.MidiFile('your_midi_file.mid')
    for i, track in enumerate(mid.tracks):
        print(f'Track {i}: {track.name}')
        for message in track:
            print(message)
except FileNotFoundError:
    print("Error: MIDI file not found.")
except Exception as e:
    print(f"An error occurred: {e}")
