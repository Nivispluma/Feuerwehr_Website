//-----------------------------
function increment(){
    let counter = 0;
    return function() {counter += 1; return counter;}
}

let add = increment();

function myFunction(){
    document.getElementById("demo").innerHTML = add()
}

//----------------------

document.getElementsByTagName("BODY")[0].onload = Init;

function Init()
{

}

let elemDiv = document.createElement('div');
elemDiv.style.cssText = 'position:absolute;width:100%;height: 10px; opacity:0.3;z-index:100;background:#000;';
document.body.appendChild(elemDiv);

let myHeading = document.querySelector('h1');
myHeading.textContent = 'Hallo Welt!';

//--------------------------------------------------------

function createMenuItem(name) {
    let li = document.createElement('li');
    li.textContent = name;
    return li;
}
// get the ul#menu
const menu = document.querySelector('#menu');
// add menu item

menu.appendChild(createMenuItem('Dienste'));