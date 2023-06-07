import { useState } from "react";
import ReactDOM from 'react-dom';
import reportWebVitals from './reportWebVitals';
import Battery from "./components/battery";
import Temp from "./components/temp";
import Dial from "./components/dial";
import AccelDial from "./components/accelDial";
import Speedometer from "./components/speedometer";
import Barometer from "./components/barometer";
import Time from "./components/time";
import useInitializeState from "./utils/updateInterface";
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
  car: "car1",
  car_id: "test_car"
};

const App = function () {
  // Initialize state using custom data
  const state = useInitializeState(incoming);
  const {
    date,
    setDate,
    battery,
    setBattery,
    baro,
    setBaro,
    pitch,
    setPitch,
    roll,
    setRoll,
    yaw,
    setYaw,
    vgx,
    setVgx,
    vgy,
    setVgy,
    vgz,
    setVgz,
    agx,
    setAgx,
    agy,
    setAgy,
    agz,
    setAgz,
    templ,
    setTempl,
    temph,
    setTemph,
    location,
    setLocation,
  } = state;

  return (
    <div className="App">     
      <div className="title">Pilot Battery Energy </div>
      {/* Battery component */}
      <Battery percentage={battery} />
      
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
    </div>
  );
}

ReactDOM.render(<App />, document.getElementById("app"));

reportWebVitals();
