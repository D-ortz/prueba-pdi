$(document).ready(function() {
    $('#analyzeButton').on('click', function() {
        var fileInput = document.getElementById('inputImage');
        var file = fileInput.files[0];
        var formData = new FormData();
        formData.append('file', file);

        fetch('http://127.0.0.1:5000/analyze', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.result !== null) {
                $('#result').text(data.result);
            } else {
                console.error('Respuesta inesperada:', data);
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    });
});
