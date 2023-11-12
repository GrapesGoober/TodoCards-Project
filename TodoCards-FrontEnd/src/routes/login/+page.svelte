<script>
    import * as APIs from "$lib"

    let username = "" // the input requires a username & password
    let password = ""
    let wrong_password_text = ""
    async function login(){
        let status = await APIs.login(username, password)
        // upon successful login, we wanna redirect user to home page 
        if (status == true) {
            // (which is default endpoint)
            window.location.href = "/";
        }
        // upon bad login, we might want to display something on the screen
        else {
            wrong_password_text = "username or password is incorrect"
        }
    }
</script>

<input type="text" placeholder="username" bind:value={username}>
<input type="password" placeholder="password" bind:value={password}>
<button on:click={login}>submit</button>