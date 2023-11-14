<script>
    import * as APIs from "$lib"
    import { onMount } from "svelte";
	import Card from './card.svelte'
    import EditdeckModal from "./editdeckmodal.svelte";

    // Send request to backend to query the cards for us
    let cardslist = []
    let deckinfo
    async function getCardslistAndDeckInfo(){
        // get the cardslist
        let searchParams = new URLSearchParams(window.location.search)
        let deckId = searchParams.get("deckId")
        cardslist = await APIs.getCardslist(deckId)

        // also get the deck info to display as well
        let deckslist = await APIs.getDeckslist()
        deckinfo = deckslist.find(deck => deck.deckId == deckId)
    }
    onMount(getCardslistAndDeckInfo)
    
    let isEditing = false
    async function showEditDeckModal(){
        isEditing = true
    }

    
</script>

<!-- Font Awesome 5 Free -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<EditdeckModal
    bind:showModal={isEditing} 
    bind:deckInfo={deckinfo}
    refresh={getCardslistAndDeckInfo}>
</EditdeckModal>

{#if deckinfo}
    <h1>{deckinfo.deckName}
        <button class="edit-button bobbing-hover" on:click={showEditDeckModal}>
            <i class="fas fa-edit"></i>
        </button>
    </h1>
    
    {#if deckinfo.nearestDue != ""}
        <p><b>Nearest Due Date</b> {deckinfo.nearestDue}</p>
    {/if}
    <p>{deckinfo.deckDescription}</p>
{/if}

<button on:click={getCardslistAndDeckInfo}>refresh</button>

<div>
    {#each cardslist as card}
        <Card bind:cardinfo={card} refresh={getCardslistAndDeckInfo}></Card>
    {/each}
</div>

<style>
    @import "../style.css";

    .edit-button {
        left: 10px;
    }
</style>