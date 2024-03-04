import whisper
import re



def analyze_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, fp16=False)
    result_text = result["text"]
    sentences = re.split(r'[.!?] ', result_text)
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    print(sentences)
    return sentences
