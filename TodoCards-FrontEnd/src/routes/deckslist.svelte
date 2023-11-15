<script>
    import * as APIs from "$lib"
	import { onMount } from 'svelte'
    import Deck from "./deck.svelte";
    
    // Send request to backend to query the cards for us
    let deckslist = []
    export async function getDeckslist(){
        deckslist = await APIs.getDeckslist()
    }
    onMount(getDeckslist)

</script>

<div>
    {#each deckslist as deck}
        <Deck bind:deckinfo={deck}></Deck>
    {/each}
</div>
