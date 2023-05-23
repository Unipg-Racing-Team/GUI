import ReactSpeedometer from "react-d3-speedometer";

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
    color: "#000"
  }
};

// Speedometer component
const Speedometer = ({ id, value, title }) => {
  return (
    <div style={styles.dial}>
      {/* ReactSpeedometer component */}
      <ReactSpeedometer
        maxValue={120}
        minValue={-100}
        height={190}
        width={290}
        value={value}
        needleTransition="easeQuadIn"
        needleTransitionDuration={1000}
        needleColor="red"
        startColor="green"
        segments={10}
        endColor="blue"
      />
      {/* Title */}
      <div style={styles.title}>{title}</div>
    </div>
  );
};

export default Speedometer;