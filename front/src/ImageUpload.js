import React, { useState } from "react";
import axios from "axios";
import { Navbar, Nav } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.min.css';
import { css } from "@emotion/react";
import { PacmanLoader } from "react-spinners";
import './ImageUpload.css';
import unnamed from './unnamed.png'; // Import the image here

function ImageUpload() {
  const [file, setFile] = useState(null);
  const [name, setName] = useState("");
  const [imageUrls, setImageUrls] = useState([]);
  const [isLoading, setIsLoading] = useState(false); // Add isLoading state

  const handleFileUpload = (event) => {
    setFile(event.target.files[0]);
  };

  const handleNameChange = (event) => {
    setName(event.target.value);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    const formData = new FormData();
    formData.append("image", file);
    const config = {
      headers: {
        "content-type": "multipart/form-data",
      },
    };

    setIsLoading(true); // Set isLoading to true

    try {
      const response = await axios.post("http://192.168.1.41:8000/menus/", formData, config);
      if (response.data.lista_of_urls_perdish) {
        console.log(response.data.lista_of_urls_perdish)
        setImageUrls(response.data.lista_of_urls_perdish);
      }
    } catch (error) {
      console.error(error);
    }

    setIsLoading(false); // Set isLoading to false
  };

  const renderImages = () => {
    return imageUrls.map((urls, index) => {
      return urls.map((url, subIndex) => {
        return (
          <div key={`${index}-${subIndex}`}>
            <div className="container text-center" >
              <img src={url} alt={`Image ${index}-${subIndex}`} />
            </div>
          </div>
        );
      });
    });
  };

  const override = css`
    display: block;
    margin: 0 auto;
    border-color: red;
  `;

  return (
    <div className="container text-center" style={{ maxWidth: "600px", backgroundColor: "grey" }}>
      <img src={unnamed} style={{ maxWidth: "50%" }}></img>
      <div>
        <form onSubmit={handleSubmit} style={{ margin: "10px", backgroundColor: "purple" }}>
          <div className="form-group" style={{ margin: "10px" }}>
            <input type="file" onChange={handleFileUpload} className="form-control" />
          </div>
          <button type="submit" className="btn btn-primary" style={{ margin: "10px" }}>Submit</button>
        </form>
        <div className="loader-container">
          {isLoading ? (
            <div className="d-flex justify-content-center align-items-center">
              <PacmanLoader color="purple" size={50} />
            </div>
          ) : (
            <div style={{ backgroundColor: "yellow" }}>{renderImages()}</div>
          )}
        </div>
      </div>
    </div>
  );
}

export default ImageUpload;
