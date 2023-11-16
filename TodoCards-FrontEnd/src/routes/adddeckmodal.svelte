<script>
    import * as APIs from "$lib"
    import Modal from "./modal.svelte"
    export let showModal = false, refresh
    let deckInfo = {
        deckName:           "",
        deckDescription:    ""
    }

    async function addDeck(){
        let status = await APIs.addDeck(deckInfo)
        if (status == true) {
            refresh()
            showModal = false
        }
    }
    function cancel() {
        showModal = false
    }
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<Modal bind:showModal={showModal}>
    <div class="header">
        <button class="cancel_btn" on:click={cancel}><i class="fas fa-angle-left"></i></button>
        <h1>Add Deck</h1>
    </div>

    <div class="deck-name">
        <p class="deckinfo-txt">Deck</p>
        <input type="text" placeholder="Name" bind:value={deckInfo.deckName}>
    </div>

    <div class="deck-description">
        <p class="deckinfo-txt">Description</p>
        <input type="text" placeholder="Description" bind:value={deckInfo.deckDescription}>
    </div>

    <div class="delete-submit">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <i class="fas fa-check-circle submit" on:click={addDeck}></i>
    </div>
</Modal>

<style>
    @import "./style.css";
    p {
        margin: 0;
    }
    h1 {
        margin: 0;
    }
    input {
        width: 250px;
        padding: 4px;
        padding-left: 6px;
        border: solid;
        border-width: 1px;
        border-radius: 4px;
        border-color: rgb(156, 156, 156);
    }
    input:focus {
        box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.3);
    }
    .header {
        display: flex;
        align-items: center;
        margin: 10px;
    }
    .cancel_btn {
        font-size: 36px;
        background-color: white;
        border: none;
        padding-right: 15px;
        cursor: pointer;
    }
    .cancel_btn:active {
        color: rgb(77, 77, 77);
    }
    .deck-name, .deck-description, .delete-submit {
        margin-left: 20px;
        margin-right: 20px;
        margin-bottom: 10px;
    }
    .deckinfo-txt {
        margin-bottom: 4px;
    }
    .delete-submit {
        display: flex;
        align-items: center;
        justify-content: end;
    }
    .submit {
        margin-top: 10px;
        color: green;
        font-size: 20px;
        cursor: pointer;
    }
    .submit:active {
        color: rgb(0, 194, 0);
    }
</style>

