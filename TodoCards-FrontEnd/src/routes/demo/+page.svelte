<script>
	let count = 0

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
		}
	}
</script>

<h1>Click thy button</h1>

<button on:click={handleClick}>
	Clicked {count}
	{count === 1 ? 'time' : 'times'}
</button>

<button on:click={ping}>
	pingMe!
	ping counter = {ping_count}
</button>

<a href="/">go back</a>
