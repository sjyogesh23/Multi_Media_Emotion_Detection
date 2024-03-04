import os
from flask import Flask, request, jsonify
from img_analysis import analyze_image
from text_analysis import analyze_text
from audio_analysis import analyze_audio
from new_ana import analyze_emotions

app = Flask(__name__)

@app.route("/analyze-text", methods=["POST"])
def analyze_text_route():
    data = request.json
    text = data.get("text")
    print(text)
    analysis_result = analyze_emotions(text)
    
    return jsonify(analysis_result)


@app.route("/analyze-image", methods=["POST"])
def analyze_image_route():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    UPLOAD_FOLDER = 'images'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(UPLOAD_FOLDER, 'emo_img.jpg')
    file.save(file_path)

    try:
        paragraph = analyze_image(file_path)
        return jsonify({"message": "Image saved and analyzed successfully.", "result": paragraph})
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@app.route("/analyze-audio", methods=["POST"])
def analyze_audio_route():
    if 'audio' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['audio']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    UPLOAD_FOLDER = 'audio'
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    file_path = os.path.join(UPLOAD_FOLDER, 'emo_aud.wav')
    file.save(file_path)

    try:
        sentences = analyze_audio(file_path)
        return jsonify({"message": "Audio saved and analyzed successfully.", "result": sentences})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
