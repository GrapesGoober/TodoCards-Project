<script>
    import * as APIs from "$lib"

    let cardId = 1
    let finishCardResult = false
    async function finishCard(){
        finishCardResult = await APIs.finishCard(cardId)
    }
    let subcardId = 1
    let finishSubardResult = false
    async function finishSubcard(){
        finishSubardResult = await APIs.finishSubcard(subcardId)
    }
</script>

<p>finishCardResult = {finishCardResult}</p>
<input type="button" value="Finish Card!" on:click={finishCard}>
<p>finishCardResult = {finishSubardResult}</p>
<input type="button" value="Finish Subcard!" on:click={finishSubcard}>