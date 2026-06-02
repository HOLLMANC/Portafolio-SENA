document.addEventListener("DOMContentLoaded", function() {

    // Seleccionamos el formulario por su ID único
    const formulario = document.getElementById("formContacto");

    formulario.addEventListener("submit", function(evento) {
        // Detiene el comportamiento clásico de recargar toda la página
        evento.preventDefault();

        // Agrupamos todos los campos del formulario automáticamente para enviarlos
        const datosFormulario = new FormData(formulario);

        // Enviamos los datos asíncronamente hacia el archivo PHP
        fetch("guardar.php", {
            method: "POST",
            body: datosFormulario
        })
        .then(respuesta => respuesta.text()) // Leemos la respuesta que nos da el servidor
        .then(resultado => {
            // Si el archivo PHP respondió con la palabra 'exito'
            if (resultado.trim() === "exito") {
                alert("¡Mensaje guardado con éxito en la base de datos MySQL! Tu portafolio funciona Full Stack.");
                formulario.reset(); // Resetea las cajas de texto del formulario
            } else {
                alert("Hubo un percance en el servidor: " + resultado);
            }
        })
        .catch(error => {
            console.error("Error en la petición:", error);
            alert("No se pudo establecer comunicación con el servidor local.");
        });
    });
});