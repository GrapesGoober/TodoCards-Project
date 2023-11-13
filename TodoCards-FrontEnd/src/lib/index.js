// place files you want to import through the `$lib` alias in this folder.
const ENDPOINT = "http://127.0.0.1:5000"

// route to the login page upon unsuccessful login
const LOGIN_HREF = "/login"

async function sendGetRequest(route, params) {

    let queryString = Object.keys(params)
        .map(key => `${encodeURIComponent(key)}=${encodeURIComponent(params[key])}`)
        .join('&');
        
    let response = await fetch(`${ENDPOINT}${route}?${queryString}`, {
        method: "GET",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        }
    })

    return await response.json()
}

async function sendPostRequest(route, body) {
    let response = await fetch(ENDPOINT + route, {
        method: "POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(body)
    })

    return await response.json()
}

async function sendAuthPostRequest(route, body) {
    let result = await sendPostRequest(route, body)
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}

async function sendAuthGetRequest(route, body) {
    let result = await sendGetRequest(route, body)
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}


let ping_count = 0
export async function ping() {

    let result = await sendGetRequest("/ping", {})
    if (result.message === "pong"){
        ping_count ++
    }

    return ping_count
}

export async function login(username, password){
    return await sendPostRequest("/login", {username, password})
}

export async function signup(username, password){
    return await sendPostRequest("/signup", {username, password})
}

export async function logout() {
    await sendPostRequest("/logout", {})
    return false
}

export async function getDeckslist(){
    return await sendAuthGetRequest("/get-decks-list", {})
}

export async function getCardslist(deckId){
    return await sendAuthGetRequest("/get-cards-list", {deckId})
}

export async function getSubcardslist(cardId){
    return await sendAuthGetRequest("/get-subcards-list", {cardId})
}

export async function editCard(cardInfo){
    return await sendAuthPostRequest("/edit-card", {cardInfo})
}

export async function editSubcard(subcardInfo){
    return await sendAuthPostRequest("/edit-subcard", {subcardInfo})
}

export async function editDeck(deckInfo){
    return await sendAuthPostRequest("/edit-deck", {deckInfo})
}

export async function createCard(cardInfo){
    return await sendAuthPostRequest("/create-card", {cardInfo})
}

export async function createSubcard(subcardInfo){
    return await sendAuthPostRequest("/create-subcard", {subcardInfo})
}

export async function createDeck(deckInfo){
    return await sendAuthPostRequest("/create-deck", {deckInfo})
}

export async function deleteCard(cardId){
    return await sendAuthPostRequest("/delete-card", {cardId})
}

export async function deleteSubcard(subcardId){
    return await sendAuthPostRequest("/delete-subcard", {subcardId})
}

export async function deleteDeck(deckId){
    return await sendAuthPostRequest("/delete-deck", {deckId})
}

export async function finishCard(cardId){
    return await sendAuthPostRequest("/finish-card", {cardId})
}
export async function finishSubcard(subcardId){
    return await sendAuthPostRequest("/finish-card", {subcardId})
}

export async function getSharecode(deckId){
    return await sendAuthGetRequest("/get-sharecode", {deckId})
}

export async function recieveSharecode(sharecode){
    return await sendAuthGetRequest("/recieve-sharecode", {sharecode})
}