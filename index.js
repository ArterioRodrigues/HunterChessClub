function handleNavClick(node){  
    

 
    nav_items = document.getElementsByClassName('nav-link');

    for(let i = 0; i < 3; i++)
        nav_items[i].classList.remove("active")

    node.classList.add("active");

    if(node.innerText == "Events" || node.innerText == "Contact"){    
        nav = document.getElementById('navbar')
        nav.classList.add("navbar-dark")
        nav.classList.add("bg-dark")  
    }
    else{
        nav = document.getElementById('navbar')
        nav.classList.remove("navbar-dark")
        nav.classList.remove("bg-dark")  

    }
}