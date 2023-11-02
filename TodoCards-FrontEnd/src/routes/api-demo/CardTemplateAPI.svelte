<script>
    
    let deckname = "quickdeck" // the input requires a deckname
    let cardslist = [] // output of the fetch goes into this list
    async function getCardslist(){
        let response = await fetch("http://127.0.0.1:5000/get-cards-list?deckname=" + deckname, {
            method:"GET"
        })

        // recieve the cards
        cardslist = await response.json()
    }

</script>


cardslist = {JSON.stringify(cardslist)} <br>
deckname = <input type="text" bind:value={deckname}>
<input type="button" value="get cards list!" on:click={getCardslist}>