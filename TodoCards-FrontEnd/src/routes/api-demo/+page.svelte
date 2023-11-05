<script>
    import CardTemplate from "./CardTemplate.svelte";
    import DeckTemplate from "./DeckTemplate.svelte";
    import PingTemplate from "./PingTemplate.svelte";
    import UserTemplate from "./UserTemplate.svelte";
    import EditCardTemplate from "./EditCardTemplate.svelte";
  import EditDeckTemplate from "./EditDeckTemplate.svelte";
</script>

<h1>This is a demo for the APIs</h1>

<h2>Try pinging the server</h2>
<PingTemplate></PingTemplate>

<h2>Log in first</h2>
<UserTemplate></UserTemplate>
<h2>Get items (as list)</h2>
<DeckTemplate></DeckTemplate> <br>
<CardTemplate></CardTemplate>

<h2>Edit some Items</h2>
<h3>Some editing card</h3>
<EditCardTemplate></EditCardTemplate>
<h3>Some editing deck</h3>
<EditDeckTemplate></EditDeckTemplate>
