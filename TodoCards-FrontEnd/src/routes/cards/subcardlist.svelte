<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";
    import Subcard from "./subcard.svelte";
    export let cardId, refresh
    let subcardslist = []
    async function getSubcardslist() {
        subcardslist = await APIs.getSubcardslist(cardId)
    }
    onMount(getSubcardslist)

</script>


{#each subcardslist as subcard}
    <Subcard bind:subcardinfo={subcard} refresh={refresh}></Subcard>
{/each}