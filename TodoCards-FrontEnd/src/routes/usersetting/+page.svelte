<script>
    async function goback(){
        window.location.href = "/";
    }
</script>

<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<div class="header">
    <!--might add an icon for going back to login page-->
    <button class="goback_btn" on:click={goback}><i class="fas fa-angle-left"></i></button>
    <p class="logout">Log out</p>
</div>

<div class="user-profile">
    <i class="fas fa-user-circle user-pic"></i>
</div>

<div class="edit-username-section">
    <p class="text">Username</p>
    <input type="text" placeholder="Username">
</div>

<div class="password-section">
    <p class="text">Change password</p>
    <div class="edit-pass-section">
        <p class="text">Old password</p>
        <input type="text">
    </div>
    <div class="edit-pass-section">
        <p class="text">New password</p>
        <input type="text">
    </div>
    <div class="edit-pass-section">
        <p class="text">Confirm New password</p>
        <input type="text">
    </div>
</div>

<div class="user-submit">
    <!-- svelte-ignore a11y-click-events-have-key-events -->
    <!-- svelte-ignore a11y-no-static-element-interactions -->
    <i class="fas fa-check-circle submit"></i>
</div>

<style>
    @import "../style.css";
    p {
        margin: 0;
        font-size: 13px;
    }
    input {
        width: 100%;
        padding: 4px;
        padding-left: 6px;
        border: solid;
        border-width: 1px;
        border-radius: 4px;
        border-color: rgb(156, 156, 156);
    }
    input:focus {
        box-shadow: 0px 0px 4px rgba(0, 0, 0, 0.3);
    }
    .header {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .goback_btn {
        font-weight: bold;
        font-size: 36px;
        margin-right: 12px;
        background-color: white;
        padding: 0;
        border: none;
        cursor: pointer;
    }
    .goback_btn:active {
        color: rgb(77, 77, 77);
    }
    .logout {
        font-weight: bold;
        cursor: pointer;
    }
    .logout:active {
        color: rgb(103, 103, 103);
    }
    .user-profile {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .user-pic {
        font-size: 75px;
        color: rgb(46, 0, 144);
    }
    .text {
        margin-right: 7px;
    }
    
    .edit-username-section {
        display: flex;
        align-items: center;
        margin: 20px;
    }
    .password-section {
        margin: 20px;
    }
    .edit-pass-section {
        display: flex;
        align-items: center;
        margin-top: 8px;
        margin-bottom: 8px;
    }
    .user-submit {
        display: flex;
        align-items: center;
        justify-content: end;
    }
    .submit {
        margin-top: 8px;
        margin-right: 8px;
        color: green;
        font-size: 25px;
        cursor: pointer;
    }
    .submit:active {
        color: rgb(0, 194, 0);
    }
</style>