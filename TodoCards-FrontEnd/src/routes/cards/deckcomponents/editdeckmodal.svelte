<script>
    import * as APIs from "$lib"
    import Modal from "../../modal.svelte"
    import Useraccesslist from "./useraccesslist.svelte";
    export let showModal = false, deckInfo, refresh

    let shareDeckEditorViewer = false, usersToRemove = []
    
    async function editDeck(){
        let status = await APIs.editDeck(deckInfo)
        console.log(usersToRemove)
        usersToRemove.forEach(async user => {
            await APIs.removeAccess(deckInfo.deckId, user)
        }); 
        if (status == true) {
            await refresh()
            showModal = false
        }
    }

    function handleComboBoxChange(event) {
        const selectedValue = event.target.value;

        // Assuming shareDeckEditorViewer is a variable in your script
        // that determines whether to show the link section
        if (selectedValue === "option2" || selectedValue === "option3") {
            shareDeckEditorViewer = true;
        } else {
            shareDeckEditorViewer = false;
        }
    }

    function cancel() {
        usersToRemove = []
        showModal = false
    }
</script>


<Modal bind:showModal={showModal}>
    <div class="header">
        <button class="cancel_btn" on:click={cancel}><i class="fas fa-angle-left"></i></button>
        <h1>Edit Deck</h1>
    </div>

    <div class="deck-name">
        <p class="deckinfo-txt">Deck Name</p>
        <input type="text" placeholder="Name" bind:value={deckInfo.deckName}>
    </div>

    <div class="deck-description">
        <p class="deckinfo-txt">Description</p>
        <input type="text" placeholder="Description" bind:value={deckInfo.deckDescription}>
    </div>

    <Useraccesslist bind:deckId={deckInfo.deckId} bind:usersToRemove={usersToRemove}></Useraccesslist>
<!--------------------------------------------------->

    <div class="share-section"> <!--share section-->
        <i class="fas fa-user-plus fa-2xs share-icon"></i>
        <div class="share-icon">share</div>
        <div>
            <select class="share-combobx" id="myComboBox" name="myComboBox" on:change={handleComboBoxChange}>
                <option value="option1"></option>
                <option value="option2">Editor</option>
                <option value="option3">Viewer</option>
            </select>
        </div>
    </div>

    <!--link section will appear when you choose an option in share section-->
    {#if shareDeckEditorViewer}
    <div class="link-section">
        <div>Link</div>
        <div class="link-code">
            <div>1234567890</div>
            <i class="far fa-copy fa-xs copy-icon"></i>
        </div>
    </div>
    <p class="link-txt">This link will be expired in 3 minutes</p>
    {/if}

    <div class="delete-submit">
        <button class="red-button bobbing-hover">
            <i class="fas fa-trash-alt"></i>
        </button>

        <button class="green-button bobbing-hover"  on:click={editDeck}>
            <i class="fas fa-check-circle"></i>
        </button>

    </div>

</Modal>

<style>
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
    .share-section, .link-section, .link-code, .header, .delete-submit {
        display: flex;
        align-items: center;
    }
    .deck-name, .deck-description, .share-section, .link-section, .link-txt, .delete-submit {
        margin-left: 20px;
        margin-right: 20px;
        margin-bottom: 10px;
    }

    .header {
        margin: 10px;
    }

    .deckinfo-txt {
        margin-bottom: 4px;
    }

    .share-section {
        margin-bottom: 20px;
    }
    .share-icon {
        margin-right: 5px;
    }
    .share-combobx {
        padding: 3px;
        padding-left: 6px;
        border: solid;
        border-width: 1px;
        border-radius: 4px;
        border-color: rgb(156, 156, 156);
    }
    
    .link-code {
        width: 200px;
        justify-content: space-between;
        align-items: center;
        margin-left: 10px;

        padding: 3px;
        padding-left: 6px;
        padding-right: 6px;
        border: solid;
        border-width: 1px;
        border-radius: 4px;
    }
    .copy-icon {
        color: black;
        padding: 0;
        border: none;
        background-color: white;
        font-size: 15px;
        cursor: pointer;
    }
    .copy-icon:active {
        color: rgb(84, 84, 84);
    }
    .link-txt {
        color: red;
        font-size: 12px;
        margin-bottom: 25px;
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

    .delete-submit {
        justify-content: space-between;
        align-items: center;
    }
    .red-button {
        color: rgb(187, 0, 0);
        font-size: 20px;
        cursor: pointer;
        background-color: transparent;
        border: none;
    }
    .red-button:hover {
        color: rgb(229, 0, 0);
    }
    .green-button {
        color: green;
        font-size: 20px;
        cursor: pointer;
        background-color: transparent;
        border: none;
    }
    .green-button:hover {
        color: rgb(0, 194, 0);
    }
</style>