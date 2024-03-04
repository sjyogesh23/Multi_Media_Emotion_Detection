import text2emotion as te
import nltk
from langdetect import detect
from googletrans import Translator
from word_checker import has_offensive_words, has_threatening_words

def analyze_emotions(text):
    def translate_text(text, src_lang, dest_lang):
        translator = Translator()
        translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
        return translated_text

    result = {}

    language = detect(text)
    translated_text = text
    if language != 'en':
        translated_text = translate_text(text, language, 'en')

    overall_emotion = None
    overall_ipc = None
    if has_offensive_words(translated_text):
        overall_emotion = "Offensive"
        overall_ipc = 249
    elif has_threatening_words(translated_text):
        overall_emotion = "Angry"
        overall_ipc = 503
    else:
        emotions = te.get_emotion(translated_text)
        overall_emotion = max(emotions, key=emotions.get)

    overall_link = None
    if overall_ipc == 249:
        overall_link = "https://devgan.in/ipc/section/249/#:~:text=Whoever%20performs%20on%20any%20Indian,also%20be%20liable%20to%20fine."
    elif overall_ipc == 503:
        overall_link = "https://www.indiacode.nic.in/show-data?actid=AC_CEN_5_23_00037_186045_1523266765688&orderno=570"

    result['wholeText'] = {'text': text, 'emotion': overall_emotion, 'IPC': overall_ipc, 'Link': overall_link}

    sentences = nltk.sent_tokenize(text)
    sentence_results = []
    for sentence in sentences:
        sentence_result = {}
        translated_sentence = sentence
        if language != 'en':
            translated_sentence = translate_text(sentence, language, 'en')

        sentence_emotion = None
        sentence_ipc = None
        if has_offensive_words(translated_sentence):
            sentence_emotion = "Offensive"
            sentence_ipc = 249
        elif has_threatening_words(translated_sentence):
            sentence_emotion = "Angry"
            sentence_ipc = 503
        else:
            emotions = te.get_emotion(translated_sentence)
            sentence_emotion = max(emotions, key=emotions.get)

        sentence_link = None
        if sentence_ipc == 249:
            sentence_link = "https://devgan.in/ipc/section/249/#:~:text=Whoever%20performs%20on%20any%20Indian,also%20be%20liable%20to%20fine."
        elif sentence_ipc == 503:
            sentence_link = "https://www.indiacode.nic.in/show-data?actid=AC_CEN_5_23_00037_186045_1523266765688&orderno=570"

        sentence_result['Sentence'] = sentence
        sentence_result['Emotion'] = sentence_emotion
        sentence_result['IPC'] = sentence_ipc
        sentence_result['Link'] = sentence_link
        sentence_results.append(sentence_result)

    result['sentences'] = sentence_results
    return result

if __name__ == "__main__":
    input_text = "knell down before me. fuck you. i love you"
    result = analyze_emotions(input_text)
    print(result)
