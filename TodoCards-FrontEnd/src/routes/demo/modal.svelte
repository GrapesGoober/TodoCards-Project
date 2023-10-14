<script>
    import { fade } from "svelte/transition";

    export let showModal = false;

    function modalOff() {
        showModal = false;
    }

</script>

{#if showModal}
    <div class="modal-backdrop" transition:fade>
        <div class="modal-box">
            <h1>This is my modal</h1>
            <button on:click={modalOff}>modal be gone</button>
        </div>
    </div>
{/if}

<style>
    .modal-backdrop {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        display: flex;
        align-items: center;
        justify-content: center;
    }

    .modal-box {
        background-color: white;
        padding: 10px;
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }
</style>