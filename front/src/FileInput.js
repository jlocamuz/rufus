import React, { useRef, useState } from "react";
import camara from './cámara.png'; // Importa la imagen aquí

function FileInput({ onPhotoCapture, hideImage }) { // Agrega un prop hideImage
  const inputRef = useRef(null);

  const handleCapture = () => {
    inputRef.current.click();
  };

  const handleInputChange = (event) => {
    const file = event.target.files[0];
    onPhotoCapture(file);
  };

  return (
    <div className="camera-icon" onClick={handleCapture}>
      {hideImage ? null : ( // Verifica el estado hideImage antes de renderizar la imagen
        <img
          src={camara} // Reemplaza "ruta/a/tu/imagen.png" con la ruta de tu imagen
          alt="Capture"
          style={{ marginTop: "60px", width: "100px", height: "100px" }}
        />
      )}
      <input
        ref={inputRef}
        type="file"
        accept="image/*"
        capture="environment"
        onChange={handleInputChange}
        style={{ display: "none" }}
      />
    </div>
  );
}

export default FileInput;
