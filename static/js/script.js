const canvas = document.getElementById("drawingCanvas");
const ctx = canvas.getContext("2d");

let drawing = false;
let currentColor = "red";

/* Start drawing */

canvas.addEventListener("mousedown", () => {
    drawing = true;
});

/* Stop drawing */

canvas.addEventListener("mouseup", () => {
    drawing = false;
    ctx.beginPath();
});

/* Draw */

canvas.addEventListener("mousemove", draw);

function draw(event) {

    if (!drawing) return;

    ctx.lineWidth = 5;
    ctx.lineCap = "round";
    ctx.strokeStyle = currentColor;

    ctx.lineTo(event.offsetX, event.offsetY);
    ctx.stroke();
    ctx.beginPath();
    ctx.moveTo(event.offsetX, event.offsetY);
}

/* Clear Canvas */

function clearCanvas() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

/* Change Color */

function changeColor(color) {
    currentColor = color;
}

/* Save Drawing */

function saveDrawing() {

    const dataURL = canvas.toDataURL("image/png");

    const link = document.createElement("a");
    link.href = dataURL;
    link.download = "drawing.png";
    link.click();
}