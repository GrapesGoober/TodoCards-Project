<script>
    import * as APIs from "$lib"

    async function logout(){
        status = await APIs.logout()
    }

</script>

<input type="button" value="logout" on:click={logout}>