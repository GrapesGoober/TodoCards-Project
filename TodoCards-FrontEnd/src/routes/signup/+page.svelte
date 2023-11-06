<script>
    import * as APIs from "$lib"

    let signup_username = ""
    let signup_password = ""
    let signup_status = false;
    async function signup(){
        signup_status = await APIs.signup(signup_username, signup_password)
    }
</script>