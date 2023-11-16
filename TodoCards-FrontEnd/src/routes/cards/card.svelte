<script>
    import * as APIs from "$lib"
    import Subcardlist from "./subcardlist.svelte";
    import EditcardModal from "./editcardmodal.svelte";
    export let cardinfo, refresh, editable
    
    let showDescription = false
    async function finishCard() {
        if (editable == true) {
            let status = await APIs.finishCard(cardinfo.cardId)
            if (status == true) {
                refresh()
            }
        }
    }
    let isEditing = false
    let currentlyEditingCard
    function showEdit(cardinfo) {
        currentlyEditingCard = cardinfo
        isEditing = true
    }

</script>

{#if isEditing}
<EditcardModal 
    bind:showModal={isEditing} 
    bind:cardInfo={currentlyEditingCard}
    refresh={refresh}>
</EditcardModal>
{/if}

<div class="wrapper">

    {#if cardinfo.cardIsFinished}
        <div class="card" style="background-color: lightgrey;">
            <button class="tick {editable ? "bobbing-hover" : ""}" on:click={finishCard}>
                <i class="fas fa-check-square fa-lg isFinished"></i>
            </button>

            <button class="title isFinished" on:click={()=>{showDescription = !showDescription}}>
                {cardinfo.cardName}
            </button>

            {#if showDescription && editable}
            <button class="edit-button bobbing-hover" on:click={()=>{showEdit(cardinfo)}}>
                <i class="fas fa-edit"></i>
            </button>
            {/if}
        </div>
        
        
    {:else}
        <div class="card" style="background-color: {cardinfo.cardColor};">
            <button class="tick {editable ? "bobbing-hover" : ""}" on:click={finishCard}>
                <i class="far fa-square fa-lg"></i>
            </button>

            <button class="title" on:click={()=>{showDescription = !showDescription}}>
                {cardinfo.cardName}
            </button>            

            {#if showDescription && editable}
                <button class="edit-button bobbing-hover" on:click={()=>{showEdit(cardinfo)}}>
                    <i class="fas fa-edit "></i>
                </button>
            {/if}
        </div>

    {/if}
    
    {#if showDescription}
        <div class="description-box">
            <!-- <i class="fas fa-spinner fa-pulse"></i> <br> -->
            <div>
                <p> Due {cardinfo.cardDue} </p>
                <p>{cardinfo.cardDescription} </p>
            </div>
            <Subcardlist 
                bind:cardId={cardinfo.cardId} 
                bind:editable={editable} 
                refresh={refresh}>
            </Subcardlist>
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

    .description-box {
        font-size: small;
        width: 20em;
        padding-left: 15px;
    }

    .isFinished {
        color: grey;
    }

    .edit-button {
        left: -10px;
    }
</style>