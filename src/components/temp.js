import Thermometer from "react-thermometer-component";

const styles = {
  dial: {
    // Styling for the dial component
    display: "inline-block",
    width: `300px`,
    height: `auto`,
    color: "#000",
    border: "0.5px solid #fff",
    padding: "2px"
  },
  title: {
    // Styling for the title component
    fontSize: "1em",
    color: "#000",
    marginTop: "15px"
  }
};

// Temp component
const Temp = ({ id, value, title }) => {
  return (
    <div style={styles.dial}>
      {/* Thermometer component */}
      <Thermometer
        theme="light"
        value={value}
        max="100"
        steps="1"
        format="°C"
        size="normal"
        height="180"
      />
      {/* Title and value */}
      <div style={styles.title}>
        {title}: {value}°C
      </div>
    </div>
  );
};

export default Temp;