<script>
    import * as APIs from "$lib"

    let username = "" // the input requires a username & password
    let password = ""
    let status = false // status can either be true or false
    async function login(){
        status = await APIs.login(username, password)
    }
</script>

login status = {status} <br>
<input type="text" placeholder="username" bind:value={username}>
<input type="password" placeholder="password" bind:value={password}>
<input type="button" value="login" on:click={login}>