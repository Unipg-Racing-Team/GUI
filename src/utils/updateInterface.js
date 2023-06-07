import { useState } from 'react';

// Custom data to initialize the application state
function useInitializeState(incoming) {
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

  // Return the states and set functions as an object
  return {
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
  };
}

export default useInitializeState;