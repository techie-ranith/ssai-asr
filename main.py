from flask import Flask, request, jsonify
import whisper
import librosa
import numpy as np


app = Flask(__name__)


@app.route('/audio', methods=['POST'])

def upload_file():
    uploaded_file = request.files['audio']
    if uploaded_file:
        print("file fetched to python script")
        # Load the audio file as a numpy array

        audio, sr = librosa.load(uploaded_file, sr=None)

        model = whisper.load_model("base")
        result = model.transcribe(audio)
        transcribed_text = result["text"]

        with open("output.txt", 'w') as f:
            f.write(transcribed_text)
            print("done")
        # Return the transcribed text as a JSON response
        return jsonify({'text': transcribed_text})
    else:
        error = "No file was uploaded."
        return jsonify({'error': error})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
