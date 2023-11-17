<script>
    import * as APIs from "$lib"
    import Modal from "../../modal.svelte"
    export let showModal = false, deckId, refresh

    let cardInfo = {
        cardName:           "",
        cardDescription:    "",
        cardDue:            "",
        cardColor:          "",
    }

    async function createCard(){
        let status = await APIs.createCard(deckId, cardInfo)
        if (status == true) {
            await refresh()
            showModal = false
        }
    }
    function cancel() {
        showModal = false
    }
</script>

<Modal bind:showModal={showModal}>
    <h1>Create Card</h1>
    cardName
    <input type="text" placeholder="cardName" bind:value={cardInfo.cardName}> <br>
    cardDescription
    <input type="text" placeholder="cardDescription" bind:value={cardInfo.cardDescription}> <br>
    cardDue
    <input type="text" placeholder="cardDue" bind:value={cardInfo.cardDue}> <br>
    cardColor
    <input type="text" placeholder="cardColor" bind:value={cardInfo.cardColor}> <br>
    <input type="button" value="submit" on:click={createCard}>
    <input type="button" value="cancel" on:click={cancel}>

</Modal>

