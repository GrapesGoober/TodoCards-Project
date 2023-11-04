<script>

    let status = false
    let cardInfo = {
        cardId:             1,
        cardName:           "Write introduction",
        cardDescription:    "200 words zuzu",
        cardDue:            "Tue, 17 Oct 2023 00:00:00 GMT",
        cardColor:          "lightblue",
        cardIsFinished:     0,
    }
    async function editCard(){
        let response = await fetch("http://127.0.0.1:5000/edit-card", {
            method:"POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({cardInfo})
        })

        // recieve the result
        status = await response.json()
    }

</script>

status = {status} <br>
<input type="text" placeholder="cardId" bind:value={cardInfo.cardId}> <br>
<input type="text" placeholder="cardName" bind:value={cardInfo.cardName}> <br>
<input type="text" placeholder="cardDescription" bind:value={cardInfo.cardDescription}> <br>
<input type="text" placeholder="cardDue" bind:value={cardInfo.cardDue}> <br>
<input type="text" placeholder="cardColor" bind:value={cardInfo.cardColor}> <br>
<input type="text" placeholder="cardIsFinished" bind:value={cardInfo.cardIsFinished}> <br>
<input type="button" value="submit" on:click={editCard}>