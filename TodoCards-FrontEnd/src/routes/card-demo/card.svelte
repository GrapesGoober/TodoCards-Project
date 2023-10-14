<script>
    import { slide } from "svelte/transition";
    export let info
    let showDescription = false
    
</script>

<div class="card" style="background-color: {info.cardColor};"
    role="button"
    on:click={()=>{showDescription = !showDescription}}
    on:keydown={e=>{if (e.key=="Enter") {showDescription = !showDescription}}}
    tabindex="0">

    <div class="title">{info.cardName}</div>
    {#if showDescription}
        <div class="description" transition:slide>
            {info.cardDue}
            {info.cardDescription}
        </div>
    {/if}
</div>

<style>
    .card {
        border-radius: 10px;
        padding: 15px;
        margin: 10px;
        max-width: 20em;
    }
    .title {
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        font-size: large;
        color: black;
    }
    .description{
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        color: black;
        font-size: small;
        padding-top: 15px;
    }
</style>