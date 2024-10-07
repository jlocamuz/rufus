import React, { useState } from "react";
import axios from "axios";
import unnamed from './unnamed.png';
import FileInput from "./FileInput";
import gifImage from './gato.gif';
import noSeleccionado from './no_seleccionado.png';
import flechaAtras from './botón de volver.png';
import comer from './comer.png';
import yo from './yo.png'

function ImageItem({ dish_name, imageUrl, isSelected, onClick }) {
  const imageStyle = {
    width: '200px',
    height: '200px',
    padding: '20px',
  };

  return (
    <div className="container text-center">
      <button
        style={{ background: "transparent", border: "none" }}
        onClick={onClick}
      >
        <div className="image-container" style={isSelected ? { border: '2px solid black' } : {}}>
          <img
            src={imageUrl}
            alt={`Image`}
            style={imageStyle}
          />
        </div>
        <div style={{ textAlign: "right" }}>
          <span>{dish_name}</span>
        </div>
      </button>
    </div>
  );
}

function Rufus() {
  const [file, setFile] = useState(null);
  const [imageUrls, setImageUrls] = useState([]);
  const [isLoading, setIsLoading] = useState(false);
  const [showBackButton, setShowBackButton] = useState(false);
  const [hideCameraImage, setHideCameraImage] = useState(false);
  const [selectedImage, setSelectedImage] = useState(null);

  const resetFile = () => {
    setFile(null);
    setShowBackButton(false);
    setImageUrls([]);
    setHideCameraImage(false);
    setSelectedImage(null);
  };

  const handlePhotoCapture = (photo) => {
    resetFile();
    setFile(photo);
    setShowBackButton(true);
    setHideCameraImage(true);

    if (photo instanceof Blob) {
      const reader = new FileReader();

      reader.onload = () => {
        setIsLoading(true);

        const formData = new FormData();
        formData.append("image", photo);
        const config = {
          headers: {
            "content-type": "multipart/form-data",
          },
        };

        axios
          .post("http://0.0.0.0:8000/menus/", formData, config)
          .then((response) => {
            if (response.data.lista_of_urls_perdish) {
              console.log(response.data.lista_of_urls_perdish);
              setImageUrls(response.data.lista_of_urls_perdish);
            }
          })
          .catch((error) => {
            console.error(error);
          })
          .finally(() => {
            setIsLoading(false);
          });
      };

      reader.readAsDataURL(photo);
    } else {
      console.error("El parámetro 'photo' no es un objeto Blob válido");
    }
  };

  const handleImageSelect = (imageUrl) => {
    setSelectedImage(imageUrl);
  };

  const renderImages = () => {
    const imagesToRender = [...imageUrls];
    const maxColumns = 3;

    // Filtrar la imagen seleccionada
    const selectedImageItem = imagesToRender.find(
      (item) => item.fields.url === selectedImage
    );
    if (selectedImageItem) {
      // Eliminar la imagen seleccionada del arreglo
      imagesToRender.splice(imagesToRender.indexOf(selectedImageItem), 1);
    }

    const rows = [];
    let currentRow = [];

    imagesToRender.forEach((dish, index) => {
      currentRow.push(dish);
      if (currentRow.length === maxColumns || index === imagesToRender.length - 1) {
        // Si se alcanzó el máximo de columnas o es la última imagen, crear una nueva fila
        rows.push(currentRow);
        currentRow = [];
      }
    });

    // Agregar un rectángulo blanco con borde negro si no hay imagen seleccionada
    if (!selectedImage) {
      imagesToRender.push({
        fields: {
          url: noSeleccionado, // Ruta a la imagen en blanco con borde negro
        },
      });
    }

    return (
      <div>
        {/* Mostrar la imagen seleccionada arriba en una fila centrada */}
        {
        hideCameraImage && (
          <div style={{ display: 'flex', justifyContent: 'center', marginBottom: '100px' }}>
            <img src={yo} style={{ width: '200px', height: '200px' ,  border: '2px solid black'}}></img>
            <img src={comer}style={{ width: '200px', height: '200px'  ,border: '2px solid black'}}></img>
            <div className="image-container" style={{ width: '200px', height: '200px', border: '2px solid black' }}>
              <img
                src={selectedImage}
                alt="Selected"
                style={{ width: '200px', height: '200px' }}
              />
            </div>
          </div>
        )}

        {rows.map((row, rowIndex) => (
          <div key={rowIndex} style={{ display: 'flex', marginBottom: '100px' }}>
            {row.map((dish, index) => (
              <div key={index} style={{ flex: '1' }}>
                {dish.dish_items.map((dishItem, itemIndex) => (
                  <ImageItem
                    key={itemIndex}
                    dish_name={dishItem.fields.name}
                    imageUrl={dishItem.fields.url}
                    isSelected={dishItem.fields.url === selectedImage}
                    onClick={() => handleImageSelect(dishItem.fields.url)}
                  />
                ))}
              </div>
            ))}
          </div>
        ))}
      </div>
    );
  }

  return (
    <div className="container text-center mobile-background" style={{ maxWidth: "600px" }}>
      {showBackButton ? (
        <div className="circle-container" style={{ marginTop: "35px" }}>
          <button
            onClick={() => resetFile()}
            style={{ background: "transparent", border: "none" }}
          >
            <img
              src={flechaAtras}
              alt="Volver"
              style={{ width: "50px", height: "50px", marginTop: "50px" }}
            />
          </button>
          <div></div>
          <div></div>
        </div>
      ) : (
        <div className="circle-container" style={{ marginTop: "35px" }}>
          <img style={{ width: "350px" }} src={unnamed} className="circle-image" alt="Profile" />
        </div>
      )}
      <div>
        <FileInput onPhotoCapture={handlePhotoCapture} hideImage={hideCameraImage} />
        <div className="loader-container" style={{ marginTop: "60px" }}>
          {isLoading ? (
            <div className="d-flex justify-content-center align-items-center">
              <img src={gifImage} alt="Loading" className="loader-gif" />
            </div>
          ) : (
            <div>{renderImages()}</div>
          )}
        </div>
      </div>
    </div>
  );
}

export default Rufus;
