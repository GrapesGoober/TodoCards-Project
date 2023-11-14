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
        <button class="tick" on:click={finishCard}>
            <i class="fas fa-check-square fa-lg finished"></i>
        </button>
        <span class="finished">
            {subcardinfo.subcardName}
        </span>
    {:else}
        <button class="tick" on:click={finishCard}>
            <i class="far fa-square fa-lg"></i>
        </button>
        <span>
            {subcardinfo.subcardName}
        </span>
    {/if}
</div>


<style>
    .wrapper{
        padding: 5px;
        margin: 0.5em;
        width: 20em;
    }
    .tick {
        background-color: transparent;
        border: none;
        position: relative;
        left: 0px;
        top: 0px;
        transition: 0.1s ease-in-out;
    }
    .tick:hover {
        position: relative;
        left: -2px;
        top: -2px;
    }

    .finished {
        color: grey;
    }
    
</style>