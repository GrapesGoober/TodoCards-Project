<script>
    import * as APIs from "$lib"

    let username = "" // the input requires a username & password
    let password = ""
    let wrong_password_text = ""
    let status = false
    async function login(){
        status = await APIs.login(username, password)
        // upon successful login, we wanna redirect user to home page 
        if (status == true) {
            // (which is default endpoint)
            window.location.href = "http://localhost:5173";
        }
        // upon bad login, we might want to display something on the screen
        else {
            wrong_password_text = "username or password is incorrect"
        }
    }
</script>

login status = {status} <br>
<input type="text" placeholder="username" bind:value={username}>
<input type="password" placeholder="password" bind:value={password}>
<button on:click={login}>submit</button>