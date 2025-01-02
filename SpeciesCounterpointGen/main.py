perfect_consonances = [1, 5]
imperfect_consonances = [3, 6]
dissonances = [2, 4, 7]
possible_intervals = perfect_consonances + imperfect_consonances

scale = ["C", "D", "E", "F", "G", "A", "B"]

def decode_sequence(codes: tuple[int]) -> tuple[str]:
    def decode_note(code: int) -> str:
        code = code-1
        octave = str(code//len(scale) - 1)
        pitch_class = scale[code%len(scale)]
        return pitch_class + octave
    
    return tuple(decode_note(code) for code in codes)

def encode_sequence(notes: tuple[str]) -> tuple[int]:
    def encode_note(note: str) -> int:
        pitch = note[:-1]
        octave = int(note[-1])
        assert (pitch in scale), f"Note {pitch} is not in scale"
        pitch_class = scale.index(pitch)+1
        return pitch_class + len(scale) * (octave + 1)
    
    return tuple(encode_note(note) for note in notes)

def generate_first_species(melodic_line: tuple[int]) -> tuple[int]:
    pass

if __name__ == "__main__":
    cantus_firmus = ("C4", "B3", "G3", "A3", "B3", "C4", "A3", "G3", "E3", "A3", "G3", "F3", "E3", "F3", "D3", "C3")
    encoded = encode_sequence(cantus_firmus)
    print(encoded)
    print(decode_sequence(encoded))