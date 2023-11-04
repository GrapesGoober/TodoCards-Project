<script>
    
    let deckId = "1" // the input requires a deckid
    let cardslist = [] // output of the fetch goes into this list
    async function getCardslist(){
        let response = await fetch("http://127.0.0.1:5000/get-cards-list?deckId=" + deckId, {
            method:"GET",
            credentials: "include"
        })

        // recieve the cards
        cardslist = await response.json()
    }

</script>


cardslist = {JSON.stringify(cardslist)} <br>
deckname = <input type="text" bind:value={deckId}>
<input type="button" value="get cards list!" on:click={getCardslist}>