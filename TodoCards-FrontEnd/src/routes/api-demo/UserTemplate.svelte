<script>

    let username = "" // the input requires a username & password
    let password = ""
    let status = false // status can either be true or false
    async function login(){
        let response = await fetch("http://127.0.0.1:5000/login", {
            method:"POST",
            credentials: "include",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                password
            })
        })

        // recieve the result
        status = await response.json()
    }

</script>

login status = {status} <br>
<input type="text" placeholder="username" bind:value={username}>
<input type="password" placeholder="password" bind:value={password}>
<input type="button" value="login" on:click={login}>