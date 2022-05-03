



async function wikiFetch(){
    let search_term = getSearchText()

    let url_for_api_call = buildURI(search_term)

    // get fetch data from link -> url_for_api_call
    let answer = await fetch(url_for_api_call)

    //
    let myJson = await answer.json()
    // define array index
    let i = 1
    // create a div
    const node = document.createElement("div");
    // create text from json
    const textnode = document.createTextNode(myJson.query.search[i].title);

    const body = document.querySelector("body");
    const section = document.getElementById("section_for_result");
    // debugger

    // append text to the created div
    node.appendChild(textnode);
    // append  the div to the body
    body.appendChild(node);
    section.appendChild(node);
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