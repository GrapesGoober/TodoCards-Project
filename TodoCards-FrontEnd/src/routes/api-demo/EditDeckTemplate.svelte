<script>

    let status = false
    let deckInfo = {
        deckId:             1,
        deckName:           "Write introduction",
        deckDescription:    "200 words zuzu"
    }
    async function editDeck(){
        let response = await fetch("http://127.0.0.1:5000/edit-deck", {
            method:"POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({deckInfo})
        })

        // recieve the result
        status = await response.json()
    }

</script>

status = {status} <br>
<input type="text" placeholder="deckId" bind:value={deckInfo.deckId}> <br>
<input type="text" placeholder="deckName" bind:value={deckInfo.deckName}> <br>
<input type="text" placeholder="deckDescription" bind:value={deckInfo.deckDescription}> <br>
<input type="button" value="submit" on:click={editDeck}>
