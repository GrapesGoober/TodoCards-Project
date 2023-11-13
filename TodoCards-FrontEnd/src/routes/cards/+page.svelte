<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";
	import Card from './card.svelte'

    // Send request to backend to query the cards for us
    let cardslist = []
    let deckinfo
    async function getCardslist(){
        // get the cardslist
        let searchParams = new URLSearchParams(window.location.search)
        let deckId = searchParams.get("deckId")
        cardslist = await APIs.getCardslist(deckId)

        // also get the deck info to display as well
        let deckslist = await APIs.getDeckslist()
        deckinfo = deckslist.find(deck => deck.deckId == deckId)
    }
    onMount(getCardslist)
    
</script>


<!-- Font Awesome 5 Free -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

{#if deckinfo}
    <h1>{deckinfo.deckName}</h1>
    <p><b>Nearest Due Date</b> {deckinfo.nearestDue}</p>
    <p>{deckinfo.deckDescription}</p>
{/if}

<button on:click={getCardslist}>refresh</button>

<div>
    {#each cardslist as card}
        <Card bind:cardinfo={card} refresh={getCardslist}></Card>
    {/each}
</div>

<style>
    @import "../style.css";

</style>