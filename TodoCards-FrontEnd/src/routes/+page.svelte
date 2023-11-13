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
    <button class="edit_btn">Edit</button>
    <button class="add_btn">+</button>
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
    .edit_btn {
        font-size: 23px;
        border: none;
        background-color: white;
        cursor: pointer;
    }
    .edit_btn:hover {
        color: rgb(100, 100, 100);
    }
    .edit_btn:active {
        color: rgb(139, 139, 139);
    }
    .add_btn {
        font-size: 25px;
        font-weight: bold;
        vertical-align: middle;
        text-align: center;
        height: 40px;
        width: 40px;
        border-radius: 50%;
        border-style: solid;
        border-width: 3.5px;
        background-color: white;
        color: green;
        border-color: green;

        transition: background-color 0.15s, color 0.15s, border-color 0.15s;
    }
    .add_btn:hover {
        background-color: green;
        color: white;
    }
    .add_btn:active {
        background-color: rgb(0, 169, 0);
        border-color: rgb(0, 169, 0);
    }
</style>