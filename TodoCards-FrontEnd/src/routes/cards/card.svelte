<script>
    import * as APIs from "$lib"
    import { slide } from "svelte/transition";
    import Subcardlist from "./subcardlist.svelte";
    export let cardinfo, refresh
    let showDescription = false
    async function finishCard() {
        let status = await APIs.finishCard(cardinfo.cardId)
        if (status == true) {
            refresh()
        }
    }
</script>


<div class="wrapper">

    {#if cardinfo.cardIsFinished}
        <div class="card" style="background-color: lightgrey;">
            <button class="tick" on:click={finishCard}>
                <i class="fas fa-check-square fa-lg isFinished"></i>
            </button>

            <button class="title isFinished" on:click={()=>{showDescription = !showDescription}}>
                {cardinfo.cardName}
            </button>
        </div>
    {:else}
        <div class="card" style="background-color: {cardinfo.cardColor};">
            <button class="tick" on:click={finishCard}>
                <i class="far fa-square fa-lg"></i>
            </button>

            <button class="title" on:click={()=>{showDescription = !showDescription}}>
                {cardinfo.cardName}
            </button>
        </div>
    {/if}
    
    {#if showDescription}
        <div class="description" transition:slide>
            <!-- <i class="fas fa-spinner fa-pulse"></i> <br> -->
            Due {cardinfo.cardDue} <br>
            {cardinfo.cardDescription}
            <Subcardlist bind:cardId={cardinfo.cardId} refresh={refresh}></Subcardlist>
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
        font-size: small;
        width: 20em;
        padding: 15px;
    }

    .isFinished {
        color: grey;
    }
</style>