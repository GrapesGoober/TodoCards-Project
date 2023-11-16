<script>
    import * as APIs from "$lib"
    import Modal from "../modal.svelte"
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
    <div class="header">
        <button class="cancel_btn" on:click={cancel}><i class="fas fa-angle-left"></i></button>
        <h1>Create Card</h1>
    </div>


    <div class="name">
        <p class="info-txt">Card Name</p>
        <input type="text" placeholder="Name" bind:value={cardInfo.cardName}>
    </div>


    <div class="description">
        <p class="info-txt">Description</p>
        <input type="text" placeholder="Card Description" bind:value={cardInfo.cardDescription}>
    </div>


    <div class="description">
        <p class="info-txt">Due date</p>
        <input type="text" placeholder="datepicker" bind:value={cardInfo.cardDue}>
    </div>


    <div class="card-color">
        <p class="info-txt">Color</p>
        <input class="color-input" type="text" placeholder="cardColor" bind:value={cardInfo.cardColor}>
    </div>
    

    <div class="submit-section">
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <i class="fas fa-check-circle submit" on:click={createCard}></i>
    </div>

</Modal>

<style>
    @import "../style.css";
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
    .header, .submit-section {
        display: flex;
        align-items: center;
    }
    .name, .description, .submit-section {
        margin-left: 20px;
        margin-right: 20px;
        margin-bottom: 10px;
    }

    .header {
        margin: 10px;
    }

    .info-txt {
        margin-bottom: 4px;
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

    .card-color {
        display: flex;
        align-items: center;
        margin-left: 20px;
        margin-right: 20px;
        margin-top: 18px;
        margin-bottom: 10px;
    }
    .color-input {
        margin-left: 8px;
        width: 200px;
    }

    .submit-section {
        justify-content: end;
        align-items: center;
    }
    .submit {
        color: green;
        font-size: 20px;
        cursor: pointer;
    }
    .submit:active {
        color: rgb(0, 194, 0);
    }
</style>
