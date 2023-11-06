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
            window.location.href = "http://localhost:5173";
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

<!-- Using the svelte's if logic block to handle conditioning -->
{#if wrong_password_text != ""}
    <!-- Using a css class to style this red -->
    <!-- Note: use the {curly brackers} to denote that the text is a variable -->
    <p class="login-error">{wrong_password_text}</p>
{/if}

<style>
    /* Might wanna add some styling further, if so wish */
    .login-error {
        color: red;
    }
</style>