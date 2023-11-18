<script>
    function gotoUserSetting(){
        window.location.href = "/usersetting";
    }
</script>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<h1>Hello Admin
<button class="fas fa-user-circle user-btn" on:click={gotoUserSetting}></button>

</h1>


<style>
    @import "../style.css";
    h1 {
        margin: 0;
    }
    .user-btn {
        font-size: xx-large;
        border: none;
        color: rgb(89, 89, 89);
        cursor: pointer;
        transition: 0.15s;
        background-color: white;
        position:relative;
        left: 40%;
    }

    .user-btn:hover {
        color: rgb(145, 145, 145);
    }
</style>
