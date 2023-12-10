const redInput = document.getElementById('redColor');
const greenInput = document.getElementById('greenColor');
const blueInput = document.getElementById('blueColor');
const boxColor = document.getElementById('boxColor');

redInput.addEventListener('change', changeColor);
greenInput.addEventListener('change', changeColor);
blueInput.addEventListener('change', changeColor);

function changeColor() {
    const redValue = redInput.value;
    const greenValue = greenInput.value;
    const blueValue = blueInput.value;
    console.log(redValue)
    console.log(greenValue)
    console.log(blueValue)

    const color = `rgb(${redValue}, ${greenValue}, ${blueValue})`;

    boxColor.style.backgroundColor = color;
}
