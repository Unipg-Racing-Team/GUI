import React, { useState, useEffect } from "react";
import ReactDOM from 'react-dom';
import reportWebVitals from './reportWebVitals';
import Battery from "./components/battery";
import Temp from "./components/temp";
import Dial from "./components/dial";
import AccelDial from "./components/accelDial";
import Speedometer from "./components/speedometer";
import Barometer from "./components/barometer";
import Time from "./components/time";
import "./index.css";

// Sample incoming data
const incoming = {
  date: 1597107474849,
  data: {
    pitch: "0",
    roll: "0",
    yaw: "0",
    vgx: "0",
    vgy: "0",
    vgz: "-8",
    templ: "66",
    temph: "69",
    tof: "30",
    h: "20",
    bat: "90",
    baro: "172.62",
    time: "0",
    agx: "-12.00",
    agy: "-8.00",
    agz: "-980.00",
    location: "32.942690,-96.994845"
  },
  type: "toy",
  drone_id: "drone1"
};

const App = function () {
  // State variables
  const [date, setDate] = useState(new Date());
  const [battery, setBattery] = useState(incoming.data.bat);
  const [baro, setBaro] = useState(incoming.data.baro);
  const [pitch, setPitch] = useState(incoming.data.pitch);
  const [roll, setRoll] = useState(incoming.data.roll);
  const [yaw, setYaw] = useState(incoming.data.yaw);
  const [vgx, setVgx] = useState(incoming.data.vgx);
  const [vgy, setVgy] = useState(incoming.data.vgy);
  const [vgz, setVgz] = useState(incoming.data.vgz);
  const [agx, setAgx] = useState(incoming.data.vgx);
  const [agy, setAgy] = useState(incoming.data.vgy);
  const [agz, setAgz] = useState(incoming.data.vgz);
  const [templ, setTempl] = useState(incoming.data.templ);
  const [temph, setTemph] = useState(incoming.data.temph);
  const [location, setLocation] = useState(incoming.data.location);

  // useEffect(() => {
  //   // Timer to update the date every second
  //   const timerID = setInterval(() => tick(), 1000);

  //   return () => {
  //     clearInterval(timerID);
  //   };
  // }, []);

  const tick = () => {
    setDate(new Date());
  };

  return (
    <div className="App">
      <div className="dials">
        
        {/* Input for barometer */}
        barometer:
        <input
          type="text"
          value={baro}
          onChange={(e) => setBaro(e.target.value)}
        />
        
        {/* Input for lowest temperature */}
        lowestTemp:
        <input
          type="text"
          value={templ}
          onChange={(e) => setTempl(e.target.value)}
        />
        
        {/* Input for highest temperature */}
        highestTemp:
        <input
          type="text"
          value={temph}
          onChange={(e) => setTemph(e.target.value)}
        />
        
        {/* Input for speedX */}
        speedX:
        <input
          type="text"
          value={vgx}
          onChange={(e) => setVgx(e.target.value)}
        />
        
        {/* Input for speedY */}
        speedY:
        <input
          type="text"
          value={vgy}
          onChange={(e) => setVgy(e.target.value)}
        />
        
        {/* Input for accelerationX */}
        accelerationX:
        <input
          type="text"
          value={agx}
          onChange={(e) => setAgx(e.target.value)}
        />
        
        {/* Input for accelerationY */}
        accelerationY:
        <input
          type="text"
          value={agy}
          onChange={(e) => setAgy(e.target.value)}
        />
      </div>
     
      <div className="title">Pilot Battery Energy </div>
      {/* Battery component */}
      <Battery percentage={battery} />
      <p>Move slider to see battery level change</p>
      <div className="slidecontainer">
        
        {/* Slider for battery level */}
        <input
          type="range"
          min="1"
          max="100"
          step="1"
          className="slider"
          id="myRange"
          value={battery}
          onChange={(e) => setBattery(e.target.value)}
        />
      </div>
      
      <div className="dials">
        {/* Time component */}
        <Time id="dial10" value="10" title="Total Flight Time" />
      </div>
      
      <div className="dials">
        {/* Barometer component */}
        <Barometer id="dial9" value={baro} title="Barometer" />
      
        {/* Temperature components */}
        <Temp id="dial7" value={templ} title="Lowest Temp" />
        <Temp id="dial8" value={temph} title="Highest Temp" />
      </div>
      
      <div className="dials">
        {/* Speedometer components */}
        <Speedometer id="dial5" value={agx} title="Acceleration X" />
        <Speedometer id="dial6" value={agy} title="Acceleration Y" />
      </div>
      
      <div className="dials">
        {/* Dial and AccelDial components */}
        <Dial id="dial1" value={vgx} title="Speed X" />
        <Dial id="dial2" value={vgy} title="Speed Y" />
        <AccelDial id="dial3" value={agx} title="Acceleration X" />
        <AccelDial id="dial4" value={agy} title="Acceleration Y" />
      </div>
      
      <div className="dials">
        {/* Display pitch, yaw, and roll */}
        <div>
          Pitch: {pitch} | Yaw: {yaw} | Roll: {roll}
        </div>
      </div>
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("app"));

reportWebVitals();
