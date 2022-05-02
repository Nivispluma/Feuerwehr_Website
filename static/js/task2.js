
async function wikiCall(){
    let answer = await fetch('http://localhost:5000/proxy?url=https://de.wikipedia.org/w/api.php?action=query%26list=search%26srsearch=HLF%26format=json')
    console.log(await answer.json())
}



