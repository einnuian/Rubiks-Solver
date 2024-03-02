var color;
// Take color
function takeColor(btn) {
    var property = document.getElementById(btn);
    color = property.style.backgroundColor;
}
// Set color and value of the piece. Prep for cube_str
function setColor(btn) {
    var property = document.getElementById(btn);
    property.style.backgroundColor = color;
    if (color.localeCompare("blue") == 0){
        property.value = 'b';
    }
    else if (color.localeCompare("white") == 0){
        property.value = 'w';
    }
    else if (color.localeCompare("red") == 0){
        property.value = 'r';
    }
    else if (color.localeCompare("green") == 0){
        property.value = 'g';
    }
    else if (color.localeCompare("yellow") == 0){
        property.value = 'y';
    }
    else {
        property.value = 'o';
    }
}
// Generate cube_str when the Solve! button is clicked
// Send cube_str over to Python
function sendVar(){
    var cube_str = '';
    // Loop through each piece on the cube
    for (let i = 0; i < 54; i++){
        let id = i.toString();
        let piece = document.getElementById(id);
        cube_str = cube_str + piece.value; // Making cube_str
    }
    const s = JSON.stringify({'value':cube_str})
    $.ajax({
        url: '/process', //url to process() to process cube_str
        type: 'POST',
        data: {"value":cube_str}
    })
    // Notify user that the cube is submitted
    document.getElementById("cube").textContent = "Submitted!"
}

