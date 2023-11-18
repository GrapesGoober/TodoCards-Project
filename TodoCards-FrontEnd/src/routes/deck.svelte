<script>
    export let deckinfo

    let formattedDue = ""
    if (deckinfo.nearestDue != "") {
        let cardDue_dateObj = new Date(deckinfo.nearestDue)
        formattedDue = new Intl.DateTimeFormat('en-US', {
            weekday: 'short',
            day: 'numeric',
            month: 'short'
        }).format(cardDue_dateObj);
    }

    function toCardsPage() {
        window.location.href = "/cards?deckId=" + deckinfo.deckId
    }
</script>

<div class="alldeck">
    <button on:click={toCardsPage} class="container">

    <!-- For card name & nearest date due -->
        <div class="text-container">
            <div class="deck-name"> {deckinfo.deckName} </div>
            <div> {formattedDue} </div>
        </div>

    <!-- For the multicolored cards icon -->
    <!--  <div class="icon-container">
        {#each deckinfo.cardColors as color, i}
            <div class="icon" style="
                background-color: {color}
            "> </div>
        {/each  }
    </div> -->
    </button>
</div>


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
        width: 300px;
        height: 54px;
        margin: 25px;
        padding-left: 20px;
        border: none;
        background-color: rgb(126, 126, 255);
        color: white;
        border-radius: 1em;
        text-align: left;
        display: flex;
        justify-content: space-between;
        align-items: center;
        cursor: pointer;

        transition: background-color 0.3s;
    }
    .container:hover {
        background-color: rgb(156, 156, 255);
    }
    .text-container {
        width: 20em;
    }
    .icon-container {
        display: inline;
    }
    .alldeck {
        margin-left: 5px;
    }
</style>