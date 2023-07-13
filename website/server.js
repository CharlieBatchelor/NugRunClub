const express = require("express");
const path = require("path");

const app = express();

app.use("/static", express.static(path.resolve(__dirname, "frontend", "static")));
app.use("/images", express.static(path.resolve(__dirname, "frontend", "images")));

app.get("/*", (req, res) => {
    res.sendFile(path.resolve("frontend", "index.html"));
});

const port = process.env.PORT || 8080;
const host = '0.0.0.0'; // Listen on all available network interfaces

app.listen(port, host, () => {
    console.log(`Server running on http://${host}:${port}`);
});