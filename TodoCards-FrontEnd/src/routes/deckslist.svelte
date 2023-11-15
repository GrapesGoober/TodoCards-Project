<script>
    import * as APIs from "$lib"
	import { onMount } from 'svelte'
    import Deck from "./deck.svelte";
    
    // Send request to backend to query the cards for us
    let deckslist = []
    async function getCardslist(){
        deckslist = await APIs.getDeckslist()
    }
    onMount(getCardslist)

</script>

<div>
    {#each deckslist as deck}
        <Deck bind:deckinfo={deck}></Deck>
    {/each}
</div>
