import os
import sys
from pydub import AudioSegment


def convert_mp3_to_wav(mp3_folder, wav_folder):
    if not os.path.exists(wav_folder):
        os.makedirs(wav_folder)

    for filename in os.listdir(mp3_folder):
        if filename.endswith('.mp3'):
            mp3_path = os.path.join(mp3_folder, filename)
            wav_path = os.path.join(wav_folder, os.path.splitext(filename)[0] + '.wav')
            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format='wav')
            print(f'Converted {filename} to WAV')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python audio_converter.py <mp3_folder> <wav_folder>')
        sys.exit(1)

    mp3_folder = sys.argv[1]
    wav_folder = sys.argv[2]

    convert_mp3_to_wav(mp3_folder, wav_folder)