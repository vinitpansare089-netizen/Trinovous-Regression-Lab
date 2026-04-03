const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();

app.use(cors());
app.use(express.json());

// test route
app.get("/", (req, res) => {
    res.send("Node working 🚀");
});

app.post("/predict", async (req, res) => {
    try {
        console.log("Incoming:", req.body);

        const response = await axios.post(
            "http://127.0.0.1:8000/predict",
            req.body
        );

        res.json(response.data);

    } catch (error) {
        console.error(error.message);
        res.status(500).json({ error: "ML API error" });
    }
});

app.listen(5000, () => {
    console.log("Backend running on port 5000");
});

// app.get("/", (req, res) => {
//     res.send("Node working 🚀");
// });