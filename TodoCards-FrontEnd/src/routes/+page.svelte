<script>
    import Deckslist from "./deckslist.svelte";
</script>

<!-- Font Awesome 5 Free -->
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">

<!--This is the deckslist page (the home page)-->
<div class="header">
    <h1 class="todo-header">Todo</h1>
    <div>profilepic</div>
</div>
<div>
    <Deckslist></Deckslist>
</div>
<div class="header">
    <button class="edit-btn">Edit</button>
    <button class="fas fa-plus-circle add-btn"></button>
</div>

<style>
    @import "./style.css";
    h1 {
        margin: 0;
    }
    .header {
        margin-top: 20px;
        margin-left: 26px;
        width: 450px;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    .edit-btn {
        font-size: 23px;
        border: none;
        background-color: white;
        cursor: pointer;
    }
    .edit-btn:hover {
        color: rgb(100, 100, 100);
    }
    .edit-btn:active {
        color: rgb(139, 139, 139);
    }
    .add-btn {
        font-size: xx-large;
        padding: 0;
        height: 40px;
        width: 40px;
        border: none;
        border-radius: 50%;
        color: green;
        transition: background-color 0.15s, color 0.15s, border-color 0.15s;
    }
    .add-btn:hover {
        background-color: green;
        color: white;
    }
    .add-btn:active {
        background-color: rgb(0, 169, 0);
        border-color: rgb(0, 169, 0);
    }
</style>