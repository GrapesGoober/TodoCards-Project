<script>
    import * as APIs from "$lib"
	import { clickOutside } from './clickOutside.js';
    export let subcardinfo, refresh, editable
    async function finishSubcard() {
        if (editable == true) {
            let status = await APIs.finishSubcard(subcardinfo.subcardId)
            if (status == true) {
                await refresh()
            }
        }
    }
    
    let isSelected = false
</script>


<button 
    class="wrapper {isSelected ? "selected" : ""}" 
    on:click={()=> {isSelected=!isSelected}}
    use:clickOutside on:click_outside={()=>{isSelected = false}}>

    {#if subcardinfo.subcardIsFinished}
        <button class="tick {editable ? "bobbing-hover" : ""}" on:click={finishSubcard}>
            <i class="fas fa-check-square fa-lg finished"></i>
        </button>
        <span class="finished">
            {subcardinfo.subcardName}
        </span>
        {#if editable && isSelected}
            <button class="tick trash bobbing-hover" on:click={finishSubcard}>
                <i class="fas fa-trash-alt finished"></i>
            </button>
        {/if}
    {:else}
        <button class="tick {editable ? "bobbing-hover" : ""}" on:click={finishSubcard}>
            <i class="far fa-square fa-lg"></i>
        </button>
        <span>
            {subcardinfo.subcardName}
        </span>
    {/if}
</button>


<style>

    .wrapper{
        display: block;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        margin-left: 1em;
        width: 20em;
        border: none;
        background-color: transparent;
        text-align: left;
    }
    .selected {
        border: 1px solid black;
    }
    .tick {
        padding: 10px;
        background-color: transparent;
        border: none;
    }

    .finished {
        color: grey;
    }
    
    .trash {
        position: absolute;
        left: 80%;        
    }
</style>