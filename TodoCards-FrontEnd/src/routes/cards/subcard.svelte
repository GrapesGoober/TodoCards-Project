<script>
    import * as APIs from "$lib"
    export let subcardinfo, refresh
    async function finishCard() {
        let status = await APIs.finishSubcard(subcardinfo.subcardId)
        console.log(status)
        if (status == true) {
            refresh()
        }
    }
</script>


<div class="wrapper">
    {#if subcardinfo.subcardIsFinished}
        <button class="tick bobbing-hover" on:click={finishCard}>
            <i class="fas fa-check-square fa-lg finished"></i>
        </button>
        <span class="finished">
            {subcardinfo.subcardName}
        </span>
    {:else}
        <button class="tick bobbing-hover" on:click={finishCard}>
            <i class="far fa-square fa-lg"></i>
        </button>
        <span>
            {subcardinfo.subcardName}
        </span>
    {/if}
</div>


<style>
    .wrapper{
        margin-left: 1em;
        width: 20em;
    }
    .tick {
        padding: 10px;
        background-color: transparent;
        border: none;
    }

    .finished {
        color: grey;
    }
    
</style>