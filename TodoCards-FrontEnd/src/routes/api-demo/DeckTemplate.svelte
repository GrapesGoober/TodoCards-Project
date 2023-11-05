<script>
    
    let deckslist = [] // output of the fetch goes into this list
    async function getDeckslist(){
        let response = await fetch("http://127.0.0.1:5000/get-decks-list?", {
            method:"GET",
            credentials: "include"
        })

        // recieve the cards
        deckslist = await response.json()
    }

</script>


deckslist = {JSON.stringify(deckslist)} <br>
<input type="button" value="get decks list!" on:click={getDeckslist}>