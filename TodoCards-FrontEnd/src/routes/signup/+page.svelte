<script>
    import * as APIs from "$lib"

    let signup_username = ""
    let signup_password = ""
    let signup_status = false;
    async function signup(){
        signup_status = await APIs.signup(signup_username, signup_password)
    }
</script>


signup_status = {signup_status} <br>
<input type="text" placeholder="username" bind:value={signup_username}>
<input type="password" placeholder="password" bind:value={signup_password}> 
<input type="button" value="signup" on:click={signup}> <br>