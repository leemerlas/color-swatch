// import logo from './logo.svg';
import React, { useState, useLayoutEffect} from 'react';

import './App.css';


function App() {

  const [swatchList, setSwatchList] = useState([]);

  const getSwatches = () => {
    fetch(`http://127.0.0.1:8000/swatch-api/swatches`, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
      }
    })
    .then(res => res.json())
    .then(data => {
      setSwatchList(data.swatches)
    })
    .catch(err => console.error(err));
  }

  useLayoutEffect(() => { 
    getSwatches();
  }, [])

  return (
    <div className="app" align='center'>
      <h2>Colors Swatch Challenge</h2>
      { swatchList && swatchList.map((swatch, i) => {
        // <div key={i}>{swatch.swatch_type}</div>

        return swatch.swatch_type === 'rgb' ? 
          <div key={i} style={{ width: 50, height: 50, borderRadius: 25, backgroundColor: `rgb(${swatch.red}, ${swatch.green}, ${swatch.blue})`, marginTop: 10 }}>
            <span style={{ paddingTop: 30 }}>RGB</span>
          </div>
        :
          <div key={i} style={{ width: 50, height: 50, borderRadius: 25, backgroundColor: `hsl(${swatch.hue}, ${swatch.saturation}, ${swatch.lightness})`, marginTop: 10 }}>
            <span style={{ paddingTop: 30 }}>HSL</span>
          </div>
          
        }) 
      }

      <button style={{ width: 120, height: 50, marginTop: 20 }} onClick={getSwatches}>New Swatch</button>
    </div>
  );
}

export default App;
