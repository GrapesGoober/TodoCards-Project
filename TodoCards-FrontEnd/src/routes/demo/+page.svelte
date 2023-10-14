<script>
	import Modal from './modal.svelte';
	import Card from './card.svelte';

	let count = 0
	let showModal = false;
	let cardShowDesc = false;
	let cardTitle = "This is Card"
	let cardDescription = "This is supposed to be a really long description of the card. "+
	"It can be as long as you'd like it doesn't matter. In fact, the longer the better."
	let cardColour = "green"

	function handleClick() {
		count += 1
	}

	let ping_count = 0
	async function ping () {
		console.log("sending ping request")
		const res = await fetch('http://127.0.0.1:5000/ping', {
			method: "GET"
		})
		
		const result = await res.json()
		if (result.message == "pong"){
			ping_count ++
			console.log("recieved pong")
		}
		
	}

	function modalOn() {
		showModal = true
	}

	function toggleCardDesc() {
		cardShowDesc = !cardShowDesc
	}
</script>

<h1>Click thy button</h1>

<a href="/">go back</a> <br>

<button on:click={handleClick}>
	Clicked {count}
	{count === 1 ? 'time' : 'times'}
</button>

<button on:click={ping}>
	pingMe!
	ping counter = {ping_count}
</button>

<button on:click={modalOn}>show modal</button>

<button on:click={toggleCardDesc}>toggle card description</button>
<input type="text" bind:value={cardTitle}>
<input type="textArea" bind:value={cardDescription}>
<input type="text" bind:value={cardColour}>

<Modal bind:showModal></Modal>

<Card 
bind:showDescription={cardShowDesc} 
bind:color={cardColour} 
bind:title={cardTitle}
bind:description={cardDescription}>
</Card>

