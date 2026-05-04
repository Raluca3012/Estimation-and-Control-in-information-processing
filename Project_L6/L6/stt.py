import whisper

model = whisper.load_model("base")

files = ["sound.wav", "sound2.wav", "sound3.wav", "sound4.wav"]

for f in files:
    result = model.transcribe(f, language="ro")
    print(f)
    print(result["text"])
    print("------")