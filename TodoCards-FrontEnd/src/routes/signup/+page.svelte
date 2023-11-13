<script>
    import * as APIs from "$lib"

    let signup_username = ""
    let signup_password = ""
    let signup_confirm_password = ""
    let signup_status = false;

    let passwordNotMatching = false

    async function signup(){
        if (signup_password == signup_confirm_password) {
            signup_status = await APIs.signup(signup_username, signup_password)
            window.location.href = "/"
        }
        else {
            passwordNotMatching = true
        }
    }
</script>


<div class="signuppage">
    <h1>Sign up</h1>
    <div>
        <input type="text" placeholder="Username" bind:value={signup_username}>
    </div>
    <div>
        <input type="password" placeholder="Password" bind:value={signup_password}> 
    </div>
    <div>
        <input type="password" placeholder="Confirm Password" bind:value={signup_confirm_password}>
    </div>

    {#if passwordNotMatching}
    <p class="wrong-text">Please confirm your password again.</p>  
    {/if}
    <button on:click={signup}>Sign up</button>
</div>

<style>
    @import "../style.css";
    div {
        width: 300px;
        height: 40px;
    }
    .signuppage {
        margin-left: 15px;
    }
    input {
        width: 250px;
        height: 28px;
        border-radius: 16px;
        border-width: 1px;
        padding-left: 16px;
    }
    button {
        width: 268px;
        height: 30px;
        border: none;
        border-radius: 15px;
        background-color: rgb(90, 90, 255);
        color: white;
        font-weight: bold;
        cursor: pointer;
    }
    button:hover {
        background-color: rgb(111, 111, 255);
    }
    button:active {
        background-color: rgb(129, 129, 255);
    }
</style>