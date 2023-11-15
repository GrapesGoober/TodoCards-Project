<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";
    import Subcard from "./subcard.svelte";
    export let cardId, refresh, editable
    let subcardslist = []
    async function getSubcardslist() {
        await refresh()
        subcardslist = await APIs.getSubcardslist(cardId)
    }
    onMount(getSubcardslist)

</script>


{#each subcardslist as subcard}
    <Subcard bind:subcardinfo={subcard} bind:editable={editable} refresh={getSubcardslist}></Subcard>
{/each}