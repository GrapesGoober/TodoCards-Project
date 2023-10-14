<script>
	import { onMount } from 'svelte';
	import Card from './card.svelte'

    // Each card-list is only limited to one deck at a time
	export let deckname = "QuickDeck"
    // An index to determine which card is currently being selected
    let selectedCards = []

    // Send request to backend to query the cards for us
    let cardslist = []
    async function getCardslist(){
        let response = await fetch("http://127.0.0.1:5000/get-cards-list", {
            method:"POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                deckname
            })
        })

        // recieve the cards
        cardslist = await response.json()
        console.log(cardslist)
        
        // cardslist[0] = {
        //     cardName: "Just an example card",
        //     cardDue: "Today",
        //     cardDescription: "This is supposed to be a really long description of the card. It can be as long as you'd like it doesn't matter. In fact, the longer the better.",
        //     cardColor: "lightgreen"
        // }
        // cardslist[1] = {
        //     cardName: "Just an example card",
        //     cardDue: "Today",
        //     cardDescription: "This is supposed to be a really long description of the card. It can be as long as you'd like it doesn't matter. In fact, the longer the better.",
        //     cardColor: "pink"
        // }

        selectedCards = [false, false]
    }
    onMount(getCardslist) 

</script>

<div>
    {#each cardslist as card, i}
    <div 
        role="button"
        on:click={()=>{selectedCards[i] = !selectedCards[i]}}
        on:keydown={e=>{if (e.key=="Enter") {selectedCards[i] = !selectedCards[i]}}}
        tabindex="0"
    >
        <Card 
            bind:name={card.cardName}
            bind:dueDate={card.cardDue}
            bind:description={card.cardDescription}
            bind:showDescription={selectedCards[i]}
            bind:color={card.cardColor}
        ></Card>
    </div>
    {/each}
</div>

