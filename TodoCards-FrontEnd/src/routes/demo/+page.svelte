<script>
	let count = 0;

	function handleClick() {
		count += 1;
	}
</script>

<h1>Click thy button</h1>

<button on:click={handleClick}>
	Clicked {count}
	{count === 1 ? 'time' : 'times'}
</button>

<a href="/">go back</a>
