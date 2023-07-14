var attemt = 3;
function validate(){
    var nombreU = document.getElementById("nombre").value;
    var contra = document.getElementById("password").value;
    if(nombreU == "maldo" && contra == 1234){
        alert("Ingreso exitoso");
        window.location="../index.html"
        return false;

    }if(nombreU == "nanoR" && contra == 12345){
        alert("Ingreso exitoso");
        window.location="../index.html"
        return false;
    } 
    
    else{
        attemt --;
    }
    alert("Te quedan " + attemt + " intentos")
    if(attemt == 0){
        document.getElementById("nombreU").disable=true;
        document.getElementById("contra").disable=true;
        document.getElementById("submit").disable=true;
    }
} 

function openNav(){
    document.getElementById("mobile-menu").style.width = "100%";
}

function closeNav(){
    document.getElementById("mobile-menu").style.width = "0%";
}