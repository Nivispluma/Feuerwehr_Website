//-----------------------------
function increment(){
    let counter = 0;
    return function() {counter += 1; return counter;}
}

let add = increment();

function myFunction(){
    document.getElementById("demo").innerHTML = add()
}

//--------------------------------------------------------

function createMenuItem(menu_item) {
    let li = document.createElement('li');
    //li.textContent = menu_item;
    li.innerHTML = menu_item;
    return li;
}
// get the ul#menu
const menu = document.querySelector('#menu');
// add menu item

menu.appendChild(createMenuItem('<a href="">Dienste</a>'));

