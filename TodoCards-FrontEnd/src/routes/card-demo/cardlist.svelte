<script>
	import { onMount } from 'svelte';
	import Card from './card.svelte'

    // Each card-list is only limited to one deck at a time
	export let deckname = "QuickDeck"

    // Send request to backend to query the cards for us
    let cardslist = []
    async function getCardslist(){
        let response = await fetch("http://127.0.0.1:5000/get-cards-list", {
            method:"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                deckname
            })
        })

        // recieve the cards
        cardslist = await response.json()
        console.log(cardslist)
    }
    onMount(getCardslist) 

</script>

<div>
    {#each cardslist as card, i}
    <Card bind:info={card}></Card>
    {/each}
</div>

