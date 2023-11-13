<script>
    export let deckinfo
    function toCardsPage() {
        window.location.href = "/cards?deckId=" + deckinfo.deckId
    }
</script>

<button on:click={toCardsPage} class="container">

    <!-- For card name & nearest date due -->
    <div class="text-container">
        <div class="deck-name"> {deckinfo.deckName} </div>
        <div> {deckinfo.nearestDue} </div>
    </div>

    <!-- For the multicolored cards icon -->
    <div class="icon-container">
        {#each deckinfo.cardColors as color, i}
            <div class="icon" style="
                background-color: {color}
            "> </div>
        {/each  }
    </div>

</button>

<style>
    .icon {
        width: 30px;
        height: 30px;
        border-radius: 4px;
        display: inline-block;
    }
    .deck-name {
        font-size: large;
    }
    .container {
        width: 30em;
        height: 5em;
        margin: 2em;
        padding-left: 20px;
        border: 1px solid black;
        border-radius: 1em;
        text-align: left;
        display: flex;
        justify-content: space-between;
    }
    .text-container {
        width: 20em;
    }
    .icon-container {
        display: inline;
    }
</style>