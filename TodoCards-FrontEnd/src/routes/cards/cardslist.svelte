<script>
    import * as APIs from "$lib"
	import { onMount } from 'svelte'
	import Card from './card.svelte'

    // Each card-list is only limited to one deck at a time
	export let deckId
    
    // Send request to backend to query the cards for us
    let cardslist = []
    async function getCardslist(){
        cardslist = await APIs.getCardslist(deckId)
    }
    onMount(getCardslist)

</script>

<p>The deckid of this cardslist = {deckId}</p>
<button on:click={getCardslist}>refresh</button>

<div>
    {#each cardslist as card}
        <Card bind:cardinfo={card} refresh={getCardslist}></Card>
    {/each}
</div>
