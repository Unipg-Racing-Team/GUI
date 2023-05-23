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

// Time component
const Time = ({ id, value, title }) => {
  return <div style={styles.dial}></div>;
};

export default Time;