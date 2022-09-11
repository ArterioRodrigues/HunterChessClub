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

function handleEventClick(node, node_link){
    event_node = document.getElementById(node_link);
    let check = false;
    for(let i = 0; i < event_node.classList.length; i++)
    {
        if(event_node.classList[i] == 'show')
            check = true;
    }
    if(check)
        event_node.classList.remove('show')
       
    else
        event_node.classList.add('show')
}