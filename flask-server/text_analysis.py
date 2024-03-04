import numpy as np
import joblib
import nltk
from nltk.tokenize import sent_tokenize
from collections import Counter
from langdetect import detect
from googletrans import Translator

nltk.download('punkt')
pipe_lr = joblib.load(open("text_emotion.pkl", "rb"))

emotions_emoji_dict = {
    "anger": "😠", "disgust": "🤮", "fear": "😨", "happy": "🤗", "joy": "😃",
    "neutral": "😐", "love": "❤", "sadness": "😔", "shame": "😳", "surprise": "😮"
}

def detect_language(text):
    try:
        lang = detect(text)
        return lang
    except:
        return "unknown"

def translate_to_english(text):
    translator = Translator()
    translated_text = translator.translate(text, src='auto', dest='en').text
    return translated_text

def predict_emotions(docx):
    results = pipe_lr.predict([docx])
    probabilities = pipe_lr.decision_function([docx])[0]
    max_prob_index = np.argmax(probabilities)
    predicted_emotion = results[0]
    confidence = probabilities[max_prob_index]
    return predicted_emotion, confidence

def analyze_text(text):
    lang = detect_language(text)
    if lang != 'en':
        text = translate_to_english(text)
    
    sentences = sent_tokenize(text)
    
    overall_emotions = []
    emotions_data = []
    for sentence in sentences:
        prediction, confidence = predict_emotions(sentence)
        overall_emotions.append(prediction)
        emotions_data.append({'Sentence': sentence, 'Emotion': prediction, 'Confidence': confidence})
    
    overall_emotion = max(set(overall_emotions), key=overall_emotions.count)
    overall_emoji = emotions_emoji_dict[overall_emotion]
    
    confidence_overall = overall_emotions.count(overall_emotion) / len(overall_emotions)
    
    emotion_counts = Counter(overall_emotions)
    plot_data = [{"Emotion": emotion, "Count": count} for emotion, count in emotion_counts.items()]
    print(overall_emotion)
    return overall_emotion, overall_emoji, confidence_overall, emotions_data, plot_data
