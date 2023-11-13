<script>
    import * as APIs from "$lib"

    let username = "" // the input requires a username & password
    let password = ""
    let wrongPassword = false
    async function login(){
        let status = await APIs.login(username, password)
        // upon successful login, we wanna redirect user to home page 
        if (status == true) {
            // (which is default endpoint)
            window.location.href = "/";
        }
        // upon bad login, we might want to display something on the screen
        else {
            wrongPassword = true
        }
    }

    function goToSignup() {
        window.location.href = "/signup";
    }
</script>

<h1>Login</h1>
<input type="text" placeholder="username" bind:value={username}>
<input type="password" placeholder="password" bind:value={password}>
<button on:click={login}>submit</button>
{#if wrongPassword}
    <p class="wrong-text">username or password is incorrect</p>  
{/if}
<br>
<p>If you don't have an account, sign up <a href="/signup">here</a> </p>

<style>
    @import "../style.css";
    .wrong-text {
        color: red;
    }
</style>