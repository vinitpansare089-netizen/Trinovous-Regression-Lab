import { useState } from "react";
import axios from "axios";
import "./App.css";

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

      setResult(response.data.Prediction);
      console.log("FULL RESPONSE:", response);
console.log("DATA:", response.data);
    } catch (error) {
      alert("Error connecting to backend");
    }
    
  };

  return (
    <div className="container">
      <div className="card">
        <h2>🎓 Student Grade Predictor</h2>

        <input
          name="studytime"
          placeholder="Study Time"
          onChange={handleChange}
        />

        <input
          name="failures"
          placeholder="Failures"
          onChange={handleChange}
        />

        <input
          name="absences"
          placeholder="Absences"
          onChange={handleChange}
        />

        <button onClick={handleSubmit}>Predict</button>

        <div className="result">
  {result !== null ? `Predicted Score: ${result}` : "Enter values and click Predict"}
</div>
      </div>
    </div>
  );
}

export default App;