# from flask import Flask, request, jsonify
# import os
# import whisper

# app = Flask(__name__)

# @app.route('/transcribe', methods=['POST'])
# def transcribe():
#     # Get the audio file from the request
#     file = request.files['audio']
#     if not file:
#         return jsonify({'error': 'Audio file not found'}), 400

#     # Read the audio file into memory
#     audio_bytes = file.read()

#     # Initialize the Whisper API client with your API key
#     client = whisper.Client(os.environ.get('WHISPER_API_KEY'))

#     # Call the transcribe method with the audio bytes and the desired output format (text)
#     transcription, err = client.transcribe(audio_bytes, whisper.Output.TEXT)
#     if err:
#         return jsonify({'error': 'Transcription failed'}), 500

#     # Return the transcription as the response
#     return jsonify({'transcription': transcription}), 200

# if __name__ == '__main__':
#     app.run(debug=True, port=8080)


import subprocess
import whisper
model = whisper.load_model("base")

video_in = 'file.wav'
audio_out = 'audio.mp3'

ffmpeg_cmd = f"ffmpeg -i {video_in} -vn -c:a libmp3lame -b:a 192k {audio_out}"

subprocess.run(["ffmpeg", "-i", video_in, "-vn", "-c:a", "libmp3lame", "-b:a", "192k", audio_out])

result = model.transcribe(audio_out)
print(result["text"])