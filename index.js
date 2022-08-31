function handleNavOver(node){
    node.parentNode.style.animation = "wiggle 3s linear infinite";
    if(node.innerText == "E1"){
        node.innerText = "Home"
    }    
    if(node.innerText == "D1"){
        node.innerText = "Events"
    }
    if(node.innerText == "F1"){
        node.innerText = "Contact"
    }
    
    console.log(node.attributes)
    console.log(node.nodeValue)
}

function handleNavOut(node){
    node.parentNode.style.animation = "";
    if(node.innerText == "Home"){
        node.innerText = "E1"
    }    
    if(node.innerText == "Events"){
        node.innerText = "D1"
    }
    if(node.innerText == "Contact"){
        node.innerText = "F1"
    }
    
    console.log(node.attributes)
    console.log(node.nodeValue)
}

function handleNavClick(node){
    
    
}