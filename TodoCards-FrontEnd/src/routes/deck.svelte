<script>
    export let deckinfo
</script>

<div class="wrapper">

    <!-- For card name & nearest date due -->
    <div>
        <div> {deckinfo.deckName} </div>
        <div> {deckinfo.nearestDue} </div>
    </div>

    <!-- For the multicolored cards icon -->
    <div>
        {#each deckinfo.cardColors as color}
            <div style="background-color: {color}"> </div>
        {/each  }
    </div>
</div>