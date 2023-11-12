<script>
  import { onMount } from "svelte";

    // Need to get the deckId for this page
    let searchParams
    let deckId

    onMount( () => {
        searchParams = new URLSearchParams(window.location.search)
        deckId = searchParams.get("deckId")
    })
    
</script>

<h1>This is the cardslist page</h1>
<p>The deckid of this page = {deckId}</p>