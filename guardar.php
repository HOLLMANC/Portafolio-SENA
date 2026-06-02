<?php
// 1. Configuración de los datos de conexión a la base de datos
$servidor = "localhost";
$usuario  = "root";
$password = ""; // Por defecto en XAMPP viene vacía
$base_datos = "proyecto_sena";

// Especificamos el puerto 3307 que es el que se activó con éxito en tu XAMPP
$puerto = "3307";

// 2. Establecer la conexión con el servidor MySQL
$conexion = mysqli_connect($servidor, $usuario, $password, $base_datos, $puerto);

// Verificamos si la conexión falló
if (!$conexion) {
    die("Error al conectarse con la base de datos: " . mysqli_connect_error());
}

// 3. Capturar los datos enviados desde el formulario HTML
if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Protegemos la base de datos de caracteres extraños
    $nombre  = mysqli_real_escape_string($conexion, $_POST['nombre']);
    $correo  = mysqli_real_escape_string($conexion, $_POST['correo']);
    $mensaje = mysqli_real_escape_string($conexion, $_POST['mensaje']);

    // Validamos que el servidor no reciba campos vacíos
    if (empty($nombre) || empty($correo) || empty($mensaje)) {
        echo "Error: Todos los campos son obligatorios.";
        exit;
    }

    // 4. Escribir la orden SQL para insertar los datos en la tabla 'contactos'
    $sql = "INSERT INTO contactos (nombre, correo, mensaje) VALUES ('$nombre', '$correo', '$mensaje')";

    // Ejecutamos la orden y comprobamos si fue exitosa
    if (mysqli_query($conexion, $sql)) {
        // Respondemos únicamente con la palabra 'exito' para que script.js lo procese
        echo "exito";
    } else {
        echo "Error al guardar los datos: " . mysqli_error($conexion);
    }
}

// 5. Cerrar la conexión
mysqli_close($conexion);
?>