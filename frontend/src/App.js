import { useState } from "react";
import axios from "axios";

function App() {
  const [form, setForm] = useState({
    studytime: "",
    failures: "",
    absences: ""
  });

  const [result, setResult] = useState(null);

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://localhost:5000/predict", {
        ...form,
        school: "GP",
        sex: "M"
      });

      setResult(response.data.prediction);
    } catch (error) {
      console.error(error);
      alert("Error connecting to backend");
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h2>🎓 Student Grade Predictor</h2>

      <input name="studytime" placeholder="Study Time" onChange={handleChange} />
      <br /><br />

      <input name="failures" placeholder="Failures" onChange={handleChange} />
      <br /><br />

      <input name="absences" placeholder="Absences" onChange={handleChange} />
      <br /><br />

      <button onClick={handleSubmit}>Predict</button>

      {result && <h3>Predicted G3: {result}</h3>}
    </div>
  );
}

export default App;