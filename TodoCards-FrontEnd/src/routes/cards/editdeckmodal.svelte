<script>
    import * as APIs from "$lib"
    import Modal from "../modal.svelte"
    export let showModal = false, deckInfo, refresh

    async function editDeck(){
        let status = await APIs.editDeck(deckInfo)
        if (status == true) {
            refresh()
            showModal = false
        }
    }
    function cancel() {
        showModal = false
    }
</script>

<Modal bind:showModal={showModal}>
    <h1>Edit Deck</h1>
    cardName
    <input type="text" placeholder="cardName" bind:value={deckInfo.deckName}> <br>
    cardDescription
    <input type="text" placeholder="cardDescription" bind:value={deckInfo.deckDescription}> <br>
    <input type="button" value="submit" on:click={editDeck}>
    <input type="button" value="cancel" on:click={cancel}>

</Modal>

