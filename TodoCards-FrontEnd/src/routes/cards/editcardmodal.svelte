<script>
    import * as APIs from "$lib"
    import Modal from "../modal.svelte"
    export let showModal = false, cardInfo, refresh

    async function editCard(){
        let status = await APIs.editCard(cardInfo)
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
    <h1>Edit Card</h1>
    cardName
    <input type="text" placeholder="cardName" bind:value={cardInfo.cardName}> <br>
    cardDescription
    <input type="text" placeholder="cardDescription" bind:value={cardInfo.cardDescription}> <br>
    cardDue
    <input type="text" placeholder="cardDue" bind:value={cardInfo.cardDue}> <br>
    cardColor
    <input type="text" placeholder="cardColor" bind:value={cardInfo.cardColor}> <br>
    <input type="button" value="submit" on:click={editCard}>
    <input type="button" value="cancel" on:click={cancel}>

</Modal>

