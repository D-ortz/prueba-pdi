from flask import Flask, request, jsonify
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_image():
    # Verifica si se ha recibido un archivo
    if 'file' not in request.files:
        return jsonify({'error': 'No se recibió ningún archivo'}), 400

    # Lee el archivo de la solicitud
    file = request.files['file']

    # Lee la imagen usando OpenCV
    img_bytes = file.read()
    nparr = np.frombuffer(img_bytes, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Realiza el procesamiento de la imagen (aquí puedes llamar a tu función de predicción)
    # Por ejemplo:
    # prediction = predict_image(img)

    # Devuelve el resultado (aquí puedes devolver el resultado de la predicción)
    return jsonify({'result': 'La imagen fue recibida y procesada correctamente'}), 200

if __name__ == '__main__':
    app.run(debug=True)
