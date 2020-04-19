notes = {'C': 0.0, 'C#': 100.0, 'Db': 100.0, 'D': 200.0, 'D#': 300.0, 'Eb': 300.0, 'E': 400.0, 'F': 500.0, 'F#': 600.0,
         'Gb': 600.0, 'G': 700.0, 'G#': 800.0, 'Ab': 800.0, 'A': 900.0, 'A#': 1000.0, 'Bb': 1000.0, 'B': 1100.0, }

justIntonation = [0, 111.73, 203.91, 315.64, 386.31, 498.04, 582.51, 701.96, 813.69, 884.36, 996.09, 1088.27]

nekChand = [2, 269, 500, 704, 886, 1049]


def convert_to_cents(inputmelody):
    inputmelody = inputmelody.split(" ")
    for i in range(len(inputmelody)):
        inputmelody[i] = notes[inputmelody[i]]
    return inputmelody


def closest_note(note, tuning):
    closest = tuning[0]
    for cents in tuning:
        if abs(cents - note) < abs(closest-note):
            closest = cents
    return closest


def map_to_tuning(tune, tuning):
    for note in range(len(tune)):
        tune[note] = closest_note(tune[note], tuning)
    return tune


if __name__ == '__main__':
    melody = input("Notes? ")
    melody = convert_to_cents(melody)
    melody = map_to_tuning(melody, nekChand)
    print(melody)
