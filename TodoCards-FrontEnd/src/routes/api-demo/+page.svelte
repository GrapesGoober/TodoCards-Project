<script>
    import CardTemplate from "./CardTemplate.svelte";
    import PingTemplate from "./PingTemplate.svelte";
    import UserTemplate from "./UserTemplate.svelte";
</script>

<h1>This is a demo for the APIs</h1>

<h2>Try pinging the server</h2>
<PingTemplate></PingTemplate>

<h2>Log in first</h2>
<UserTemplate></UserTemplate>


<h2>Some cards-list test</h2>
<CardTemplate></CardTemplate>