<script>
    import { slide } from "svelte/transition";
    export let title = ""
    export let dueDate = ""
    export let description = ""
    export let showDescription = false
    export let color = ""
</script>

<div class="card" style="background-color: {color};">
    <div class="title">{title}</div>
    {#if showDescription}
        <div class="description" transition:slide>
            {dueDate}
            {description}
        </div>
    {/if}
</div>

<style>
    .card {
        border-radius: 10px;
        padding: 15px;
        margin: 10px;
        max-width: 10em;
    }
    .title {
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        font-size: large;
        color: white;
    }
    .description{
        font-family: Verdana, Geneva, Tahoma, sans-serif;
        color: white;
        font-size: small;
        padding-top: 15px;
    }
</style>