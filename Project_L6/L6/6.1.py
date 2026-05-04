#SOUND CLARIFICATION TASK
#USE 2 machines (PCs/laptops...) in which one is the emittor of sound and the 
#other one is the receptor, at a distance of 2m. Use the microphone of the 2nd
#machine to capture the specific sound, via Matlab scheme.. 
#use matlab to apply different strategies(discussed at the beggining of the semester
#to amplify and clarify this received input)
#The test must imply a voice conversation, that are emitted by machine 1,
#received by machine 2.
#USE AI to transform conversation from the output signal into text (STT)
#Measure the error, in relation to distance. Make a chart

import wave
import struct
import os

input_file = "sound.wav"
output_file = "final_clarified_voice.wav"

if not os.path.exists(input_file):
    raise FileNotFoundError("File not found: " + input_file)

with wave.open(input_file, "rb") as wav:
    channels = wav.getnchannels()
    sample_width = wav.getsampwidth()
    Fs = wav.getframerate()
    n_frames = wav.getnframes()
    raw_data = wav.readframes(n_frames)

if sample_width != 2:
    raise ValueError("Use 16-bit PCM WAV")

samples = struct.unpack("<" + "h" * (len(raw_data)//2), raw_data)

# stereo to mono
x = []
if channels == 1:
    for s in samples:
        x.append(s / 32768.0)
else:
    for i in range(0, len(samples), channels):
        avg = sum(samples[i:i+channels]) / channels
        x.append(avg / 32768.0)

# remove DC offset
mean_val = sum(x) / len(x)
x = [v - mean_val for v in x]

# normalize
max_val = max(abs(v) for v in x) + 1e-12
x = [v / max_val for v in x]

# gentle amplification
gain = 1.4
final_signal = []

for v in x:
    y = gain * v

    # prevent clipping
    if y > 1.0:
        y = 1.0
    elif y < -1.0:
        y = -1.0

    final_signal.append(y)

# save output
out = [int(v * 32767) for v in final_signal]
raw_out = struct.pack("<" + "h" * len(out), *out)

with wave.open(output_file, "wb") as wav:
    wav.setnchannels(1)
    wav.setsampwidth(2)
    wav.setframerate(Fs)
    wav.writeframes(raw_out)

print("DONE:", output_file)