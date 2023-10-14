<script>
	import Card from './card.svelte';

	let cardShowDesc = false;
	let cardTitle = "This is Card"
	let cardDescription = "This is supposed to be a really long description of the card. "+
	"It can be as long as you'd like it doesn't matter. In fact, the longer the better."
	let cardColour = "green"

	function toggleCardDesc() {
		cardShowDesc = !cardShowDesc
	}
</script>

<h1>This is a demo for the cards</h1>

<a href="/">go back</a> <br>

<button on:click={toggleCardDesc}>toggle card description</button>
<input type="text" bind:value={cardTitle}>
<input type="textArea" bind:value={cardDescription}>
<input type="text" bind:value={cardColour}>

<Card 
bind:showDescription={cardShowDesc} 
bind:color={cardColour} 
bind:title={cardTitle}
bind:description={cardDescription}>
</Card>

