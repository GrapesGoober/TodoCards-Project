<script>
    import * as APIs from "$lib"

    let username = "" // the input requires a username & password
    let password = ""
    let status = false // status can either be true or false
    async function login(){
        status = await APIs.login(username, password)
    }
</script>

<input type="text" placeholder="username" bind:value={username}>
<input type="password" placeholder="password" bind:value={password}>
<button on:click={login}>submit</button>