



async function wikiFetch(){

    clearBox("section_for_result")
    let search_term = getSearchText()

    let url_for_api_call = buildURI(search_term)

    // get fetch data from link -> url_for_api_call
    let answer = await fetch(url_for_api_call)

    //
    let myJson = await answer.json()
    // define array index

    // create a div
    const rootelement = document.createElement("div");
    // create text from json

    rootelement.classList.add("search_result_grid_wrapper")



    let textnode
    for(let i = 0; i < myJson.query.search.length;i++){
        let row_element = document.createElement("a")
        let node_text = myJson.query.search[i].title
        textnode = document.createTextNode(node_text);
        row_element.appendChild(textnode)
        rootelement.appendChild(row_element);


        let wikipedia_basic_link = "https://de.wikipedia.org/wiki/"
        let wikipedia_link =  wikipedia_basic_link+node_text

        row_element.classList.add("search_result_grid_child")
        row_element.setAttribute('href',wikipedia_link)
    }


    const body = document.querySelector("body");
    const section = document.getElementById("section_for_result");
    // debugger

    // append text to the created div

    // append  the div to the body
    section.appendChild(rootelement);
}

function getSearchText(){
    return document.getElementById("searchBar").value;
}

function buildURI(search_term){
    let host = window.location.host
    const proxy_path = "/proxy?"
    const wikipedia_link_first = "url=https://de.wikipedia.org/w/api.php?action=query%26list=search%26srsearch="
    const wikipedia_link_second = "%26format=json"
    // http required due to Werkzeug only supporting http
    let uri = "http://"+host+proxy_path+wikipedia_link_first+search_term+wikipedia_link_second
    return uri
}

function clearBox(elementID)
{
    document.getElementById(elementID).innerHTML = "";
}