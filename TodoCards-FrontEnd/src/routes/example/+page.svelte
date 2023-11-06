<script>
    let cardname = ""
    let cardDescription = ""

    const today = new Date();
    const year = today.getFullYear();
    const month = String(today.getMonth() + 1).padStart(2, '0'); // Month is zero-based, so we add 1 and pad with '0' if necessary
    const day = String(today.getDate()).padStart(2, '0');

    let todayString = `${year}-${month}-${day}`
    let cardDue = todayString


    function clickSomething () {
        alert("I am an alert box!");
    }

    async function ping () {
		let res = await fetch('http://127.0.0.1:5000/ping', {
			method: "GET"
		})
		
		let result = await res.json()
        alert(result)
		
	}
</script>


<head> <!--create new card page-->
    <title>ToDo Cards</title>
	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
</head>


<header class="createcard">
    Create new card
</header>

<p> {cardname} </p>

<span>Card name: </span>
<input type="text" bind:value={cardname}>

<br>

<p> {cardDescription} </p>
<span>Description: </span>
<input type="text" bind:value={cardDescription}>

<br>

<span for="datepicker">Due Date:</span>
<input type="date" id="datepicker" min={todayString} bind:value={cardDue}>

<br>

<button class="far fa-times-circle cross_btn"></button>

<button class="far fa-check-circle tick_btn" on:click={clickSomething}></button>

<button on:click={ping} > ping </button>

<style>
    .tick_btn {
        color: green;
        font-size: 200%;
    }

    .cross_btn {
        color: red;
        font-size: 200%;

    }
</style>