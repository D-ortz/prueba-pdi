import sys
import cv2
import numpy as np
import tensorflow as tf
from utilities import focal_tversky, tversky_loss, tversky



# Obtener la ruta de la imagen desde la línea de comandos
image_path = sys.argv[1]
print(image_path)


# Función para preprocesar la imagen
def preprocess_image(image_path):
    # Cargar la imagen utilizando OpenCV
    image = cv2.imread(image_path)
    # Mostrar la imagen utilizando cv2.imshow()
    cv2.imshow('Imagen', prediction)
    # Esperar a que se presione una tecla
    cv2.waitKey(0)
    
    # Realizar el preprocesamiento necesario (por ejemplo, redimensionar, normalizar, etc.)
    resized_image = cv2.resize(image, (256, 256))
    normalized_image = resized_image / 255.0
    # ...
    return normalized_image

# Función para realizar la predicción utilizando el modelo de IA
def predict_image(image):
    # Cargar la arquitectura del modelo desde el archivo JSON
    with open('ResUNet-MRI.json', 'r') as json_file:
        json_savedModel = json_file.read()

    
    # Cargar la arquitectura del modelo
    model_seg = tf.keras.models.model_from_json(json_savedModel)
    
    # Cargar los pesos del modelo desde el archivo HDF5
    model_seg.load_weights('weights_seg.hdf5')
    
    # Compilar el modelo con el optimizador y la función de pérdida adecuados
    adam = tf.keras.optimizers.Adam(lr=0.05, epsilon=0.1)
    model_seg.compile(optimizer=adam, loss=focal_tversky, metrics=[tversky])
    
    # Realizar la predicción en la imagen utilizando el modelo cargado
    prediction = model_seg.predict(np.expand_dims(image, axis=0))
    
    return prediction

def print_image_with_mask(image, mask):
    # Aplica la máscara a la imagen
    masked_image = cv2.bitwise_and(image, image, mask=mask)
    
    # Concatena la imagen original y la imagen con la máscara
    printed_image = np.hstack((image, masked_image))
    
    # Muestra la imagen resultante
    cv2.imshow('Imagen con máscara', printed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    
    

    # Preprocesar la imagen
    preprocessed_image = preprocess_image(image_path)
    
    # Realizar la predicción en la imagen preprocesada
    prediction = predict_image(preprocessed_image)
    
    # Imprimir o devolver el resultado de la predicción
    print(prediction)  # Aquí puedes imprimir el resultado

    # Llama a la función para imprimir la imagen con la máscara
    print_image_with_mask(image, prediction)