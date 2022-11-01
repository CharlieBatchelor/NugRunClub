const express = require("express");
const path = require("path");

const app = express();

app.use("/static", express.static(path.resolve(__dirname, "frontend", "static")));
app.use("/images", express.static(path.resolve(__dirname, "frontend", "images")));

app.get("/*", (req, res) => {
    res.sendFile(path.resolve("frontend", "index.html"));
});

app.listen(process.env.PORT || 8080, () => console.log("Server running..."));