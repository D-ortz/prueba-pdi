<?php
if(isset($_FILES["file"])){
    $name = $_FILES["file"]["name"];
    $file = $_FILES["file"]["tmp_name"];
    $error = $_FILES["file"]["error"];
    $destination = "uploads/$name"; // Carpeta donde se guardarán las imágenes
    if(move_uploaded_file($file, $destination)) {
        // Archivo cargado correctamente
        $res = array(
            "result" => "Archivo $name subido con éxito"
        );
        // Llamar al script Python para la predicción
        $output = exec("python/image_processing.py $destination 2>&1", $output_array, $return_code);
        if ($return_code === 0) {
            // Proceso de Python finalizado correctamente
            $res["prediction"] = $output;
        } else {
            // Error en el proceso de Python
            $res["error"] = "Error en el proceso de análisis de la imagen: $output";
        }
    } else {
        // Error al mover el archivo
        $res = array(
            "error" => "Error al subir el archivo: $name"
        );
    }
    header('Content-Type: application/json');
    echo json_encode($res);
}
?>
