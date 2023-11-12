<script>
    export let deckinfo
    function toCardsPage() {
        window.location.href = "/cards?deckId=" + deckinfo.deckId
    }
</script>

<div class="wrapper">

    <button on:click={toCardsPage}>See cards</button>
    <!-- For card name & nearest date due -->
    <div>
        <div> {deckinfo.deckName} </div>
        <div> {deckinfo.nearestDue} </div>
    </div>

    <!-- For the multicolored cards icon -->
    <div>
        {#each deckinfo.cardColors as color}
            <div class="icon" style="background-color: {color}"> </div>
        {/each  }
    </div>

</div>

<style>
    .icon {
        width: 20px;
        height: 20px;
        border-radius: 2px;
    }
</style>