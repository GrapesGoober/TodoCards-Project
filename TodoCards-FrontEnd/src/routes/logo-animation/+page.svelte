<script>
	import { fade } from "svelte/transition";

    let colors = ["pink", "lightgreen", "lightblue", "khaki", "lightcoral", "peachpuff", "plum"]
</script>

<div class="wrapper">
    {#each colors as color, i}
        <div class="card" transition:fade={{delay: 1000}}
        style="
            background-color: {color};
            transform: 
                rotate({i*50 + Math.random()*20}deg) 
                translate({120 + Math.random()*30}px, 0px) 
                rotate({Math.random()*360}deg);
        "> </div>
    {/each}
</div>

<style>

    .wrapper {
        text-align: center;
        justify-content: center;
        display: flex;
    }
    .card {
        width: 50px;
        height: 50px;
        position: absolute;
        left: 50%;
        top: 50%;
        border-radius: 10px;
        animation-duration: 2s;
    }
</style>