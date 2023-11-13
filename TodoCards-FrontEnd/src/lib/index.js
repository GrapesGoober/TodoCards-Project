// place files you want to import through the `$lib` alias in this folder.
const ENDPOINT = "http://127.0.0.1:5000"

// route to the login page upon unsuccessful login
const LOGIN_HREF = "/login"

let ping_count = 0
export async function ping() {
    let res = await fetch(ENDPOINT + "/ping", {
        method: "GET",
        credentials: 'include',
        headers: {
            "Content-Type": "application/json"
        },
    })
    
    let result = await res.json()
    if (result.message === "pong"){
        ping_count ++
    }

    return ping_count
}

export async function login(username, password){
    let response = await fetch(ENDPOINT + "/login", {
        method:"POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username,
            password
        })
    })

    // recieve the result
    return await response.json()
}

export async function signup(username, password){
    let response = await fetch(ENDPOINT + "/signup", {
        method:"POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            username,
            password
        })
    })

    // recieve the result
    return await response.json()
}

export async function logout() {
    await fetch(ENDPOINT + "/logout", {
        method:"POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        }
    })

    return false
}

export async function getDeckslist(){
    let response = await fetch(ENDPOINT + "/get-decks-list?", {
        method:"GET",
        credentials: "include"
    })

    // recieve the decks
    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}

export async function getCardslist(deckId){
    let response = await fetch(ENDPOINT + "/get-cards-list?deckId=" + deckId, {
        method:"GET",
        credentials: "include"
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}

export async function getSubcardslist(cardId){
    let response = await fetch(ENDPOINT + "/get-subcards-list?cardId=" + cardId, {
        method:"GET",
        credentials: "include"
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}

export async function editCard(cardInfo){
    let response = await fetch(ENDPOINT + "/edit-card", {
        method:"POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({cardInfo})
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}

export async function editSubcard(subcardInfo){
    let response = await fetch(ENDPOINT + "/edit-subcard", {
        method:"POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({subcardInfo})
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}

export async function editDeck(deckInfo){
    let response = await fetch(ENDPOINT + "/edit-deck", {
        method:"POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({deckInfo})
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}


export async function finishCard(cardId){
    let response = await fetch(ENDPOINT + "/finish-card", {
        method:"POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({cardId})
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}
export async function finishSubcard(subcardId){
    let response = await fetch(ENDPOINT + "/finish-subcard", {
        method:"POST",
        credentials: "include",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({subcardId})
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}

export async function getSharecode(deckId){
    let response = await fetch(ENDPOINT + "/get-sharecode?deckId=" + deckId, {
        method:"GET",
        credentials: "include"
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}

export async function recieveSharecode(sharecode){
    let response = await fetch(ENDPOINT + "/recieve-sharecode?sharecode=" + sharecode, {
        method:"GET",
        credentials: "include"
    })

    let result = await response.json()
    if (result === false) {
        window.location.href = LOGIN_HREF
    }
    return result
}