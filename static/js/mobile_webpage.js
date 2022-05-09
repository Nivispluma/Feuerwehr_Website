



function changeMenuToMobile(){
    document.getElementById("text_nav_bar").classList.add("hidden_element")
    document.getElementById("picture_nav_bar").classList.add("hidden_element")
    document.getElementById("icon_nav_bar").classList.remove("hidden_element")
    return
}

function changeMenuToDesktop(){
    document.getElementById("text_nav_bar").classList.remove("hidden_element")
    document.getElementById("picture_nav_bar").classList.remove("hidden_element")
    document.getElementById("icon_nav_bar").classList.add("hidden_element")
    return
}

function checkWindowSize(){
    if (window.innerWidth < 701){
        changeMenuToMobile()
    }
    else {
        changeMenuToDesktop()
    }
}