<script>
    import { slide } from "svelte/transition";
    export let info
    let showDescription = false
    let isFinished = false
</script>

<div class="wrapper">

    {#if isFinished}
        <div class="card" style="background-color: lightgrey;">
            <button class="tick" on:click={()=>{isFinished = false}}>
                <i class="fas fa-check-square fa-lg isFinished"></i>
            </button>

            <button class="title isFinished" on:click={()=>{showDescription = !showDescription}}>
                {info.cardName}
            </button>
        </div>
    {:else}
        <div class="card" style="background-color: {info.cardColor};">
            <button class="tick" on:click={()=>{isFinished = true}}>
                <i class="far fa-square fa-lg"></i>
            </button>

            <button class="title" on:click={()=>{showDescription = !showDescription}}>
                {info.cardName}
            </button>
        </div>
    {/if}
    
    {#if showDescription}
        <div class="description" transition:slide>
            <i class="fas fa-spinner fa-pulse"></i> <br>
            Due {info.cardDue} <br>
            {info.cardDescription}
        </div>
    {/if}
</div>


<style>
    .wrapper{
        padding: 10px;
        width: 20em;
    }
    .card {
        border-radius: 10px;
        border: none;
        display: flex;
        width: 100%;
    }
    .title {
        background-color: transparent;
        font-size: large;
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        text-align: left;
        border: none;
        width: 16em;
        height: 100%;
        padding: 10px;
    }
    .tick {
        padding-left: 20px;
        background-color: transparent;
        border: none;
    }
    .description {
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        font-size: small;
        width: 20em;
        padding: 15px;
    }

    .isFinished {
        color: grey;
    }
</style>