import express from "express";

const app = express();
const PORT = 3000;

app.get('/',(req,res)=>{
    res.status(200).send("<h1> Welcome to the application </h1>");
});

app.listen(PORT, '0.0.0.0', ()=>{
    console.log(`server running on port ${PORT}...`)
});