<script>
    import * as APIs from "$lib"
    import Modal from "../modal.svelte"
    export let showModal = false, deckInfo, refresh

    let shareDeckEditorViewer = false
    
    async function editDeck(){
        let status = await APIs.editDeck(deckInfo)
        if (status == true) {
            refresh()
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
        showModal = false
    }
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<Modal bind:showModal={showModal}>
    <div class="header">
        <button class="cancel_btn" on:click={cancel}><i class="fas fa-angle-left"></i></button>
        <h1>Edit Deck</h1>
    </div>

    <div class="deck-name">
        <p class="deckinfo-txt">Deck</p>
        <input type="text" placeholder="Name" bind:value={deckInfo.deckName}>
    </div>

    <div class="deck-description">
        <p class="deckinfo-txt">Description</p>
        <input type="text" placeholder="Description" bind:value={deckInfo.deckDescription}>
    </div>

<!--these are just UI. The users in these section are not real-->

    <div class="editor-viewer-section"> <!--this part doesn't appear if you don't have other editors-->
        <div>Editor: </div>
        <div class="editor-viewer-name">
            <p class="shared-user">awacado</p>
            <button class="user-delete"><i class="fas fa-times"></i></button>
        </div>

        <div class="editor-viewer-name">
            <p class="shared-user">Elle</p>
            <button class="user-delete"><i class="fas fa-times"></i></button>
        </div>
    </div>
    <div class="editor-viewer-section"> <!--this part doesn't appear if you don't have other viewer-->
        <div>Viewer: </div>
        <div class="editor-viewer-name">
            <p class="shared-user">Grapes</p>
            <button class="user-delete"><i class="fas fa-times"></i></button>
        </div>

        <div class="editor-viewer-name">
            <p class="shared-user">Picnic</p>
            <button class="user-delete"><i class="fas fa-times"></i></button>
        </div>

        <div class="editor-viewer-name">
            <p class="shared-user">Guin</p>
            <button class="user-delete"><i class="fas fa-times"></i></button>
        </div>
    </div>

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
        <i class="fas fa-trash-alt deletedeck"></i>
        <!-- svelte-ignore a11y-click-events-have-key-events -->
        <!-- svelte-ignore a11y-no-static-element-interactions -->
        <i class="fas fa-check-circle submit" on:click={editDeck}></i>

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
    .editor-viewer-section, .editor-viewer-name, .share-section, .link-section, .link-code, .header, .delete-submit {
        display: flex;
        align-items: center;
    }
    .deck-name, .deck-description, .editor-viewer-section, .share-section, .link-section, .link-txt, .delete-submit {
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

    .editor-viewer-name {
        background-color: rgb(110, 110, 255);
        color: white;
        border-radius: 15px;
        margin-left: 4px;
        padding-left: 8px;
        padding-right: 8px;
        padding-top: 3px;
        padding-bottom: 3px;
        align-items: center;
        text-align: center;
    }
    .shared-user {
        font-size: 14px;
    }
    .user-delete {
        color: white;
        background-color: rgb(110, 110, 255);
        border: none;
        font-weight: bold;
        padding: 0;
        margin-left: 5px;
        cursor: pointer;
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
    }
    .deletedeck {
        color: rgb(187, 0, 0);
        font-size: 20px;
        cursor: pointer;
    }
    .deletedeck:active {
        color: rgb(229, 0, 0);
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