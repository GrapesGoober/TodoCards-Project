<script>
    // Need to get the deckId for this page
    let searchParams = new URLSearchParams(window.location.search);
    let deckId = searchParams.get("deckId");
    
</script>

<h1>This is the cardslist page</h1>
<p>The deckid of this page = {deckId}</p>